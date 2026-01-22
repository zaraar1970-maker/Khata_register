import pandas as pd
from datetime import datetime
from fpdf import FPDF

# Ye sirf Report ke upar print hoga (App Owner)
OWNER_NAME = "Adil Mumtaz"
OWNER_CONTACT = "03218537625"

class KhataBookApp:
    def __init__(self):
        self.file = "khata_records.csv"
        try: self.df = pd.read_csv(self.file)
        except: self.df = pd.DataFrame(columns=["Date", "Cust_Name", "Cust_Mobile", "Amount", "Desc", "Type"])

    def add_entry(self):
        print("\n--- Nayi Entry (Transaction) ---")
        c_name = input("Customer ka Naam: ")
        c_mobile = input("Customer ka Mobile Number: ") # Yahan customer ka number aayega
        amt = input("Raqam (PKR): ")
        description = input("Tafseel (Description): ")
        t_type = input("Paisa Aaya (In) ya Gaya (Out): ").lower()

        # Data save karna
        new_row = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Cust_Name": c_name,
            "Cust_Mobile": c_mobile,
            "Amount": amt,
            "Desc": description,
            "Type": t_type
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.file, index=False)

        # WhatsApp Message Link (Sirf Customer ke liye)
        message = f"Salam {c_name}, aapka PKR {amt} ka hisab update ho gaya hai. {description}."
        wa_link = f"https://wa.me/92{c_mobile[1:]}?text={message.replace(' ', '%20')}"
        
        print(f"\n✅ Entry Saved!")
        print(f"📲 Customer ko WhatsApp bhejne ke liye link: {wa_link}")

    def export_all(self):
        # Excel File
        self.df.to_excel("Mukammal_Khata.xlsx", index=False)
        
        # PDF File with Owner Header
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=f"Khata Book: {OWNER_NAME}", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=f"Owner Contact: {OWNER_CONTACT}", ln=True, align='C')
        pdf.output("Khata_Report.pdf")
        print("\n📁 Excel aur PDF files download ke liye tayyar hain!")

# --- Application Loop ---
khata = KhataBookApp()
while True:
    print(f"\n--- {OWNER_NAME} Digital Ledger ---")
    print("1. Add Entry (Name/Customer Mobile/Amount)")
    print("2. Download Reports (Excel/PDF)")
    print("3. Exit")
    
    choice = input("Option select karein: ")
    if choice == '1': khata.add_entry()
    elif choice == '2': khata.export_all()
    elif choice == '3': break
 
