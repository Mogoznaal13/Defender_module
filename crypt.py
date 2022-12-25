from cryptography.fernet import Fernet
import os.path
import pathlib
import logger_config


def keyExists():
    path = 'Tools/Keys/crypt.key'
    return os.path.isfile(path)


def createKey():
    key = Fernet.generate_key()
    with open('Tools/Keys/crypt.key', 'wb') as key_file:
        key_file.write(key)
    logger_config.createLogMessage('Был сгенерирован ключ!', 'warning')


def load_key():
    return open('Tools/Keys/crypt.key', 'rb').read()


def encrypt(filepath, key):
    f = Fernet(key)
    filename = os.path.basename(filepath)

    pathFile = pathlib.Path("Tools", "Files", filename)
    pathCopy = pathlib.Path("Tools", "Copies", filename)

    with open(filepath, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(pathCopy, 'wb') as file:
        file.write(file_data)
        logger_config.createLogMessage(f'Была создана резервная копия файла {pathCopy}!', 'warning')

    with open(pathFile, 'wb') as file:
        file.write(encrypted_data)
        logger_config.createLogMessage(f'Был зашифрован файл {pathFile}!', 'warning')


def decrypt(filepath, key):
    f = Fernet(key)
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

    logger_config.createLogMessage(f'Был расшифрован файл {filepath}!', 'warning')