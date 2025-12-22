from typing import Generic, TypeVar, Sequence, Optional

T = TypeVar("T")

class Page(Generic[T]):
    def __init__(
        self,
        items: Sequence[T],
        next_page_token: Optional[str] = None,
    ):
        self.__items = list(items)
        self.__next_page_token = next_page_token

    @property
    def items(self) -> list[T]:
        return self.__items

    @property
    def next_page_token(self) -> Optional[str]:
        return self.__next_page_token

    @property
    def has_next_page(self) -> bool:
        return self.__next_page_token is not None
