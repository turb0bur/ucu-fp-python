from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    """
    Checks if the given increment function is pure.
    
    A pure function must:
    1. Not modify its input state (input object remains unchanged)
    2. Not rely on external state (no global variables, no side effects)
    3. Always return the same output for the same input (referential transparency)
    4. Correctly implement the increment operation (output.value = input.value + 1)

    Examples:
        Pure function:
            lambda i: Integer(i.value + 1)
        
        Impure functions:
            - Modifying input: lambda i: (i.value += 1, i)[1]
            - Using external state: lambda i: (global cache, cache)[1]

    Args:
        increment_fn: Function that takes an Integer and returns an Integer.
                     The function should increment the input value by 1.

    Returns:
        bool: True if the function is pure (follows all requirements),
              False otherwise.
    """
    initial = Integer(7)
    original_value = initial.value
    
    result1 = increment_fn(initial)
    result2 = increment_fn(initial)
    
    expected = Integer(original_value + 1)
    
    different_input = Integer(original_value + 2)
    different_result = increment_fn(different_input)
    
    return (initial.value == original_value and  # Input not modified
            result1.value == result2.value and   # Same input → same output
            result1.value == expected.value and  # Correct increment
            different_result.value == different_input.value + 1)  # Different input → different output
