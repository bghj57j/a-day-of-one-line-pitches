# Writes the one pitch sentence to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "You don't need to know how to code — just describe the app you wish existed, and an AI agent builds a real one you can tap and use while you tell it what to fix."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
