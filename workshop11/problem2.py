# problem2, 03/06/21, Cordelia Jiang
# add: add domainName, IPA to _ipaDict (white list)
# black: add domainName, IPA to _ipaBlackDict (black list)
# get: get IPA of domainName
# quit: terminate program


class DNS:
    def __init__(self):
        self._ipaDict = dict()  # the variable is made private, can't access the variable from outside the object

    # method for updating DNS with a new domain name and its IPA. define a dictionary ipaDict under Class DNS, using
    # the domain name as the key (unique) and IPA as the value.
    def addIPA(self, domainName, IPA):
        self._ipaDict[domainName] = IPA

    # method for returning the IPA for a domain name, return the value associated with key domainName in ipaDict,
    # optionally returning default None if the key domainName specified is not in ipaDict.
    def getIPA(self, domainName):
        return self._ipaDict.get(domainName, None)


# without changing DNS class, define a new class that extends your old class.
# DNSs should maintain a secret blacklist of IPAs that must not be returned, even if the domain name exists.
class extendDNS(DNS):
    def __init__(self):
        self._ipaBlackDict = dict()
        DNS.__init__(self)  # call to super class DNS

    # a method for adding an IPA to private blacklist
    def addBlackIPA(self, domainName, IPA):
        self._ipaBlackDict[domainName] = IPA

    # override the lookup method so that it returns None for blacklisted IPA
    def getIPA(self, domainName):
        # black list
        if domainName in self._ipaBlackDict:
            return None

        # white list
        elif domainName in self._ipaDict:
            return self._ipaDict.get(domainName, None)


dnsObject = extendDNS()  # create a dns object from the extendDNS class

command = input("? ").strip()  # removing both the leading and the trailing characters
while command != "quit":
    command = command.split()
    # behaves like switch statement
    if len(command) == 3 and command[0] == "add":  # if there's three words and the first word is add
        dnsObject.addIPA(command[1], command[2])  # parse it to addIPA function
    elif len(command) == 3 and command[0] == "black":
        dnsObject.addBlackIPA(command[1], command[2])
    elif len(command) == 2 and command[0] == "get":
        print(dnsObject.getIPA(command[1]))
    else:
        print("Bad Command.")

    command = input("? ").strip()  # refreshing sentinel pattern