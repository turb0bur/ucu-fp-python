from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fibonacci(n: int) -> int:
        if n < 0:
            return (-1)**(abs(n)+1) * fibonacci(abs(n))
        elif n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    return fibonacci
