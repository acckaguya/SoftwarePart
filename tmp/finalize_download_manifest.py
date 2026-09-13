from __future__ import annotations

import hashlib
import json
import urllib.parse
from pathlib import Path


ROOT = Path.cwd() / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF"
JSON_PATH = ROOT / "下载结果.json"

OVERRIDES = {
    "PyTorch2": (ROOT / "6.3" / "PyTorch2.pdf", "PyTorch official author copy", "https://docs.pytorch.org/assets/pytorch2-2.pdf"),
    "PCcheck": (ROOT / "6.4" / "PCcheck.pdf", "author-hosted published version", "https://michalfman.github.io/files/PCCheck.pdf"),
    "LowDiff": (ROOT / "6.4" / "LowDiff.pdf", "arXiv author manuscript", "https://arxiv.org/pdf/2509.04084"),
}


def clean_title(value: str) -> str:
    return value.replace("{", "").replace("}", "")


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    for item in data:
        item["resolved_title"] = clean_title(str(item.get("resolved_title") or item["title"]))
        if item["slug"] not in OVERRIDES:
            continue
        path, source, url = OVERRIDES[item["slug"]]
        raw = path.read_bytes()
        if not raw.startswith(b"%PDF"):
            raise RuntimeError(f"Not a PDF: {path}")
        item.update(
            status="downloaded",
            pdf_source=source,
            pdf_url=url,
            bytes=len(raw),
            sha256=hashlib.sha256(raw).hexdigest(),
            local_path=str(path.relative_to(ROOT.parent)).replace("\\", "/"),
            note="",
        )
    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 新增一级优先论文下载结果",
        "",
        "正式出处以章节映射中的会议、期刊或 DOI 为准；“PDF 来源”单独记录实际下载位置。`arXiv author manuscript` 表示正式论文的公开作者稿，不改变其正式发表状态。",
        "",
        "| 章节 | 论文 | 正式出处 | 下载状态 | PDF 来源 | 本地文件 |",
        "|---|---|---|---|---|---|",
    ]
    for item in data:
        title = clean_title(str(item.get("resolved_title") or item["title"])).replace("|", "\\|")
        local = str(item["local_path"]).split("新增PDF/", 1)[-1]
        target = urllib.parse.quote(local.replace("\\", "/"), safe="/.-_")
        lines.append(f"| {item['section']} | {title} | {item['venue']} | 已下载 | {item['pdf_source']} | [本地 PDF]({target}) |")
    downloaded = sum(1 for item in data if item["status"] == "downloaded")
    total_bytes = sum(int(item.get("bytes") or 0) for item in data)
    official = sum(1 for item in data if "official" in str(item.get("pdf_source", "")).lower() or "published version" in str(item.get("pdf_source", "")).lower())
    author = downloaded - official
    lines.extend([
        "",
        f"共下载 **{downloaded}/{len(data)}** 篇，PDF 合计 **{total_bytes / 1024 / 1024:.1f} MiB**。其中 **{official} 篇**来自会议、期刊、框架官方站或开放发表版本，**{author} 篇**为与正式论文对应的作者公开稿。",
        "",
        "每个文件的实际下载 URL、字节数和 SHA-256 校验值见[下载结果.json](%E4%B8%8B%E8%BD%BD%E7%BB%93%E6%9E%9C.json)。",
        "",
    ])
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

