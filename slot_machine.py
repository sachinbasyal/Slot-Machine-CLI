""" BASIC SLOT MACHINE"""
"""Algorthim: If you bet on one lines: need to check 1st row, if you bet on 2nd lines: need to check 1st and 2nd row..."""

import random
MAX_LINES = 3  # GLobal Constants
MAX_BET = 100
MIN_BET =1
ROWS =3
COLS =3

# Creating a distionary of symbol_count
symbols_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value ={
    "D": 2, # After spinning slot machine, if all three column values shows (D) -> Bet is multiplied by 2 times
    "C": 4,
    "B": 6,
    "A": 8
}

def check_winnings(columns, lines, symbol_value, bet):
    winnings =0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check !=symbol:
               break
        else:   # using "for-else" loop here so that if for loop executes successfully (without break), else statement will run afterwards
            winnings += symbol_value[symbol]*bet
            winning_lines.append(line+1)
              
    return winnings, winning_lines
        
#Let's imagine 3x3 slot machine with 3 rows and 3 columns of symbols in place
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[] # creating a list
    for symbol, symbol_count in symbols.items(): # symbols represent dictionary. This for-loop here will give us {keys}-symbol and {values}-symbol_count associated with the symbols dictioanary
        for _ in range(symbol_count): # _: denotes annonymous variable, when no iteration value is needed to represent in the code
            all_symbols.append(symbol)
            
    columns =[] # Here, columns is representing the list of vertical column-symbol-values inside the column
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:] # here, we have made a copy of all_symbols list to current_symbols so that each time we pick a random choice, the selected value gets removed from the newly copied list.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
   
    return columns

def print_slot_machine(columns):  # We need to transpose the matrix-list i.e., need to flip the print of columns' value display
    for row in range (len(columns[0])): # len(columns[0])=3, range(3) -> row =0 until 2
        for i, column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], end = " | ") # By default print() command prints the value and ends with new_line (\n) statement. Assigning end ="" -> not to perform next_line command 
            else:
                print(column[row], end ="")
        print()
            
def get_deposit():      
    while True:
        amount = input("Enter the amount of money you want to deposit: $")
        # Using try - except 
        # try:
        #     amount =int(amount)
        #     if amount <=0:
        #         print("The amount should be greater than $0")
                
        #     else: break
        # except Exception:
        #     print("Your amount is invalid!")
        if amount.isdigit(): # isdigit() function checks if the given "string" value is actual positive integer value.
            amount = int(amount)
            if amount > 0:
                break
            else: print('The amount should be greater than $0')

        else: print("Enter the valid amount.")
        
    return amount

def get_no_of_lines():
    while True:
        lines =input("Enter the number of lines you want to bet on [1 - "+str(MAX_LINES)+"]: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=lines <=MAX_LINES:
                break
            else: print('The number of lines should be between: 1 and ', str(MAX_LINES))
            
        else: print("Enter the valid number.")
        
    return lines

def get_bet():
    while True:
        amount = input("How much amount would you like to bet on each line? : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <=amount <=MAX_BET:
                break
            else: print(f"The amount must be between ${MIN_BET} and ${MAX_BET}")
            
        else: print("Enter the valid amount.")
        
    return amount

def play_game(balance):
    lines = get_no_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet = bet_amount *lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else: break
    print(f"Your are betting ${bet_amount} on {lines} lines. Total bet amount is: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    input("Press enter to spin the Slot!")
    print_slot_machine(slots)
    winning_amount, winning_lines = check_winnings(slots, lines, symbols_value, bet_amount)
    print(f"You have won: ${winning_amount}")
    print(f"You won on lines:",*winning_lines) # * represent splat operator: unpack operator -> prints every single value from the winning_lines list
    
    return (winning_amount - total_bet)

def main():
    balance = get_deposit()
    while True:
        print(f"Your current balance is ${balance}")
        play = input("Press enter to play the game. (Q/q to quit).").lower()
        if play =='q':
            break
        elif balance == 0:
            print("Sorry! You are broke :-( Better luck next time!")
            break
        else: 
            balance += play_game(balance)
    
    print(f"You have left with ${balance}. Thanks for playing!")

print("Welcome to Sachin's SLOT MACHINE!")          
main()
