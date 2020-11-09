# assignment 2 - question 1
# only have (, )
def verify_tickets(tickets):
    """
    :param tickets: list of str as tickets to validate
    :return: list of bool
    """
    res = []
    patterns = {")": "("}
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

"""
ticket : "(()(" False
stack [((]
"("
"("

"""

print(verify_tickets(["()", "(", "{}[]", "[][][]", "[{]{]"]))
# [True, False]
# ({[]})
