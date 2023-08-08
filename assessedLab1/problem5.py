# problem5, 07/08/21, Cordelia Jiang
# Define a business class. Write a constructor (__init__) to set up the business with
# initial values including name, address, founding year, email address and phone number.
# Write a function called change phone to update the phone number.
class Business:
    # a constructor __init__ is required to set up business with name, address, foundingYear, emailAddress, phoneNumber
    def __init__(self, name, address, foundingYear, emailAddress, phoneNumber):
        self.name = name
        self.address = address
        self.foundingYear = foundingYear
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

    # contains a method that accepts phoneNumber as an argument, used to change phone number
    def changePhone(self, newPhoneNumber):
        self.phoneNumber = newPhoneNumber
        return newPhoneNumber


# create objects using class Business
business1 = Business('Business 1', '1 Busy Street, Business, 4000', '1991', 'business1@company.com', '0400000001')
business2 = Business('Business 2', '2 Busy Street, Business, 4000', '1992', 'business2@company.com', '0400000002')


# printing old business info
print(business1.name, business1.address, business1.foundingYear, business1.emailAddress, business1.phoneNumber, sep=", ")
print(business2.name, business2.address, business2.foundingYear, business2.emailAddress, business2.phoneNumber, sep=", ")

# calling changePhone method of Business class to change phone number for business1 and business2,
# and store return result in two variables.
changePhoneBusiness1 = business1.changePhone('0410000000')
changePhoneBusiness2 = business1.changePhone('0420000000')


# printing new business info
print(business1.name, business1.address, business1.foundingYear, business1.emailAddress, changePhoneBusiness1, sep=", ")
print(business2.name, business2.address, business2.foundingYear, business2.emailAddress, changePhoneBusiness2, sep=", ")
