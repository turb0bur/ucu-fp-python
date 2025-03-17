from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    def fibonacci(n: int) -> int:
        if n < 0:
            return (-1) ** (abs(n) + 1) * fibonacci(abs(n))
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        @tail_call_optimized
        def tail_rec(i: int, last: int, next_to_last: int) -> int:
            if i >= n:
                return last
            return tail_rec(i + 1, last + next_to_last, last)

        return tail_rec(2, 1, 1)

    return fibonacci
