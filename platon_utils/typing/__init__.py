import warnings

from .misc import (  # noqa: F401
    Address,
    AnyAddress,
    ChecksumAddress,
    HexAddress,
    HexStr,
    Primitives,
    T,
)

warnings.warn(
    "The platon_utils.typing module will be deprecated in favor "
    "of platon-typing in the next major version bump.",
    category=DeprecationWarning,
    stacklevel=2,
)
