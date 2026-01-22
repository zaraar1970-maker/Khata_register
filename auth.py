class GoogleAuth:
    def __init__(self):
        self.current_user = None

    def login(self):
        print("\n" + "="*40)
        print("      WELCOME TO CASHBOOK APP")
        print("="*40)
        email = input("Apni Gmail ID se Login karein: ")
        
        if "@gmail.com" in email.lower():
            self.current_user = email.lower()
            print(f"✅ Welcome! Aapka data sync ho raha hai: {self.current_user}")
            return True
        else:
            print("❌ Galat Email! Baraye meherbani sahi Gmail likhein.")
            return False
