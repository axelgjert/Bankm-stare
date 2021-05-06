from functions import *
read_file()


while True:
    meny = ("\n#######################"
            "\n# Lilla bankens meny"
            "\n# Saldo: {} kr"
            "\n#######################"
            "\n1. Visa transaktioner"
            "\n2. Gör en insättning"
            "\n3. Gör ett uttag"
            "\n4. Nollställ kontot"
            "\n0. Avsluta programmet"
            "\nGör ditt val: ").format(balance())

    val = valdidate_int(meny, "Felaktig inmatning! ")

    if val == 0:
        breakpoint
    elif val == 1:
        print(print_transactions())

    elif val == 2:
        deposit = validate_int("Ange hur mycket du vill sätta in: ", "Felaktig inmatning!")
        if deposit > 0:
            add_transaction(deposit, True)
        else: 
            print("En insättning måste vara större än 0.")
    
    elif val == 3: 
        withdraw = validate_int("Ange hur mycket du vill ta ut: ", "Felaktig inmatning!")
        if withdraw <= balance() and withdraw >= 0:
            add_transaction(-withdraw, True)
        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")
        else:
            print("Uttaget får inte vara större än saldot. Uttag medges ej.")
        
    elif val == 4:
        os.remove(filename)
        transactions.clear()
        read_file

    else:
        print("felaktigt val!")

print("Tack för ditt besök, välkommen åter!")