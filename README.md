# 🧾 Invoice Generator (Python + PDF)

A Python tool that **auto-generates professional PDF invoices from client data**.
It handles invoice numbers, line items, tax, and totals automatically — producing clean, branded invoices in seconds.

> Helped a freelancer client create **dozens of invoices monthly** without touching a template manually.

---

## ✨ Features

- ✅ Generates clean, professional PDF invoices
- ✅ Auto-calculates subtotal, tax, and grand total
- ✅ Supports multiple line items (description, qty, price)
- ✅ Branded header with company & client details
- ✅ Data-driven — just edit a simple JSON file
- ✅ Saves each invoice as a separate PDF

---

## 🛠️ Tech Stack

- **Python 3**
- **ReportLab** – PDF generation
- **JSON** – simple data input

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/waseemqadir345/invoice-generator.git
cd invoice-generator
```

📖 Usage

python invoice_generator.py sample_data/invoice_data.json

This creates a file like invoice_1001.pdf in the project folder.

⚙️ Customize Your Invoice
Open sample_data/invoice_data.json and edit:

company → your business name & email
client → customer details
items → list of services/products (description, quantity, price)
tax_percent → tax rate (e.g. 10)
notes → footer message


📂 Project Structure

invoice-generator/
├── README.md
├── requirements.txt
├── invoice_generator.py
├── .gitignore
└── sample_data/
    └── invoice_data.json


👤 Author
M Waseem Q — Python Developer & Web Automation Specialist
📩 Available for freelance work on Upwork.

📝 License
MIT License — free to use and modify.
# 2. Install dependencies
pip install -r requirements.txt
