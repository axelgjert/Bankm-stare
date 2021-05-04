from config import *

def balance():
    balance = 0
    for t in transactions:
        balance += t
    return balance

def validate_int(output, error_mess):
    while true:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transactions():
    line = 0
    balance = 0
    output = ("\nAlla tranaktioner:"
              "\n{:>12} {:>12}"
              "\n------------------------").format ("Nr", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        balance += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format (line, t, balance))
        
    return output

def check_file_exists():
    try:
        with open(filename, "x"):
            print("Filen skapades")

        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    except:
        return

def read_file():

    check_file_exists()
    
    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
                
def add_transactions(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n2".format(transaction))