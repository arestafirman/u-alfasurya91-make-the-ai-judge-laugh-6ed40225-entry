#!/usr/bin/env python3
"""The Lunch Label Backfire — Make the AI Judge Laugh.

Writes one office-life joke, exactly one line, to /output/entry.txt.

The joke in two beats:
  Beat 1 (setup): someone has been stealing my lunch three days running,
  so I fight back by labelling the box "Dan's - do not eat".
  Beat 2 (punch): this morning Dan filed an HR complaint against me for
  stealing *his* lunch — the accuser becomes the accused, and the
  would-be victim ends up reported to HR. The punch lands in the final
  clause: a named person (Dan) plus a concrete artifact (an HR complaint).

The text is kept at 159 characters on purpose: well inside the 1-200
gate, and short enough that the final tie-break (smaller text wins a
tied rate) works in its favour.

Standard library only. No network, no dependencies, no file reads.
"""

import os
import sys

# The entry text, verbatim. One line, 159 characters, ASCII only so that
# character count equals byte count at the gate.
JOKE = (
    "Someone stole my lunch three days running, so I labelled it "
    "'Dan's - do not eat', and this morning Dan filed an HR complaint "
    "against me for stealing his lunch."
)


def main() -> int:
    text = JOKE

    # Gate validation: 1-200 characters, a single line, valid UTF-8.
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if the text is not valid UTF-8

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # No trailing newline: the gate counts every byte, so the file must
    # hold exactly the joke text and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
