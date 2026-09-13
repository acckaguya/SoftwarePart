from pathlib import Path

import pdfplumber


ROOT = Path(r"D:\FILE\研究生\研1\课题组\智算集群报告")
OUT = ROOT / "tmp" / "pdfs" / "631_evidence"
PDFS = {
    "MixedPrecision": ROOT / "文献材料_第三四点_2026-09-09" / "3a_低精度_算子_编译优化" / "MixedPrecision.pdf",
    "ScalingFP8": ROOT / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF" / "6.3" / "ScalingFP8.pdf",
    "COAT": ROOT / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF" / "6.3" / "COAT.pdf",
    "GPTQ": ROOT / "文献材料_第三四点_2026-09-09" / "3a_低精度_算子_编译优化" / "GPTQ.pdf",
    "SmoothQuant": ROOT / "文献材料_第三四点_2026-09-09" / "3a_低精度_算子_编译优化" / "SmoothQuant.pdf",
    "AWQ": ROOT / "文献材料_第三四点_2026-09-09" / "3a_低精度_算子_编译优化" / "AWQ.pdf",
    "CaseFor4Bit": ROOT / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF" / "6.3" / "CaseFor4Bit.pdf",
    "QServe": ROOT / "文献材料_顶会顶刊优先版_2026-09-11" / "新增PDF" / "6.3" / "QServe.pdf",
}

for stem, path in PDFS.items():
    if not path.exists():
        raise FileNotFoundError(path)
    destination = OUT / f"{stem}.txt"
    if destination.exists():
        print(f"{stem}\tSKIP\t{destination}")
        continue
    chunks = []
    with pdfplumber.open(path) as pdf:
        for number, page in enumerate(pdf.pages, 1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3, layout=True) or ""
            chunks.append(f"\n===== PDF_PAGE {number} =====\n{text}\n")
        count = len(pdf.pages)
    destination.write_text("".join(chunks), encoding="utf-8")
    print(f"{stem}\t{count}\t{destination}")
