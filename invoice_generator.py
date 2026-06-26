"""
Invoice Generator (Python + PDF)
---------------------------------
Client data (JSON) se professional PDF invoice banata hai:
- Invoice number, date, company aur client details
- Line items (description, quantity, price)
- Subtotal, tax aur grand total automatic calculate
- Clean, branded PDF output

Usage:
    python invoice_generator.py sample_data/invoice_data.json
"""

import sys
import os
import json
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


# Brand colors
PRIMARY = colors.HexColor("#4F46E5")
DARK = colors.HexColor("#111827")
GRAY = colors.HexColor("#6B7280")
LIGHT = colors.HexColor("#F3F4F6")


def load_data(path):
    """JSON file se invoice data load karta hai."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_totals(items, tax_percent):
    """Subtotal, tax aur grand total calculate karta hai."""
    subtotal = sum(item["quantity"] * item["price"] for item in items)
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    return subtotal, tax, total


def generate_invoice(data, output_path):
    """Invoice ka PDF banata hai."""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # ---------- Header ----------
    c.setFillColor(PRIMARY)
    c.rect(0, height - 45 * mm, width, 45 * mm, fill=1, stroke=0)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(20 * mm, height - 25 * mm, "INVOICE")

    c.setFont("Helvetica", 11)
    c.drawString(20 * mm, height - 33 * mm, data["company"]["name"])
    c.drawString(20 * mm, height - 39 * mm, data["company"]["email"])

    # Invoice number aur date (right side)
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(width - 20 * mm, height - 25 * mm, f"#{data['invoice_number']}")
    c.setFont("Helvetica", 10)
    c.drawRightString(width - 20 * mm, height - 32 * mm, f"Date: {data['date']}")

    # ---------- Bill To ----------
    y = height - 60 * mm
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20 * mm, y, "BILL TO:")
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20 * mm, y - 7 * mm, data["client"]["name"])
    c.setFont("Helvetica", 10)
    c.setFillColor(GRAY)
    c.drawString(20 * mm, y - 13 * mm, data["client"]["email"])

    # ---------- Table header ----------
    table_top = y - 28 * mm
    c.setFillColor(PRIMARY)
    c.rect(20 * mm, table_top, width - 40 * mm, 9 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(23 * mm, table_top + 2.7 * mm, "Description")
    c.drawString(110 * mm, table_top + 2.7 * mm, "Qty")
    c.drawString(130 * mm, table_top + 2.7 * mm, "Price")
    c.drawRightString(width - 23 * mm, table_top + 2.7 * mm, "Amount")

    # ---------- Table rows ----------
    row_y = table_top - 9 * mm
    c.setFont("Helvetica", 10)
    for i, item in enumerate(data["items"]):
        if i % 2 == 0:
            c.setFillColor(LIGHT)
            c.rect(20 * mm, row_y - 2 * mm, width - 40 * mm, 9 * mm, fill=1, stroke=0)

        amount = item["quantity"] * item["price"]
        c.setFillColor(DARK)
        c.drawString(23 * mm, row_y + 0.5 * mm, str(item["description"]))
        c.drawString(110 * mm, row_y + 0.5 * mm, str(item["quantity"]))
        c.drawString(130 * mm, row_y + 0.5 * mm, f"${item['price']:.2f}")
        c.drawRightString(width - 23 * mm, row_y + 0.5 * mm, f"${amount:.2f}")
        row_y -= 9 * mm

    # ---------- Totals ----------
    subtotal, tax, total = calculate_totals(data["items"], data.get("tax_percent", 0))
    totals_y = row_y - 6 * mm

    c.setFont("Helvetica", 10)
    c.setFillColor(GRAY)
    c.drawRightString(width - 50 * mm, totals_y, "Subtotal:")
    c.drawRightString(width - 23 * mm, totals_y, f"${subtotal:.2f}")

    c.drawRightString(width - 50 * mm, totals_y - 6 * mm, f"Tax ({data.get('tax_percent', 0)}%):")
    c.drawRightString(width - 23 * mm, totals_y - 6 * mm, f"${tax:.2f}")

    # Grand total box
    c.setFillColor(PRIMARY)
    c.rect(width - 80 * mm, totals_y - 18 * mm, 60 * mm, 10 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(width - 77 * mm, totals_y - 15 * mm, "TOTAL:")
    c.drawRightString(width - 23 * mm, totals_y - 15 * mm, f"${total:.2f}")

    # ---------- Footer ----------
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width / 2, 20 * mm, data.get("notes", "Thank you for your business!"))

    c.save()


def main():
    if len(sys.argv) < 2:
        print("Usage: python invoice_generator.py <data.json>")
        sys.exit(1)

    data_path = sys.argv[1]
    if not os.path.exists(data_path):
        print(f"File nahi mili: {data_path}")
        sys.exit(1)

    data = load_data(data_path)
    output_path = f"invoice_{data['invoice_number']}.pdf"
    generate_invoice(data, output_path)
    print(f"✅ Invoice generated: {output_path}")


if __name__ == "__main__":
    main()
