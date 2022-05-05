class PasswordGenerator:
    def __init__(self, sites):
        self._set_password = None       # sets initial password to null
        self._sites = list(sites)       # creates an empty list to hold sites
        self._show_password = False     # sets initial password visibility to none

    def push(self, urls):               # creates function to insert new sites into list
        self._sites.insert(0, urls)

    def set_password(self):             # creates account password
        self._set_password = input("Please create an account password: ")
        return self._set_password       # returns the new password to replace null

    @property
    def show_password(self):
        return self._show_password      # currently show password is set to False at SoS

    @show_password.setter
    def show_password(self, value):     # requests account password, giving 3 chances before locking up
        counter = 0

        while counter < 3:

            if value:
                password = input("Please enter your password: ")
                if password == self._set_password:
                    print("Correct password entered!")
                    self._show_password = value
                    break
                else:
                    counter += 1
                    print("Incorrect password! Try again!")

        if counter == 3:
            raise ValueError("Too many guesses! Account locked!")

    def add_site(self):
        return self.push(input("Please enter a website name to add: "))


if __name__ == '__main__':

    new_acc = PasswordGenerator(["google", "yahoo", "facebook"])
    while True:
        login = input("Welcome! Do you have an account with us? Please type Y or N : ").upper()
        if login not in "YN" or len(login) != 1:
            print("Please enter either Y or N only.")
            continue
        if login == 'N':
            new_acc.set_password()
            print("New password has been created!")
            continue
        elif login == 'Y':
            new_acc.show_password = True
            break
    while True:
        selection = input("Please choose one of the following options:"
                          "1. Find password\n 2. Add a new site & password\n"
                          "3. Remove a site & password\n 4. Amend a password\n"
                          "5. Exit\n ")
        # TODO insert case switch statement here with different options

    new_acc.add_site()
    print(new_acc._sites)

# TODO create dictionary list function that will hold all the websites and passwords
# TODO create password generator function and get the outputs to reference website keys
# TODO create a save file that the program can use to grab saved sites/passwords for future use
# need to check back on this