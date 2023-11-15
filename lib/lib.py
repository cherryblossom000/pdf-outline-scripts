from dataclasses import dataclass, field
from pathlib import Path
from typing import (
	Callable,
	Iterable,
	List,
	Tuple,
	Union,
)
from . import pikepdf
from .pikepdf import OutlineItem, Pdf


@dataclass
class WithPage:
	page: int
	"""1-indexed so you can use the page numbers directly from a PDF viewer"""


@dataclass
class OutlineNode(WithPage):
	label: str
	children: List["OutlineNode"] = field(default_factory=list)

	def map(self, fn: Callable[[int, str], Tuple[int, str]]) -> "OutlineNode":
		page, label = fn(self.page, self.label)
		return OutlineNode(page, label, list(n.map(fn) for n in self.children))


def _to_outline(node: OutlineNode) -> OutlineItem:
	outline = OutlineItem(node.label, node.page - 1)
	outline.children.extend(map(_to_outline, node.children))
	return outline


def add_outlines(
	input: Union[Path, Pdf],
	output: Path,
	outlines: Iterable[OutlineNode],
	description: str = "PDF",
):
	print(f"Writing {description} to {output}")

	def add(pdf: Pdf):
		with pdf.open_outline() as outline:
			outline.root.clear()
			outline.root.extend(map(_to_outline, outlines))
		pdf.save(output, compress_streams=True)

	if isinstance(input, Pdf):
		add(input)
	else:
		with pikepdf.open(input) as pdf:
			add(pdf)
