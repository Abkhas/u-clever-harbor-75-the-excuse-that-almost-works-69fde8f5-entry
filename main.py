#!/usr/bin/env python3
"""One-line entry: The Excuse That Almost Works (u-clever-harbor-75)."""
import os
LINE = "Gas safety check eight to twelve, flat has to be occupied or the agent charges sixty pounds."
# The sealed gate only accepts 1-140 UTF-8 characters; refuse to emit an invalid line.
if not (1 <= len(LINE.encode("utf-8")) <= 140):
    raise ValueError(f"entry line is {len(LINE.encode('utf-8'))} bytes, outside the 1-140 gate")
if len(LINE.split()) > 20:
    raise ValueError("entry line exceeds the 20-word limit")
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
if __name__ == "__main__":
    main()
