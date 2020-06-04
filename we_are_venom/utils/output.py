from typing import List, Mapping, Any, Optional

from git import Commit
from rich import print
from rich.console import Console
from rich.table import Table

from we_are_venom.common_types import ModuleAccumulation, Ticket
from we_are_venom.commit import CommitInfo
from we_are_venom.utils.lists import flat


def output_accumulation_table(module_accumulation_info: List[ModuleAccumulation]) -> None:
    is_accumulated_map = {
        None: '-',
        True: '✅',
        False: '❌',
    }
    console = Console()
    table = Table(show_header=True, header_style='bold magenta')
    table.add_column('Module', style='dim')
    table.add_column('Total lines')
    table.add_column('Touched lines')
    table.add_column('Accumulated')
    for module_info in module_accumulation_info:
        table.add_row(
            module_info.module_name,
            str(module_info.total_lines),
            str(module_info.touched_lines),
            is_accumulated_map[module_info.is_accumulated],
        )
    console.print(table)


def output_commits(commits: List[Commit]) -> None:
    console = Console()
    table = Table(show_header=True, header_style='bold magenta')
    table.add_column('Commit hash', style='dim')
    table.add_column('Summary')
    table.add_column('Commit datetime')
    for commit in commits:
        table.add_row(
            commit.hexsha,
            commit.summary,
            str(commit.committed_datetime),
        )
    console.print(table)
    print(f'[bold]Total {len(commits)} commits[/bold]')  # noqa: T001


def output_review_report(
    tickets: List[Ticket],
    small_tickets: List[Ticket],
    orphan_commits: List[CommitInfo],
    pretty_changesets_map: Optional[Mapping[str, Mapping[str, str]]],
    total_stat: Mapping[str, Any],
    web_base_repo_url: str,
) -> None:
    summary_max_width = 60
    missed_lines = sum(t.touched_lines for t in small_tickets) + sum(c.total_lines for c in orphan_commits)
    period_coverage = int(
        total_stat['loc_touched_in_tickets']
        / (total_stat['loc_touched_in_tickets'] + missed_lines)
        * 100,
    )
    for ticket in tickets:
        authors = ', '.join({c.commit.author.name for c in ticket.commits})
        touched_modules = sorted(set(flat(c.touched_modules_info.keys() for c in ticket.commits)))
        touched_modules_str = ', '.join(m.strip('/') for m in touched_modules)
        print(
            f'[bold red]{ticket.num}[/] [blue]{authors}[/] Touched modules: '
            f'[green]{touched_modules_str}[/], touched lines: {ticket.touched_lines}.',
        )
        for commit in ticket.commits:
            text = commit.commit.summary.split(': ')[-1]
            spaces = ''
            if len(text) < summary_max_width:
                spaces = ' ' * (summary_max_width - len(text))
            else:
                text = f'{text[:-(summary_max_width-3)]}...'
            url = f'{web_base_repo_url}{commit.commit.hexsha}'
            print(f'\t{text}{spaces}{url}')

    console = Console()
    table = Table(show_header=False, title='Summary', show_lines=True, padding=(0, 2))
    table.add_column('Name')
    table.add_column('Value')
    table.add_row('Total commits to review', str(total_stat['commits_in_tickets']))
    table.add_row('Total tickets to review', str(total_stat['tickets_amount']))
    table.add_row('Total lines to review', str(total_stat['loc_touched_in_tickets']))
    table.add_row('Average lines per ticket', str(total_stat['avg_lines_per_ticket']))
    table.add_row('Lines missed from the review', str(missed_lines))
    table.add_row('Period coverage', f'{period_coverage} %')
    console.print('\n\n\n', table)
