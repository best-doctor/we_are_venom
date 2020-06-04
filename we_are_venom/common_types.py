from typing import NamedTuple, Optional


class ModuleAccumulation(NamedTuple):
    module_name: str
    touched_lines: int
    total_lines: Optional[int]
    is_accumulated: Optional[bool]


class Ticket(NamedTuple):
    added_lines: int
    deleted_lines: int

    @property
    def touched_lines(self) -> int:
        return self.added_lines + self.touched_lines


class CommitInfo(NamedTuple):
    pass
