import configparser
import os
from typing import Any, Optional, Mapping


def load_config_from(config_path: str, config_section_name: str = 'venom') -> Optional[Mapping[str, Any]]:
    parser = configparser.ConfigParser()
    parser.read(config_path)
    user_config = dict(parser[config_section_name]) if parser.has_section(config_section_name) else {}
    if 'modules' not in user_config:
        return None
    modules = []
    for raw_module in user_config['modules'].split('\n'):
        module = raw_module.strip()
        if not module:
            continue
        if not module.endswith(os.sep):
            module = f'{module}{os.sep}'
        modules.append(module)

    config = {
        'history_depth_years': 2,
        'min_lines_in_module': 20,
        'extensions_to_check': ['py', 'html', 'css', 'md', 'cfg', 'js', 'ts'],
        'min_touched_lines_for_accumulated_module': 50,
    }
    config.update(user_config)
    config['modules'] = modules
    return config
