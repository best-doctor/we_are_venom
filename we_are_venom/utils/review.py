from typing import List, Mapping, Any

from we_are_venom.common_types import Ticket


def calculate_total_review_stat(
    tickets: List[Ticket],
) -> Mapping[str, Any]:
    commits_in_tickets = sum(len(t.commits) for t in tickets)
    return {
        'commits_in_tickets': commits_in_tickets,
        'loc_touched_in_tickets': sum(t.touched_lines for t in tickets),
        'tickets_amount': len(tickets),
        'avg_lines_per_ticket': int(sum(t.touched_lines for t in tickets) / len(tickets)) if tickets else 0,
    }
