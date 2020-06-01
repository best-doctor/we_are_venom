from typing import List, Mapping, Any

from we_are_venom.common_types import Commit, ModuleAccumulation


def calclulate_module_accumulation_info(
    raw_git_history: List[Commit],
    email: str,
    config: Mapping[str, Any],
) -> List[ModuleAccumulation]:
    pass


def calculate_total_accumulation_percent(module_accumulation_info: List[ModuleAccumulation]) -> float:
    pass
