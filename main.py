from auth import GoogleAuth
import pandas as pd
from datetime import datetime

# --- Theme Colors ---
G = '\033[92m' # Green
R = '\033[91m' # Red
B = '\033[94m' # Blue
Y = '\033[93m' # Yellow
W = '\033[0m'  # Reset

class KhataBookCloud:
    def __init__(self):
        self.file = "cloud_khata_backup.csv"
        try: self.df = pd.read_csv(self.file)
        except: self.df = pd.DataFrame(columns=["Date", "Name", "Mobile", "Amount", "Desc", "Type"])

    def show_dashboard(self):
        # Top Bar (Like Screenshot)
        print(f"\n{B}≡ Cashbook{W}          🔍  {Y}📄{W}  {B}📅{W}  ⋮")
        print(f"{'—'*45}")
        print(f" All | Daily | Week | Month | Year")
        print(f"{'—'*45}")

        c_total = self.df[self.df['Type'] == 'Credit']['Amount'].sum()
        d_total = self.df[self.df['Type'] == 'Debit']['Amount'].sum()

        if self.df.empty:
            print(f"\n      {Y}No transactions found in Cloud.{W}")
        else:
            for _, row in self.df.iterrows():
                color = G if row['Type'] == 'Credit' else R
                print(f" {row['Name'].ljust(15)} | {row['Desc'].ljust(15)} {color}{row['Amount']}{W}")
                print(f" {W}at {row['Date']}")
                print("-" * 45)

        # Bottom Summary Blocks
        print(f"\n{G}  + Credit          {R} - Debit          {B}   Total{W}")
        print(f"   {c_total:,.0f}               {d_total:,.0f}               {c_total-d_total:,.0f}")
        print("="*45)

    def add_entry(self, t_type):
        name = input("Customer Name: ")
        phone = input("Customer Mobile: ")
        amt = float(input("Amount: "))
        desc = input("Description: ")
        
        new_row = {"Date": datetime.now().strftime("%d %b, %I:%M %p"), 
                    "Name": name, "Mobile": phone, "Amount": amt, "Desc": desc, "Type": t_type}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.df.to_csv(self.file, index=False)

# --- Execution ---
auth = GoogleAuth()
if auth.login():
    app = KhataBookCloud()
    while True:
        app.show_dashboard()
        print(f"{G}[+] Credit{W}    {R}[-] Debit{W}    [E] Exit")
        cmd = input("\nSelect: ").upper()
        if cmd == '+': app.add_entry("Credit")
        elif cmd == '-': app.add_entry("Debit")
        elif cmd == 'E': break
