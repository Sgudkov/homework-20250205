from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)


def decorator(func: T) -> T:
    return func


## End of your code ##
@decorator
def foo(a: int, *, b: str) -> None:
    ...


@decorator
def bar(c: int, d: str) -> None:
    ...


foo(1, b="2")
bar(c=1, d="2")

foo(1, "2")  # expect-type-error
foo(a=1, e="2")  # expect-type-error
decorator(1)  # expect-type-error
