import os

from cryptography.fernet import Fernet


def load_key():

    return open('secret.key', 'rb').read()


def decrypt_file(file_path):

    key = load_key()

    fernet = Fernet(key)


    with open(file_path, 'rb') as file:

        file_data = file.read()

        decrypted_data = fernet.decrypt(file_data)


        with open(file_path, 'wb') as file:

            file.write(decrypted_data)


def main():

    decrypt_file('panda.jpg')


if __name__ == '__main__':

    main()
