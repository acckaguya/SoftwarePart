from __future__ import annotations

import difflib
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path.cwd() / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) literature-curation/1.0"
TIMEOUT = 45


PAPERS = [
    # 6.3
    {"section": "6.3", "slug": "ScalingFP8", "title": "Scaling FP8 training to trillion-token LLMs", "venue": "ICLR 2025", "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html"},
    {"section": "6.3", "slug": "COAT", "title": "COAT: Compressing Optimizer States and Activations for Memory-Efficient FP8 Training", "venue": "ICLR 2025", "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ac807c9b296964409b277369e55621a-Abstract-Conference.html"},
    {"section": "6.3", "slug": "CaseFor4Bit", "title": "The case for 4-bit precision: k-bit Inference Scaling Laws", "venue": "ICML 2023", "url": "https://proceedings.mlr.press/v202/dettmers23a.html"},
    {"section": "6.3", "slug": "QServe", "title": "QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving", "venue": "MLSys 2025", "url": "https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html"},
    {"section": "6.3", "slug": "Apollo", "title": "Apollo: Automatic Partition-based Operator Fusion through Layer by Layer Optimization", "venue": "MLSys 2022", "url": "https://proceedings.mlsys.org/paper_files/paper/2022/hash/e175e8a86d28d935be4f43719651f86d-Abstract.html"},
    {"section": "6.3", "slug": "Welder", "title": "Welder: Scheduling Deep Learning Memory Access via Tile-graph", "venue": "OSDI 2023", "url": "https://www.usenix.org/conference/osdi23/presentation/shi"},
    {"section": "6.3", "slug": "PyTorch2", "title": "PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation", "venue": "ASPLOS 2024", "url": "https://doi.org/10.1145/3620665.3640366"},
    {"section": "6.3", "slug": "FlashInfer", "title": "FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving", "venue": "MLSys 2025", "url": "https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html"},
    {"section": "6.3", "slug": "Mooncake", "title": "Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot", "venue": "FAST 2025", "url": "https://www.usenix.org/conference/fast25/presentation/qin"},
    {"section": "6.3", "slug": "PromptCache", "title": "Prompt Cache: Modular Attention Reuse for Low-Latency Inference", "venue": "MLSys 2024", "url": "https://proceedings.mlsys.org/paper_files/paper/2024/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html"},
    {"section": "6.3", "slug": "IMPRESS", "title": "IMPRESS: An Importance-Informed Multi-Tier Prefix KV Storage System for Large Language Model Inference", "venue": "FAST 2025", "url": "https://www.usenix.org/conference/fast25/presentation/chen-weijian-impress"},
    {"section": "6.3", "slug": "UniPC", "title": "UniPC: A Unified Predictor-Corrector Framework for Fast Sampling of Diffusion Models", "venue": "NeurIPS 2023", "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/9c2aa1e456ea543997f6927295196381-Abstract-Conference.html"},
    {"section": "6.3", "slug": "ImprovedLCM", "title": "Improved Training Technique for Latent Consistency Models", "venue": "ICLR 2025", "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/9541101fbc2f24bce5f2462b95db88c4-Abstract-Conference.html"},
    {"section": "6.3", "slug": "LearningToCache", "title": "Learning-to-Cache: Accelerating Diffusion Transformer via Layer Caching", "venue": "NeurIPS 2024", "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/f0b1515be276f6ba82b4f2b25e50bef0-Abstract-Conference.html"},
    {"section": "6.3", "slug": "PipeFusion", "title": "PipeFusion: Patch-level Pipeline Parallelism for Diffusion Transformers Inference", "venue": "NeurIPS 2025", "url": "https://proceedings.nips.cc/paper_files/paper/2025/hash/8da04a60948be713dc766f0c7e3a5b1f-Abstract-Conference.html"},
    {"section": "6.3", "slug": "NeuralOperator", "title": "Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs", "venue": "JMLR 2023", "url": "https://www.jmlr.org/beta/papers/v24/21-1524.html"},
    # 6.4
    {"section": "6.4", "slug": "ByteRobust", "title": "Robust LLM Training Infrastructure at ByteDance", "venue": "SOSP 2025", "url": "https://doi.org/10.1145/3731569.3764838"},
    {"section": "6.4", "slug": "GREYHOUND", "title": "GREYHOUND: Hunting Fail-Slows in Hybrid-Parallel Training at Scale", "venue": "USENIX ATC 2025", "url": "https://www.usenix.org/conference/atc25/presentation/wu-tianyuan"},
    {"section": "6.4", "slug": "Mycroft", "title": "Mycroft", "venue": "SOSP 2025", "url": "https://doi.org/10.1145/3731569.3764848"},
    {"section": "6.4", "slug": "WhatIfStragglers", "title": "Understanding Stragglers in Large Model Training Using What-if Analysis", "venue": "OSDI 2025", "url": "https://www.usenix.org/conference/osdi25/presentation/lin-jinkun"},
    {"section": "6.4", "slug": "EROICA", "title": "EROICA: Online Performance Troubleshooting for Large-scale Model Training", "venue": "NSDI 2026", "url": "https://www.usenix.org/conference/nsdi26/presentation/guan-yu"},
    {"section": "6.4", "slug": "PCcheck", "title": "PCcheck", "venue": "ASPLOS 2025", "url": "https://doi.org/10.1145/3669940.3707255"},
    {"section": "6.4", "slug": "DataStatesLLM", "title": "DataStates-LLM", "venue": "HPDC 2024", "url": "https://doi.org/10.1145/3625549.3658685"},
    {"section": "6.4", "slug": "LowDiff", "title": "LowDiff", "venue": "SC 2025", "url": "https://doi.org/10.1145/3712285.3759891"},
    {"section": "6.4", "slug": "UniversalCheckpointing", "title": "Universal Checkpointing", "venue": "USENIX ATC 2025", "url": "https://www.usenix.org/conference/atc25/presentation/lian"},
    {"section": "6.4", "slug": "SpotServe", "title": "SpotServe", "venue": "ASPLOS 2024", "url": "https://doi.org/10.1145/3620665.3640411"},
    {"section": "6.4", "slug": "BlitzScale", "title": "BlitzScale", "venue": "OSDI 2025", "url": "https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan"},
    {"section": "6.4", "slug": "AdaServe", "title": "AdaServe", "venue": "EuroSys 2026", "url": "https://doi.org/10.1145/3767295.3769315"},
    {"section": "6.4", "slug": "ServeGen", "title": "ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production", "venue": "NSDI 2026", "url": "https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen"},
]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k.lower(): v for k, v in attrs if v is not None}
        if tag.lower() == "a" and data.get("href"):
            self.links.append(html.unescape(data["href"]))
        if tag.lower() == "meta":
            key = (data.get("name") or data.get("property") or "").lower()
            if key and data.get("content"):
                self.meta[key] = html.unescape(data["content"])


def request_bytes(url: str, timeout: int = TIMEOUT) -> tuple[bytes, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,text/html,application/xhtml+xml,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read(), response.geturl(), response.headers.get("Content-Type", "")


def normalize_title(value: str) -> str:
    value = html.unescape(value).lower().replace("–", "-").replace("—", "-")
    return " ".join(re.findall(r"[a-z0-9]+", value))


def title_similarity(a: str, b: str) -> float:
    na, nb = normalize_title(a), normalize_title(b)
    if not na or not nb:
        return 0.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def crossref_metadata(landing_url: str) -> tuple[str | None, list[str]]:
    marker = "doi.org/"
    if marker not in landing_url:
        return None, []
    doi = landing_url.split(marker, 1)[1]
    api = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    try:
        raw, _, _ = request_bytes(api)
        message = json.loads(raw.decode("utf-8"))["message"]
        title = (message.get("title") or [None])[0]
        links = [x.get("URL") for x in message.get("link", []) if x.get("URL") and "pdf" in (x.get("content-type") or "").lower()]
        return title, links
    except Exception:
        return None, []


def landing_candidates(url: str) -> tuple[str | None, list[str]]:
    raw, final_url, content_type = request_bytes(url)
    if raw.startswith(b"%PDF") or "application/pdf" in content_type.lower():
        return None, [final_url]
    text = raw.decode("utf-8", errors="replace")
    parser = LinkParser()
    parser.feed(text)
    title = parser.meta.get("citation_title") or parser.meta.get("dc.title") or parser.meta.get("og:title")
    links: list[str] = []
    for key in ("citation_pdf_url", "eprints.document_url", "dc.identifier"):
        value = parser.meta.get(key)
        if value and ".pdf" in value.lower():
            links.append(urllib.parse.urljoin(final_url, value))
    for link in parser.links:
        low = link.lower()
        if ".pdf" in low or "/paper_files/paper/" in low and "paper" in low:
            links.append(urllib.parse.urljoin(final_url, link))

    def score(link: str) -> tuple[int, int]:
        low = link.lower()
        bad = any(word in low for word in ("slides", "presentation", "poster", "supp", "appendix", "artifact"))
        good = any(word in low for word in ("paper", "system/files", "content/cvpr", "proceedings", "download"))
        return (0 if bad else 2, 1 if good else 0)

    return title, sorted(dict.fromkeys(links), key=score, reverse=True)


def arxiv_candidate(title: str) -> tuple[str | None, str | None, float]:
    if len(normalize_title(title).split()) < 3:
        return None, None, 0.0
    query = urllib.parse.quote(f'ti:"{title}"')
    url = f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=5"
    try:
        raw, _, _ = request_bytes(url)
        root = ET.fromstring(raw)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        best: tuple[str | None, str | None, float] = (None, None, 0.0)
        for entry in root.findall("a:entry", ns):
            found_title = " ".join((entry.findtext("a:title", default="", namespaces=ns)).split())
            similarity = title_similarity(title, found_title)
            pdf = None
            for link in entry.findall("a:link", ns):
                if link.attrib.get("type") == "application/pdf" or link.attrib.get("title") == "pdf":
                    pdf = link.attrib.get("href")
                    break
            if pdf and similarity > best[2]:
                best = (pdf, found_title, similarity)
        return best
    except Exception:
        return None, None, 0.0


def try_pdf(url: str) -> tuple[bytes | None, str | None, str | None]:
    try:
        raw, final_url, content_type = request_bytes(url)
        if raw.startswith(b"%PDF"):
            return raw, final_url, content_type
    except Exception:
        pass
    return None, None, None


def download_one(paper: dict[str, str]) -> dict[str, object]:
    result: dict[str, object] = dict(paper)
    result.update({"status": "failed", "pdf_source": None, "pdf_url": None, "bytes": 0, "sha256": None, "note": ""})
    title = paper["title"]
    candidates: list[tuple[str, str]] = []

    crossref_title, crossref_links = crossref_metadata(paper["url"])
    if crossref_title:
        title = crossref_title
        result["resolved_title"] = crossref_title
    candidates.extend((link, "publisher/Crossref") for link in crossref_links)

    try:
        landing_title, links = landing_candidates(paper["url"])
        if landing_title and title_similarity(title, landing_title) > 0.35:
            title = landing_title
            result["resolved_title"] = landing_title
        candidates.extend((link, "official landing page") for link in links)
    except Exception as exc:
        result["note"] = f"landing page error: {type(exc).__name__}"

    seen: set[str] = set()
    for candidate, label in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        raw, final_url, _ = try_pdf(candidate)
        if raw is not None:
            folder = ROOT / paper["section"]
            folder.mkdir(parents=True, exist_ok=True)
            path = folder / f"{paper['slug']}.pdf"
            path.write_bytes(raw)
            result.update({"status": "downloaded", "pdf_source": label, "pdf_url": final_url, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "local_path": str(path.relative_to(ROOT.parent)).replace("\\", "/")})
            return result

    arxiv_url, arxiv_title, similarity = arxiv_candidate(title)
    if arxiv_url and similarity >= 0.70:
        raw, final_url, _ = try_pdf(arxiv_url)
        if raw is not None:
            folder = ROOT / paper["section"]
            folder.mkdir(parents=True, exist_ok=True)
            path = folder / f"{paper['slug']}.pdf"
            path.write_bytes(raw)
            result.update({"status": "downloaded", "pdf_source": "arXiv author manuscript", "pdf_url": final_url, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "local_path": str(path.relative_to(ROOT.parent)).replace("\\", "/"), "arxiv_title": arxiv_title, "title_similarity": round(similarity, 3)})
            return result

    result["note"] = (str(result.get("note") or "") + f"; no accessible PDF; resolved title={title!r}").strip("; ")
    return result


def write_manifest(results: list[dict[str, object]]) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "下载结果.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 新增一级优先论文下载结果",
        "",
        "正式出处以章节映射中的会议、期刊或 DOI 为准；“PDF 来源”单独记录实际下载位置。arXiv author manuscript 表示正式论文的公开作者稿，不改变其正式发表状态。",
        "",
        "| 章节 | 论文 | 正式出处 | 下载状态 | PDF 来源 | 本地文件或官方页 |",
        "|---|---|---|---|---|---|",
    ]
    for item in results:
        title = str(item.get("resolved_title") or item["title"]).replace("|", "\\|")
        if item["status"] == "downloaded":
            local = str(item["local_path"]).split("新增PDF/", 1)[-1]
            target = urllib.parse.quote(local.replace("\\", "/"), safe="/.-_")
            link = f"[本地 PDF]({target})"
            status = "已下载"
        else:
            link = f"[官方页]({item['url']})"
            status = "仅索引"
        lines.append(f"| {item['section']} | {title} | {item['venue']} | {status} | {item.get('pdf_source') or '—'} | {link} |")
    downloaded = sum(1 for item in results if item["status"] == "downloaded")
    total_bytes = sum(int(item.get("bytes") or 0) for item in results)
    lines.extend(["", f"共下载 **{downloaded}/{len(results)}** 篇，PDF 合计 **{total_bytes / 1024 / 1024:.1f} MiB**。未自动取得的条目保留正式来源页，便于通过机构访问或作者主页补充。", ""])
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, object]] = []
    for index, paper in enumerate(PAPERS, 1):
        print(f"[{index:02d}/{len(PAPERS)}] {paper['slug']}", flush=True)
        result = download_one(paper)
        results.append(result)
        print(f"  {result['status']} {result.get('bytes', 0)} {result.get('pdf_source') or ''}", flush=True)
        write_manifest(results)
        time.sleep(0.35)
    write_manifest(results)


if __name__ == "__main__":
    main()

