import datetime
from typing import Mapping, List, Tuple, Union, Iterable, Dict, Any, overload

from git import Repo, Commit
from typing_extensions import Literal

from we_are_venom.common_types import Ticket, CommitInfo


@overload
def fetch_git_history(
    path: str,
    get_extended_commits_info: Literal[True],
    date_from: datetime.datetime = None,
    modules: Iterable[str] = None,
    date_to: datetime.datetime = None,
) -> List[CommitInfo]:
    pass


@overload
def fetch_git_history(
    path: str,
    get_extended_commits_info: Literal[False] = False,
    date_from: datetime.datetime = None,
    modules: Iterable[str] = None,
    date_to: datetime.datetime = None,
) -> List[Commit]:
    pass


def fetch_git_history(
    path: str,
    get_extended_commits_info: bool = False,
    date_from: datetime.datetime = None,
    modules: Iterable[str] = None,
    date_to: datetime.datetime = None,
) -> List[Union[Commit, CommitInfo]]:
    repo = Repo(path)
    date_to = date_to or datetime.datetime.now()
    modules = modules or []
    iter_commits_args: Dict[str, Any] = {'no_merges': True}
    if date_from:
        iter_commits_args['since'] = date_from
    if date_to:
        iter_commits_args['until'] = date_to
    raw_commits = list(repo.iter_commits(**iter_commits_args))
    if not get_extended_commits_info:
        return raw_commits
    return [fetch_full_commit_data(c, modules) for c in raw_commits]


def fetch_full_commit_data(raw_commit: Commit, modules: Iterable[str]) -> CommitInfo:
    pass


def aggregate_commits_by_tickets(
    commits: List[CommitInfo],
    commit_regexp: str,
) -> Tuple[List[Ticket], List[CommitInfo]]:
    pass


def cherry_pick_tickets(tickets: List[Ticket]) -> Mapping[str, Mapping[str, str]]:
    pass
