def foo() -> int:
    return 1


## End of your code ##
from typing import assert_type

assert_type(foo(), int)
assert_type(foo(), str)  # expect-type-error