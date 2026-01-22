import os

class GoogleAuth:
    def __init__(self):
        self.authorized_email = "palajalalpuria1965@gmail.com"

    def login(self):
        print("\n" + "="*40)
        print(f"        G {RED}o{Y}o{G}g{B}l{RED}e{W} Login Service")
        print("="*40)
        email = input("Enter your Gmail: ")
        
        if email == self.authorized_email:
            print(f"\n{G}✅ Authentication Successful!{W}")
            print(f"Welcome, Adil Mumtaz. Your data is being synced...")
            return True
        else:
            print(f"\n{R}❌ Access Denied!{W}")
            print("This Gmail is not linked to this KhataBook.")
            return False
