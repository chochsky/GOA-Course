def მენიუ():
    print("მოგესალმებით ბანკში!")
    print("1. შეამოწმეთ ბალანსი")
    print("2. შემოიტანეთ თანხა")
    print("3. გაიტანეთ თანხა")
    print("4. გასვლა")

def main():
    balance = 1000  # Initial balance
    while True:
        მენიუ()
        choice = input("აირჩიეთ (1-4): ")

        if choice == '1':
            print(f"ბალანსი ${balance:.2f}")
        
        elif choice == '2':
            try:
                amount = float(input("დეპოზიტის შეტანა: $"))
                if amount > 0:
                    balance += amount
                    print(f"ეარმატებით შეიტანეთ დეპოზიტი ${amount:.2f}")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '3':
            try:
                amount = float(input("გატანა: $"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"წარმატებით გაიტანეთ ${amount:.2f}")
                    else:
                        print("ბალანსი.")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '4':
            print("მადლობა რომ იყენებთ კოღო ბანკს!")
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()