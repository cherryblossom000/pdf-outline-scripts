# pdf-outline-scripts

Just some stuff I use to add a table of contents/outlines to some PDFs.

`lib.private` doesn’t implement any new logic for adding the outlines.
All `add_maths_textbook_outlines` does is call `add_maths_textbook_outlines`
from `lib.maths_textbook` but with `input`, `output`, and `answers_output`
specific to my setup.
