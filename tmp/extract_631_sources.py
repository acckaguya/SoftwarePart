from pathlib import Path
import pdfplumber


root = Path.cwd()
sources = {
    "参考报告": root / "超大规模智算集群架构技术调研报告.pdf",
    "MixedPrecision": root / "文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/MixedPrecision.pdf",
    "ScalingFP8": root / "文献材料_顶会顶刊优先版_2026-09-11/新增PDF/6.3/ScalingFP8.pdf",
    "COAT": root / "文献材料_顶会顶刊优先版_2026-09-11/新增PDF/6.3/COAT.pdf",
    "GPTQ": root / "文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/GPTQ.pdf",
    "SmoothQuant": root / "文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/SmoothQuant.pdf",
    "AWQ": root / "文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/AWQ.pdf",
    "CaseFor4Bit": root / "文献材料_顶会顶刊优先版_2026-09-11/新增PDF/6.3/CaseFor4Bit.pdf",
    "QServe": root / "文献材料_顶会顶刊优先版_2026-09-11/新增PDF/6.3/QServe.pdf",
}

out_dir = root / "tmp/pdfs/extracted"
out_dir.mkdir(parents=True, exist_ok=True)

for name, path in sources.items():
    target = out_dir / f"{name}.txt"
    if target.exists() and target.stat().st_size > 0:
        print(f"{name}: already extracted")
        continue
    chunks = []
    with pdfplumber.open(path) as pdf:
        for number, page in enumerate(pdf.pages, 1):
            text = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
            chunks.append(f"\n===== PAGE {number} =====\n{text}\n")
    target.write_text("".join(chunks), encoding="utf-8")
    print(f"{name}: {len(chunks)} pages, {target.stat().st_size} bytes")
