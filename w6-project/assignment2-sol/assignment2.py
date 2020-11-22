# assignment 2 - question 1
def verify_tickets(tickets):
    """
    :param tickets: list of str as tickets to validate
    :return: list of bool
    """
    res = []
    patterns = {")": "(", "]": "[", "}": "{"}
    for ticket in tickets:
        res.append(check_ticket(ticket, patterns))
    return res


def check_ticket(ticket, patterns):
    """
    :param ticket: str only contains '(', ')'
    :param patterns for comparison
    :return: bool
    """
    stack = []
    for c in ticket:
        if c in patterns:
            if len(stack) == 0:
                return False
            if stack.pop() != patterns[c]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


# assignment 2 - question 2
# orders = [[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
def slowest_broker(orders):
    if orders is None or len(orders) == 0:
        return -1

    brokers = [0 for i in range(20)]  # 20 brokers
    prev_time = 0
    for order in orders:
        brokers[order[0]] = max(order[1] - prev_time, brokers[order[0]])
        prev_time = order[1]
    (mx, idx) = max((v, idx) for idx, v in enumerate(brokers))
    return idx
