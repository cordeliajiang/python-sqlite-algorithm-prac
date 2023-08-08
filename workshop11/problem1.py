# problem1, 01/06/21, Cordelia Jiang
# add: add domainName, IPA to _ipaDict (white list)
# get: get IPA of domainName
# quit: terminate program

class DNS:
    def __init__(self):
        self._ipaDict = dict()  # the variable is made private, can't access the variable from outside the object

    # method for updating DNS with a new domain name and its IPA.
    # define a dictionary ipaDict under Class DNS, using the domain name as
    # the key (unique) and IPA as the value.
    def addIPA(self, domainName, IPA):
        self._ipaDict[domainName] = IPA

    # method for returning the IPA for a domain name, return the value associated
    # with key domainName in ipaDict, optionally returning default None if the
    # key domainName specified is not in ipaDict.
    def getIPA(self, domainName):
        return self._ipaDict.get(domainName, None)


dnsObject = DNS()  # create a dns object from the DNS class

command = input("? ").strip()  # removing both the leading and the trailing characters
while command != "quit":
    command = command.split()
    # behaves like switch statement
    if len(command) == 3 and command[0] == "add":  # if there's two words and the first word is r
        dnsObject.addIPA(command[1], command[2])  # convert second word to float and parse it to recordRide function
    elif len(command) == 2 and command[0] == "get":
        print(dnsObject.getIPA(command[1]))
    else:
        print("Bad Command.")

    command = input("? ").strip()  # refreshing sentinel pattern
