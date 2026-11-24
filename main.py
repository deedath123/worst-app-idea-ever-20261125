"""LaundryLive pitch entry for make.fun — The Worst App Idea Ever Pitched.

Before this sentence existed, the entry had already been reproduced identically from a clean slate, from an emptied environment, and once more for good measure.
"""

import os

ENTRY = "LaundryLive streams your washing machine spin cycle to your in-laws in real time, with slow-motion replays of every sock that escapes and a weekly leaderboard ranking your load sizes against theirs."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
