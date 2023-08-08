# problem2, 25/05/21, Cordelia Jiang
# including the printing of a full statement at the end.

balanceList = []  # stores balance ($) in a list for statement printing
amountList = []  # stores ride amount ($) and top up amount ($) in a list for statement printing
eventList = []  # stores event name as string in a list for statement printing
initialBalanceList = []


class GoCard:
    # a constructor __init__ is required to set up the account with an initial balance
    def __init__(self, initialBalance):
        self._initialBalance = initialBalance
        initialBalanceList.append(self._initialBalance)

    # contains a method that accepts the amount as a parameter, it needs to record the amount each ride costs
    def recordRide(self, rideCostAmount):
        rideCostAmount = rideCostAmount  # store number of inputted ride cost in a variable
        rideEvent = "Ride"
        self._initialBalance = self._initialBalance - rideCostAmount  # update balance
        balanceList.append(self._initialBalance)
        amountList.append(rideCostAmount)
        eventList.append(rideEvent)

    # contains a method that accepts the amount as a parameter, it needs to record the amount for each top-up
    def recordTopUp(self, topUpAmount):
        topUpAmount = topUpAmount
        topUpEvent = "Top Up"
        self._initialBalance = self._initialBalance + topUpAmount
        balanceList.append(self._initialBalance)
        amountList.append(topUpAmount)
        eventList.append(topUpEvent)

    # contains a method that returns the current balance
    def reportBalance(self):
        return "Balance = ${:.2f}".format(self._initialBalance)  # returns balance in 2 decimal places

    # print out a statement of all of the transactions.
    # formatting rows of printing statement
    def printStatement(self):
        print("Statement: ", end="\n")
        print("event", end="               ")
        print("amount ($)", end="  ")
        print("balance ($)", end="\n")

        # the format :>27.2f means right-justified with a total field width of 27, and put number in 2 decimal places
        print("Initial balance", "{:>27.2f}".format(initialBalanceList[0]))

        # check whether it's a ride or top up event and print accordingly.
        for i in range(len(balanceList)):
            if eventList[i] == "Ride":
                print(eventList[i], "{:>25.2f}".format(amountList[i]), "{:>12.2f}".format(balanceList[i]))
            else:
                print(eventList[i], "{:>23.2f}".format(amountList[i]), "{:>12.2f}".format(balanceList[i]))
        print("Final balance", "{:>29.2f}".format(self._initialBalance))


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

goCardAccount.printStatement()
