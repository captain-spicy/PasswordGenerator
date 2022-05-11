import json
from cryptography.fernet import Fernet
from pathlib import Path


class PasswordGenerator:
    def __init__(self):
        self._set_password = None       # sets initial password to None
        self._sites = dict()            # creates an empty sites dict
        self._show_password = False     # sets initial password visibility to none
        self._saved_password = dict()   # creates an empty pass dict

    def set_password(self):             # creates account password
        password = input("Please create an account password: ")
        self._set_password = password
        return self._set_password

    def saved_password(self):
        saved_passwords = self._saved_password
        path_to_password = "saved_pass.json"
        path = Path(path_to_password)
        # key generation for new password being added to list
        p_key = Fernet.generate_key()

        # string the key into a file
        with open('p_file_key.key', 'wb') as p_file_key:
            p_file_key.write(p_key)

        # checks if the password exists and if not then
        # creates a file and saves new password to file
        if path.is_file() is True:

            # decrypts the password file if file exists
            # opens the key
            with open("p_file_key.key", 'rb') as file_key:
                p_key = file_key.read()

            # using the key
            p_fernet = Fernet(p_key)

            # opening the encrypted file
            with open("saved_pass.json", 'rb') as p_enc_file:
                p_encrypted = p_enc_file.read()

            # decrypting the file
            p_decrypted = p_fernet.decrypt(p_encrypted)

            # opening the file in write mode and
            # writing the decrypted data
            with open("saved_pass.json", 'wb') as p_dec_file:
                p_dec_file.write(p_decrypted)

            # with the file unencrypted, appends new password to file
            with open("saved_pass.json", "a") as np:
                json.dump(saved_passwords, np)
                #TODO come back to this and check if needs to be an append or if needs to check against list

        else:
            # creates a new file and adds password to file with encryption
            with open("saved_pass.json", "w") as s_p:
                json.dump(self._set_password, s_p)

            # opening the key
            with open('p_file_key.key', 'rb') as file_key:
                key = file_key.read()

            # using the generated key
            fernet = Fernet(key)

            # opening the original file to encrypt
            with open("saved_pass.json", 'rb') as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('saved_pass.json', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

    @property
    def show_password(self):
        # currently show password is set to False at SoS
        return self._show_password

    @show_password.setter
    def show_password(self, value):
        # requests account password, giving 3 chances before locking up
        counter = 0

        while counter < 3:

            if value:
                password = input("Please enter your password: ")
                if password == self.saved_password():
                    print("Correct password entered!")
                    self._show_password = value

                    # creates an encryption key if password is entered correctly
                    # key generation
                    key = Fernet.generate_key()

                    # string the key into a file
                    with open('file_key.key', 'wb') as file_key:
                        file_key.write(key)
                    break
                else:
                    counter += 1
                    print("Incorrect password! Try again!")

        if counter == 3:
            raise ValueError("Too many guesses! Account locked!")

    def add_site(self):
        # creates a site dict, creates a file to store, and encrypts file
        add_sites = self._sites

        print("Please enter a website name to add: \n")
        site_key = input(print("Website:"))
        site_value = input(print("Password:"))
        add_sites[site_key] = site_value

        # writes the dict to a json file
        with open("sites_list.json", 'w') as f:
            json.dump(add_sites, f)

        # opening the key
        with open('file_key.key', 'rb') as file_key:
            key = file_key.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open("sites_list.json", 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('sites_list.json', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def view_sites(self):
        # opens the key
        with open("file_key.key", 'rb') as file_key:
            key = file_key.read()

        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open("sites_list.json", 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open("sites_list.json", 'wb') as dec_file:
            dec_file.write(decrypted)

        # reads the sites list file after decryption and assigns to _sites dict
        with open("sites_list.json", 'r') as sl:
            self._sites = json.load(sl)

        # prints out the site list
        for site_key in self._sites:
            print(site_key, " : ", self._sites[site_key])


if __name__ == '__main__':

    new_acc = PasswordGenerator()
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

        match int(selection):

            case 1:
                new_acc.view_sites()
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
