# problem1, 23/05/21, Cordelia Jiang
# leaving out the printing of a full statement at the end.

class GoCard:
    # a constructor __init__ is required to set up the account with an initial balance
    def __init__(self, initialBalance):
        self._initialBalance = initialBalance

    # contains a method that accepts the amount as a parameter, it needs to record the amount each ride costs
    def recordRide(self, rideCostAmount):
        self._initialBalance = self._initialBalance - rideCostAmount

    # contains a method that accepts the amount as a parameter, it needs to record the amount for each top-up
    def recordTopUp(self, topUpAmount):
        self._initialBalance = self._initialBalance + topUpAmount

    # contains a method that returns the current balance
    def reportBalance(self):
        return "Balance = ${:.2f}".format(self._initialBalance)  # returns balance in 2 decimal places


initialBalanceInput = float(input("Creating account. Input initial balance: "))
goCardAccount = GoCard(initialBalanceInput)

command = input("? ").strip()  # removing both the leading and the trailing characters
while command != "q":
    command = command.split()
    # behaves like switch statement
    if len(command) == 2 and command[0] == "r":  # if there's two words and the first word is r
        goCardAccount.recordRide(float(command[1]))  # convert second word to float and parse it to recordRide function
    elif len(command) == 2 and command[0] == "t":
        goCardAccount.recordTopUp(float(command[1]))
    elif len(command) == 1 and command[0] == "b":
        print(goCardAccount.reportBalance())
    else:
        print("Bad Command.")

    command = input("? ").strip()  # refreshing sentinel pattern

