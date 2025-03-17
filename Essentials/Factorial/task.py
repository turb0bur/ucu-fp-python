from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def factorial(n: int, acc: int = 1) -> int:
        return acc if n <= 0 else factorial(n - 1, n * acc)

    return factorial
