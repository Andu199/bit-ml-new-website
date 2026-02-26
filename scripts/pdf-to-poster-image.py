#!/usr/bin/env python3
"""Render first page of each PDF to PNG (for poster gallery). Saves alongside PDF."""
import fitz
from pathlib import Path

# Scale for ~150 DPI equivalent on letter-size; good for viewing
MATRIX = fitz.Matrix(2, 2)  # 2x zoom

def convert_pdf_to_png(pdf_path: Path, out_path: Path) -> bool:
    try:
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(matrix=MATRIX, alpha=False)
        pix.save(str(out_path))
        doc.close()
        return True
    except Exception as e:
        print(f"  skip {pdf_path.name}: {e}")
        return False

def main():
    base = Path(__file__).resolve().parent.parent
    for folder in ["posters-2022", "posters-2024", "posters-2025"]:
        dir_path = base / "content" / "community" / "deep-fmi" / folder
        if not dir_path.is_dir():
            continue
        for pdf in sorted(dir_path.glob("*.pdf")):
            png = pdf.with_suffix(".png")
            if png.exists() and png.stat().st_mtime >= pdf.stat().st_mtime:
                continue
            print(f"  {folder}/{pdf.name} -> {png.name}")
            convert_pdf_to_png(pdf, png)
    print("Done.")

if __name__ == "__main__":
    main()
