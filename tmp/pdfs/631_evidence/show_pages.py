from pathlib import Path
import re
import sys


path = Path(sys.argv[1])
requested = {int(x) for x in sys.argv[2:]}
text = path.read_text(encoding="utf-8")
parts = re.split(r"\n===== PDF_PAGE (\d+) =====\n", text)
for i in range(1, len(parts), 2):
    page = int(parts[i])
    if page in requested:
        print(f"\n===== PDF_PAGE {page} =====\n{parts[i + 1]}")
