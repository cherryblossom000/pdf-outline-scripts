# This file is mainly due to issues with types being Unknown/incorrect types
# TODO: remove some stuff when https://github.com/pikepdf/pikepdf/pull/265 is merged

from pathlib import Path
from types import TracebackType
from typing import (
    BinaryIO,
    Callable,
    Iterable,
    List,
    Optional,
    Protocol,
    Tuple,
    Type,
    TypeVar,
    Union,
)
from pikepdf.models.encryption import Encryption
from pikepdf.models.outlines import PageLocation
from pikepdf.objects import Array, Dictionary, Name, String
from pikepdf._qpdf import (
    AccessMode,
    ObjectStreamMode,
    Page,
    StreamDecodeLevel,
)

_T = TypeVar("_T", bound=BaseException)

class OutlineItem:
    # changed from Iterable[OutlineItem]
    children: List[OutlineItem]
    def __init__(
        self,
        title: str,
        # added int in the union
        destination: Optional[Union[int, Array, String, Name]] = ...,
        page_location: Optional[Union[PageLocation, str]] = ...,
        action: Optional[Dictionary] = ...,
        obj: Optional[Dictionary] = ...,
        *,
        left: Optional[float] = ...,
        top: Optional[float] = ...,
        right: Optional[float] = ...,
        bottom: Optional[float] = ...,
        zoom: Optional[float] = ...,
    ) -> None: ...

class Outline:
    def __enter__(self) -> Outline: ...
    def __exit__(
        self, exc_type: Type[_T], exc_value: _T, traceback: TracebackType
    ) -> None: ...
    # changed from Optional[List[OutlineItem]]
    @property
    def root(self) -> List[OutlineItem]: ...

class PageList:
    # changed from list
    def __getitem__(self, arg0: slice) -> List[Page]: ...
    def extend(self, iterable: Iterable[Page]) -> None: ...

class Pdf:
    def __enter__(self) -> Pdf: ...
    def __exit__(
        self, exc_type: Type[_T], exc_value: _T, traceback: TracebackType
    ) -> None: ...
    @property
    def pages(self) -> PageList: ...
    def open_outline(self, max_depth: int = ..., strict: bool = ...) -> Outline: ...
    def save(
        self,
        filename_or_stream: Union[Path, str, BinaryIO, None] = ...,
        *,
        static_id: bool = ...,
        preserve_pdfa: bool = ...,
        min_version: Union[str, Tuple[str, int]] = ...,
        force_version: Union[str, Tuple[str, int]] = ...,
        fix_metadata_version: bool = ...,
        compress_streams: bool = ...,
        stream_decode_level: Optional[StreamDecodeLevel] = ...,
        object_stream_mode: ObjectStreamMode = ...,
        normalize_content: bool = ...,
        linearize: bool = ...,
        qdf: bool = ...,
        progress: Callable[[int], None] = ...,
        encryption: Optional[Union[Encryption, bool]] = ...,
        recompress_flate: bool = ...,
    ) -> None: ...

New = Callable[[], Pdf]

class Open(Protocol):
    def __call__(
        self,
        filename_or_stream: Union[Path, str, BinaryIO],
        *,
        password: Union[str, bytes] = ...,
        hex_password: bool = ...,
        ignore_xref_streams: bool = ...,
        suppress_warnings: bool = ...,
        attempt_recovery: bool = ...,
        inherit_page_attributes: bool = ...,
        access_mode: AccessMode = ...,
        allow_overwriting_input: bool = ...,
    ) -> Pdf: ...
