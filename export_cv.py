#!/usr/bin/env python3
"""Exporte un CV Markdown (voir templates/) en PDF texte, une seule colonne,
police standard — sans tableau, image ou colonne, pour rester 100% lisible
par un logiciel de tri de CV (ATS).

Usage :
    python3 export_cv.py templates/cv-template-fr.md mon-cv.pdf
"""

import sys

from fpdf import FPDF

MARGIN_MM = 18

# La police standard (Helvetica) ne supporte que le Latin-1 : on normalise
# la ponctuation "intelligente" vers de l'ASCII simple plutôt que de planter
# ou d'embarquer une police Unicode (qui compliquerait la compatibilité ATS).
_CHAR_MAP = {
    "—": "-",  # em dash —
    "–": "-",  # en dash –
    "‘": "'", "’": "'",  # guillemets simples courbes
    "“": '"', "”": '"',  # guillemets doubles courbes
    "…": "...",  # ellipse
}


def _sanitize(text: str) -> str:
    for bad, good in _CHAR_MAP.items():
        text = text.replace(bad, good)
    return text.encode("latin-1", "replace").decode("latin-1")


class CVPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


def export(markdown_path: str, output_path: str):
    with open(markdown_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    pdf = CVPDF(format="A4")
    pdf.set_margins(MARGIN_MM, MARGIN_MM, MARGIN_MM)
    pdf.set_auto_page_break(auto=True, margin=MARGIN_MM)
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)

    contact_line_pending = False

    for raw_line in lines:
        line = _sanitize(raw_line.strip())

        if not line:
            pdf.ln(2)
            continue

        pdf.set_x(pdf.l_margin)

        if line.startswith("# "):
            pdf.set_font("Helvetica", "B", 18)
            pdf.multi_cell(pdf.epw, 9, line[2:].strip(), new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=11)
            contact_line_pending = True
            continue

        if line.startswith("## "):
            pdf.ln(3)
            pdf.set_x(pdf.l_margin)
            pdf.set_font("Helvetica", "B", 13)
            pdf.multi_cell(pdf.epw, 8, line[3:].strip().upper(), new_x="LMARGIN", new_y="NEXT")
            pdf.set_draw_color(0, 0, 0)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - MARGIN_MM, pdf.get_y())
            pdf.ln(2)
            pdf.set_font("Helvetica", size=11)
            continue

        if line.startswith("### "):
            pdf.ln(1)
            pdf.set_x(pdf.l_margin)
            pdf.set_font("Helvetica", "B", 11.5)
            pdf.multi_cell(pdf.epw, 6, line[4:].strip(), new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=11)
            continue

        if line.startswith("- "):
            indent = 4
            pdf.set_x(pdf.l_margin + indent)
            pdf.multi_cell(pdf.epw - indent, 6, f"- {line[2:].strip()}", new_x="LMARGIN", new_y="NEXT")
            continue

        # Ligne de contact juste après le nom, ou texte courant.
        if contact_line_pending:
            pdf.set_font("Helvetica", size=10)
            pdf.multi_cell(pdf.epw, 6, line, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=11)
            contact_line_pending = False
        else:
            pdf.multi_cell(pdf.epw, 6, line, new_x="LMARGIN", new_y="NEXT")

    pdf.output(output_path)
    print(f"PDF généré : {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python3 export_cv.py <fichier.md> <sortie.pdf>")
        sys.exit(1)
    export(sys.argv[1], sys.argv[2])
