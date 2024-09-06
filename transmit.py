import os

from cryptography.fernet import Fernet


def generate_key():

    key = Fernet.generate_key()

    with open('secret.key', 'wb') as key_file:

        key_file.write(key)


def load_key():

    return open('secret.key', 'rb').read()


def encrypt_file(file_path):

    key = load_key()

    fernet = Fernet(key)


    with open(file_path, 'rb') as file:

        file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)


        with open(file_path, 'wb') as file:

            file.write(encrypted_data)


def main():

    if not os.path.exists('secret.key'):

        generate_key()

    encrypt_file('panda.jpg')


if __name__ == '__main__':

    main()
