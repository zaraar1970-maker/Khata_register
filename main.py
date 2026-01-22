import pandas as pd
from datetime import datetime
from fpdf import FPDF

# Aapki details jo screenshots mein thi
USER_NAME = "Adil Mumtaz"
USER_PHONE = "03218537625"
USER_EMAIL = "palajalalpuria1965@gmail.com"

class KhataApp:
    def __init__(self):
        self.file_name = "khata_data.csv"
        try:
            self.df = pd.read_csv(self.file_name)
        except:
            # Naya register banaya agar file maujood nahi hai
            self.df = pd.DataFrame(columns=["Date", "Name", "Mobile", "Amount", "Description", "Type"])

    def add_entry(self):
        print("\n" + "="*30)
        print("      NEW ENTRY")
        print("="*30)
        name = input("Customer Name: ")
        phone = input("Customer Mobile: ")
        amount = float(input("Amount (PKR): "))
        desc = input("Description: ")
        # Type 'in' matlab paisa aaya, 'out' matlab paisa gaya
        entry_type = input("Type (In/Out): ").lower()

        new_row = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Name": name,
            "Mobile": phone,
            "Amount": amount,
            "Description": desc,
            "Type": entry_type
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)
        print("\n✅ Transaction Saved Successfully!")

    def show_summary(self):
        total_in = self.df[self.df['Type'] == 'in']['Amount'].sum()
        total_out = self.df[self.df['Type'] == 'out']['Amount'].sum()
        balance = total_in - total_out
        
        print("\n" + "*"*40)
        print(f"KHATA SUMMARY FOR {USER_NAME}")
        print(f"Contact: {USER_PHONE}")
        print("-" * 40)
        print(f"Total Cash In : PKR {total_in}")
        print(f"Total Cash Out: PKR {total_out}")
        print(f"NET BALANCE   : PKR {balance}")
        print("*"*40)

# Main Loop
app = KhataApp()
while True:
    print(f"\nWelcome to {USER_NAME}'s Digital Khata")
    print("1. Add Transaction (Name/Mobile/Amount/Desc)")
    print("2. View Ledger Summary")
    print("3. Exit")
    
    choice = input("\nApna option select karein: ")
    
    if choice == '1':
        app.add_entry()
    elif choice == '2':
        app.show_summary()
    elif choice == '3':
        print("KhataBook band ho rahi hai. Allah Hafiz!")
        break
