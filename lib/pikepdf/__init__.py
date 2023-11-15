from typing import TYPE_CHECKING, Type, cast
from pikepdf import new as _new, open as _open
from pikepdf.models.outlines import OutlineItem as _OutlineItem


if TYPE_CHECKING:
	from .types import New, Open, OutlineItem as _PatchedOutlineItem, Pdf as Pdf

	new = cast(New, _new)
	open = cast(Open, _open)
	OutlineItem = cast(Type[_PatchedOutlineItem], _OutlineItem)
else:
	from pikepdf import Pdf

	new = _new
	open = _open
	OutlineItem = _OutlineItem
