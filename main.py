import json
from cryptography.fernet import Fernet
from pathlib import Path
from string import ascii_letters, digits
from random import choice


class PasswordGenerator:
    def __init__(self):
        self._set_password = None  # sets initial password to None
        self._sites = dict()  # creates an empty sites dict
        self._show_password = False  # sets initial password visibility to none
        self._saved_password = dict()  # creates an empty pass dict
        self._account_names = dict()  # creates an empty acc dict

    def create_acc(self):
        # creates an encryption key if password is entered correctly
        # key generation
        account_key = Fernet.generate_key()

        # string the key into a file
        with open('acc_key.key', 'wb') as acc_key:
            acc_key.write(account_key)

        new_account = input("New username: ")
        new_password = input("New password: ")
        create_acc = self._account_names

        # checks if the acc_list file exists, else creates a new file and encrypts it
        # if file exists, decrypts file and checks if username is taken
        path_to_file = 'acc_list.json'
        path = Path(path_to_file)

        if path.is_file():
            # opens the key
            with open("acc_key.key", 'rb') as acc_key:
                acc_key = acc_key.read()

            # using the key
            acc_key_fernet = Fernet(acc_key)

            # opening the encrypted file
            with open("acc_list.json", 'rb') as enc_file:
                acc_list_encrypted = enc_file.read()

            # decrypting the file
            acc_list_decrypted = acc_key_fernet.decrypt(acc_list_encrypted)

            # opening the file in write mode and
            # writing the decrypted data
            with open("acc_list.json", 'wb') as dec_file:
                dec_file.write(acc_list_decrypted)

            # reads the sites list file after decryption and assigns to _account_names dict
            with open("acc_list.json", 'r') as al:
                self._account_names = json.load(al)

                if new_account in self._account_names:
                    print("Username already exists!")
                else:
                    # creates a dict format with account and password
                    create_acc[new_account] = new_password

                    # writes the dict to a json file
                    with open("acc_list.json", 'a+') as f:
                        json.dump(create_acc, f)

                    # opening the key
                    with open('acc_key.key', 'rb') as acc_key:
                        acc_key = acc_key.read()

                    # using the generated key
                    acc_key_fernet = Fernet(acc_key)

                    # opening the original file to encrypt
                    with open("acc_list.json", 'rb') as file:
                        original = file.read()

                    # encrypting the file
                    acc_list_encrypted = acc_key_fernet.encrypt(original)

                    # opening the file in write mode and
                    # writing the encrypted data
                    with open('acc_list.json', 'wb') as encrypted_file:
                        encrypted_file.write(acc_list_encrypted)

        else:
            # creates a dict format with account and password
            create_acc[new_account] = new_password

            # writes the dict to a json file
            with open("acc_list.json", 'a+') as f:
                json.dump(create_acc, f)

            # opening the key
            with open('acc_key.key', 'rb') as acc_key:
                acc_key = acc_key.read()

            # using the generated key
            acc_key_fernet = Fernet(acc_key)

            # opening the original file to encrypt
            with open("acc_list.json", 'rb') as file:
                original = file.read()

            # encrypting the file
            acc_list_encrypted = acc_key_fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('acc_list.json', 'wb') as encrypted_file:
                encrypted_file.write(acc_list_encrypted)

    def check_acc_name(self):

        # checks if the acc_list file exists, else creates a new file and encrypts it
        # if file exists, decrypts file and checks if username is taken
        path_to_file = 'acc_list.json'
        path = Path(path_to_file)

        if path.is_file():
            # opens the key
            with open("acc_key.key", 'rb') as acc_key:
                acc_key = acc_key.read()

            # using the key
            acc_key_fernet = Fernet(acc_key)

            # opening the encrypted file
            with open("acc_list.json", 'rb') as enc_file:
                acc_list_encrypted = enc_file.read()

            # decrypting the file
            acc_list_decrypted = acc_key_fernet.decrypt(acc_list_encrypted)

            # opening the file in write mode and
            # writing the decrypted data
            with open("acc_list.json", 'wb') as dec_file:
                dec_file.write(acc_list_decrypted)

            # reads the sites list file after decryption and assigns to _account_names dict
            with open("acc_list.json", 'r') as al:
                self._account_names = json.load(al)
            counter = 0

            while counter < 3:
                acc_name = input("Username: ")
                acc_pass = input("Password: ")

                if (acc_name, acc_pass) in self._account_names.items():
                    print("Login confirmed! Welcome!")
                    break
                else:
                    counter += 1
                    print("Invalid login information!")

            if counter == 3:
                raise ValueError("Too many incorrect guesses! Account locked!")

        else:
            print("No users currently registered! Please create a new account first.")

    def add_site(self):
        # creates an encryption key to hold websites and passwords
        # key generation
        sites_key = Fernet.generate_key()

        # string the key into a file
        with open('sites_key.key', 'wb') as s_key:
            s_key.write(sites_key)

        # creates a site dict, creates a file to store, and encrypts file
        add_sites = self._sites

        print("Please enter a website name to add: \n")
        site_key = input("Website:")
        print("Create a randomly generated password or enter your own?\n"
              "(1) Random password generation\n"
              "(2) Enter my own password\n")

        rand_or_self = int(input("Please choose option 1 or 2: "))
        while True:
            match int(rand_or_self):
                case 1:
                    print("How many characters does the password need?")

                    def pass_gen(x):
                        return ''.join([choice(ascii_letters + digits) for i in range(x)])

                    char_count = int(input("Character count required: "))
                    site_value = pass_gen(char_count)
                    print("Randomly created password to use: ", site_value)
                    break

                case 2:
                    site_value = input("Please enter your own password:")
                    break
                case _:
                    print("Please choose either option 1 or 2 only.")
                    continue

        add_sites[site_key] = site_value

        # writes the dict to a json file
        with open("sites_list.json", 'w') as f:
            json.dump(add_sites, f)

        # opening the key
        with open('sites_key.key', 'rb') as sites_key:
            sites_key = sites_key.read()

        # using the generated key
        fernet = Fernet(sites_key)

        # opening the original file to encrypt
        with open("sites_list.json", 'rb') as file:
            original = file.read()

        # encrypting the file
        sites_list_encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('sites_list.json', 'wb') as encrypted_file:
            encrypted_file.write(sites_list_encrypted)

    def view_sites(self):
        # opens the key
        with open("sites_key.key", 'rb') as sites_key:
            sites_key = sites_key.read()

        # using the key
        sites_key_fernet = Fernet(sites_key)

        # opening the encrypted file
        with open("sites_list.json", 'rb') as enc_file:
            sites_list_encrypted = enc_file.read()

        # decrypting the file
        sites_list_decrypted = sites_key_fernet.decrypt(sites_list_encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open("sites_list.json", 'wb') as dec_file:
            dec_file.write(sites_list_decrypted)

        # reads the sites list file after decryption and assigns to _sites dict
        with open("sites_list.json", 'r') as sl:
            self._sites = json.load(sl)

        # prints out the site list
        for site_key in self._sites:
            print("Website:", site_key, " : ", "Password:", self._sites[site_key])


if __name__ == '__main__':

    new_acc = PasswordGenerator()
    while True:
        login = input("Welcome! Do you have an account with us? Please type Y or N : ").upper()
        if login not in "YN" or len(login) != 1:
            print("Please enter either Y or N only.")
            continue
        if login == 'N':
            new_acc.create_acc()
            continue
        elif login == 'Y':
            new_acc.check_acc_name()
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
#TODO encryption of files not opening existing files correctly, need to research more on encryption/decryption methods