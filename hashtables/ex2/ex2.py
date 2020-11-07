#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # 1. Identify the origin
    # 2. Link each subsequent route
    route = [None] * length
    hashed_tickets = {}

    for ticket in tickets:
        hashed_tickets[ticket.source] = ticket.destination
    next = hashed_tickets["NONE"]

    for current in range(0, length):
        route[current] = next
        next = hashed_tickets[next]

    return route
