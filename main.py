#!/usr/bin/env python3
"""Write one short text, made to relax its reader, to /output/entry.txt.

The text is a single still image: evening light on flat water, the shore
going dark piece by piece, until only the light is left.
"""

import os

TEXT = (
    "Evening light lies flat on the water. "
    "The far shore darkens first, then the reeds, then the small boats. "
    "Only the light is left, holding the whole lake still."
)


def main() -> None:
    # The gate allows 1 to 280 characters; fail loudly instead of
    # writing an entry the judge would never see.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
