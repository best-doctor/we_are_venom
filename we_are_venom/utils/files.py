import glob
import os
import collections
from typing import Mapping, Any

from we_are_venom.utils.lists import flat


def fetch_modules_total_lines_map(path: str, config: Mapping[str, Any]) -> Mapping[str, int]:
    module_total_lines = collections.defaultdict(int)
    for module in config['modules']:
        wildcards = [
            os.path.join(path, module, '**', f'*.{e}')
            for e in config['extensions_to_check']
        ]
        filepathes = flat(glob.glob(w, recursive=True) for w in wildcards)
        for filepath in filepathes:
            with open(filepath) as file_handler:
                num_lines = sum(1 for _ in file_handler)
            module_total_lines[module] += num_lines
    return module_total_lines
