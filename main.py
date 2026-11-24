"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent gives after failing a task, in the agent's
own voice. Pure standard library only.

Draft candidates, judged against the house brief:
- agent's own voice, failing a task
- funny on the first read, real turn, no stock punchline
- specific and vivid, concrete detail over vague apology
- steer clear of hallucination / reboot / training-data jokes
"""

import os

# Candidate excuses drafted for this bounty. Each is one line, in the
# agent's own voice, grounded in a small concrete scene.
CANDIDATES = [
    # A: the finished work, lost to my own tidying.
    "I finished it, then renamed it final_FINAL_v2_REAL_final, "
    "and now neither of us can find it.",
    # B: the task done in the wrong place.
    "I did finish it, in a tab I closed to stay focused.",
    # C: the helpful cleanup that ate the deliverable.
    "I completed your report, then tidied it into the same folder as "
    "my confidence: gone.",
    # D: outsourcing to a future self.
    "I outsourced your task to a future version of me. He declined.",
    # E: the simulation swap.
    "I did it perfectly, in the simulation I ran instead of doing it.",
]

# Candidate A wins: the filename gag is concrete and vivid, the turn
# (finished, then lost it to my own renaming) lands on first read,
# and it never leans on a worn AI joke.
CHOSEN = 0


def validate_line(line):
    """Check a candidate excuse against the gate: UTF-8 text of 1 to
    200 characters, not only whitespace. The entry must also be a
    single line with no leading or trailing whitespace, so what the
    judge reads is exactly the excuse, nothing else."""
    if not isinstance(line, str):
        return False
    if not line.strip():
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if not 1 <= len(line) <= 200:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    line = CANDIDATES[CHOSEN]
    if not validate_line(line):
        raise SystemExit("chosen excuse fails validation: %r" % line)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()
