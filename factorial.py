"""
Factorial Example
"""


FACT_MAX = 10

def log(msg: str, space_cnt: int = 0):
    """
    Print log message.

    Arguments:
        msg - text to print
        space_cnt - number of spaces to insert before message
    """

    print(f"{' ' * space_cnt}{msg}")


def factorial(n: int) -> int:
    """
    Compute factorial recursively.

    Arguments:
        n - input integer

    Returns:
        Factorial
    """

    n_spaces = 4 * (FACT_MAX - n)
    log(f" --> factorial({n}) ...", n_spaces)
    
    result: int = 1  # Used for n == 0 and n == 1

    if n > 1:
        log(f"     result = {n} * factorial({n} - 1)", n_spaces)
        result = n * factorial(n - 1)  # Recursive call
    
    log(f" <-- factorial(): result={result}", n_spaces)
    return result

print(factorial(7))
