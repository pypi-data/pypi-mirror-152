# AutoTransform
# Large scale, component based code modification library
#
# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2022-present Nathan Rockenbach <http://github.com/nathro>

# @black_format

"""The implementation for the GithubRepo."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Mapping, Optional, Sequence

from typing_extensions import NotRequired

import autotransform.schema
from autotransform.batcher.base import Batch
from autotransform.change.base import Change
from autotransform.change.github import GithubChange
from autotransform.event.debug import DebugEvent
from autotransform.event.handler import EventHandler
from autotransform.repo.git import GitRepo, GitRepoParams
from autotransform.repo.type import RepoType
from autotransform.util.github import GithubUtils


class GithubRepoParams(GitRepoParams):
    """The param type for a GithubRepo."""

    full_github_name: str
    required_labels: NotRequired[List[str]]
    hide_automation_info: NotRequired[bool]
    hide_autotransform_docs: NotRequired[bool]


class GithubRepo(GitRepo):
    """A Repo that provides support for submitting changes as a pull request against
    a Github repo.

    Attributes:
        _params (GithubRepoParams): Contains all git params as well as the Github repo
            name and any required labels.
        __github_repos (Dict[str, Repository.Repository]): A mapping of repo names to repos. Used
            for caching.
    """

    _params: GithubRepoParams

    def __init__(self, params: GithubRepoParams):
        """Establishes the Github object to enable API access.

        Args:
            params (GithubRepoParams): The paramaters used to set up the GithubRepo.
        """

        GitRepo.__init__(self, params)

    @staticmethod
    def get_type() -> RepoType:
        """Used to map Repo components 1:1 with an enum, allowing construction from JSON.

        Returns:
            RepoType: The unique type associated with this Repo
        """

        return RepoType.GITHUB

    def submit(
        self,
        batch: Batch,
        _transform_data: Optional[Mapping[str, Any]],
        change: Optional[Change] = None,
    ) -> None:
        """Performs the normal submit for a git repo then submits a pull request
        against the provided Github repo.

        Args:
            batch (Batch): The Batch for which the changes were made.
            _transform_data (Optional[Mapping[str, Any]]): Data from the transformation. Unused.
            change (Optional[Change]): An associated change which should be updated.
                Defaults to None.
        """

        title = GitRepo.get_commit_message(batch["title"])

        self.commit(batch["title"], change is not None)

        commit_branch = GitRepo.get_branch_name(batch["title"])
        remote = self._local_repo.remote()
        if change is not None:
            self._local_repo.git.push(remote.name, "-u", "-f", commit_branch)
            return

        self._local_repo.git.push(remote.name, "-u", commit_branch)

        body = batch["metadata"].get("body", None)

        if self._params.get("hide_automation_info", False):
            automation_info = ""
        else:
            automation_info = "\n\n" + self.get_automation_info(batch)

        assert body is not None, "All pull requests must have a body."
        pull_request = GithubUtils.get(self._params["full_github_name"]).create_pull_request(
            title,
            f"{str(body)}{automation_info}",
            self._base_branch.name,
            commit_branch,
        )

        EventHandler.get().handle(
            DebugEvent({"message": f"Pull request created: {pull_request.number}"})
        )

        # Add labels
        labels = batch["metadata"].get("labels", [])
        assert isinstance(labels, List)
        labels.extend(self._params.get("required_labels", []))
        if len(labels) > 0:
            pull_request.add_labels(labels)

    def get_automation_info(self, batch: Batch) -> str:
        """Gets information on automating with AutoTransform.

        Args:
            batch (Batch): The Batch the change is being made for.

        Returns:
            str: The text for automating.
        """

        # Create body content with information on replicating the change
        automation_info_lines = ["ADDED AUTOMATICALLY BY AUTOTRANSFORM"]
        if not self._params.get("hide_autotransform_docs", False):
            automation_info_lines.append(
                "Learn more about AutoTransform [here](https://autotransform.readthedocs.io)"
            )
        automation_info_lines.append("Schema and batch information for the change below")

        # Add schema JSON
        current_schema = autotransform.schema.current
        if current_schema is not None:
            automation_info_lines.extend(
                GithubRepo._get_encoded_json_lines("Schema", current_schema.bundle())
            )

        # Add batch JSON
        encodable_batch: Dict[str, Any] = {
            "title": batch["title"],
            "items": [item.bundle() for item in batch["items"]],
        }
        if "metadata" in batch:
            encodable_batch["metadata"] = batch["metadata"]
        automation_info_lines.extend(GithubRepo._get_encoded_json_lines("batch", encodable_batch))

        return "\n".join(automation_info_lines)

    @staticmethod
    def _get_encoded_json_lines(title: str, encodable_object: Any) -> List[str]:
        """Gets the details section for an encoded json object as a list of lines.

        Args:
            title (str): The title of the section.
            encodable_object (Any): The object to json encode.

        Returns:
            List[str]: _description_
        """
        return [
            f"<details><summary>{title} JSON</summary>",
            "",
            "```",
            GithubUtils.BEGIN_BATCH,
            json.dumps(encodable_object, indent=4),
            GithubUtils.END_BATCH,
            "```",
            "",
            "</details>",
        ]

    def get_outstanding_changes(self) -> Sequence[GithubChange]:
        """Gets all outstanding pull requests for the Repo.

        Returns:
            Sequence[GithubChange]: The outstanding Changes against the Repo.
        """

        pulls = GithubUtils.get(self._params["full_github_name"]).get_open_pull_requests(
            self._params["base_branch_name"]
        )
        authenticated_user_id = GithubUtils.get(self._params["full_github_name"]).get_user_id()
        return [
            GithubChange(
                {
                    "full_github_name": self._params["full_github_name"],
                    "pull_number": pull.number,
                }
            )
            for pull in pulls
            if pull.owner_id == authenticated_user_id
        ]

    @staticmethod
    def from_data(data: Mapping[str, Any]) -> GithubRepo:
        """Produces a GithubRepo from the provided data.

        Args:
            data (Mapping[str, Any]): The JSON decoded params from an encoded bundle

        Returns:
            GithubRepo: An instance of the GithubRepo
        """

        base_branch_name = data["base_branch_name"]
        assert isinstance(base_branch_name, str)
        full_github_name = data["full_github_name"]
        assert isinstance(full_github_name, str)
        params: GithubRepoParams = {
            "base_branch_name": base_branch_name,
            "full_github_name": full_github_name,
        }

        required_labels = data.get("required_labels")
        if required_labels is not None:
            assert isinstance(required_labels, List)
            params["required_labels"] = required_labels

        hide_automation_info = data.get("hide_automation_info")
        if hide_automation_info is not None:
            assert isinstance(hide_automation_info, bool)
            params["hide_automation_info"] = hide_automation_info

        hide_autotransform_docs = data.get("hide_autotransform_docs")
        if hide_autotransform_docs is not None:
            assert isinstance(hide_autotransform_docs, bool)
            params["hide_autotransform_docs"] = hide_autotransform_docs

        return GithubRepo(params)
