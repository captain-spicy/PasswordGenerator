class PasswordGenerator:
    def __init__(self):
        self._set_password = None       # sets initial password to null
        self._sites = dict()            # creates an empty dict to hold sites
        self._show_password = False     # sets initial password visibility to none

    def push(self, urls):               # creates function to insert new sites into list
        self._sites
        # TODO finish setting up this section

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

    new_acc = PasswordGenerator(None)
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
        print("Please choose one of the following options:\n"
              "1. Find a site password\n2. Add a new site & password\n"
              "3. Remove a site & password\n4. Amend a password\n"
              "5. Exit\n ")

        selection = int(input())

        match int(str(selection[0])):

            case 1:
                print("insert site search here")
                print(new_acc._sites)
            case 2:
                new_acc.add_site()
            case 3:
                print("insert site removal here")
            case 4:
                print("insert amend password func")
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Please choose an option from 1 through 5 only.")
                continue


# TODO create dictionary list function that will hold all the websites and passwords
# TODO create password generator function and get the outputs to reference website keys
# TODO create a save file that the program can use to grab saved sites/passwords for future use
# need to check back on this