from pathlib import Path

root = Path(r"C:\Users\Asus-2025\Downloads\stitch_electricity_bill_management_system\stitch_electricity_bill_management_system")
replacements = {
    'UrjaSetu Electricity': 'Electricity Bill Management System',
    'UrjaSetu Electricity Logo': 'Electricity Bill Management System Logo',
    'UrjaSetu Grid': 'Electricity Bill Management System',
    'UrjaSetu': 'Electricity Bill Management System',
    'urjasetu.gov.in': 'ebms.gov.in',
    'admin@urjasetu.gov.in': 'admin@ebms.gov.in',
    'UrjaSetu_Payments_Apr2024.csv': 'Electricity_Bill_Management_System_Payments_Apr2024.csv',
}

count = 0
for p in root.rglob('*.html'):
    text = p.read_text(encoding='utf-8', errors='ignore')
    new = text
    for old, replacement in replacements.items():
        new = new.replace(old, replacement)
    if new != text:
        p.write_text(new, encoding='utf-8')
        count += 1

print(f'updated_files={count}')
