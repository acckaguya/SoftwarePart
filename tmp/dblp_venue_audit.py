import json
import re
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(r"D:\FILE\研究生\研1\课题组\智算集群报告")
SOURCE = ROOT / "文献材料_第三四点_2026-09-09" / "文献元数据.json"
OUTPUT = ROOT / "tmp" / "dblp_venue_audit.json"


def normalize(value):
    value = re.sub(r"<[^>]+>", "", str(value or ""))
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def fetch(title):
    query = urllib.parse.quote(title)
    url = f"https://dblp.org/search/publ/api?q={query}&format=json&h=8"
    request = urllib.request.Request(url, headers={"User-Agent": "Codex literature venue audit/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    hits = payload.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    target = normalize(title)
    ranked = []
    for hit in hits:
        info = hit.get("info", {})
        candidate = normalize(info.get("title", ""))
        ranked.append((SequenceMatcher(None, target, candidate).ratio(), info))
    ranked.sort(key=lambda item: item[0], reverse=True)
    if not ranked:
        return {"query_url": url, "match_score": 0, "match": None}
    score, info = ranked[0]
    return {"query_url": url, "match_score": round(score, 4), "match": info}


records = json.loads(SOURCE.read_text(encoding="utf-8"))
results = []
for index, record in enumerate(records, start=1):
    try:
        result = fetch(record["title"])
        result["id"] = record["id"]
        result["group"] = record["group"]
        result["source_title"] = record["title"]
        results.append(result)
    except Exception as exc:
        results.append({
            "id": record["id"],
            "group": record["group"],
            "source_title": record["title"],
            "error": f"{type(exc).__name__}: {exc}",
        })
    if index < len(records):
        time.sleep(0.2)

OUTPUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {len(results)} records to {OUTPUT}")
