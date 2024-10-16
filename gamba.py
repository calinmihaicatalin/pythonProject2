import random
def row_spin():
    symbols = ['🍌', '🍎', '🍐', '⭐', '⚡']
    return[random.choice(symbols) for _ in range(3)]

def row_print(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def generate_pay(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍌':
            return bet *3
        elif row[0] == '🍎':
            return bet *4
        elif row[0] == '🍐':
            return bet *5
        elif row[0] == '⭐':
            return bet *10
        elif row[0] == '⚡':
            return bet *15
    return 0

def main():
    balance = 100
    print("*******************************")
    print("        Zeus Debauchery!       ")
    print("*******************************")
    print("Welcome esteemed guest to the gods hub!")
    print()
    while balance > 0:
        print(f"The current tribute available to be offered is: {balance}")
        bet = input("Introduce your offering: ")
        print()
        if not bet.isdigit():
            print("Invalid amount, gods are displeased!")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds detected, exiting game...")
            continue
        elif bet <= 0:
            print("Invalid input, gods are displeased!")
            continue

        balance -= bet
        row = row_spin()
        print("Gods deciding...\n")
        row_print(row)
        payout = generate_pay(row,bet)

        if payout > 0:
            print(f"Gods have favoured you with: {payout}")
        else:
            print("Lightning has struck you!")

        balance += payout
        play_again = input("Do you want to spin? (Y/N): ").upper()
        if play_again != 'Y':
            break
    print(f"Game over Hero! Your final contribution is: {balance}")

if __name__ == '__main__':
    main()