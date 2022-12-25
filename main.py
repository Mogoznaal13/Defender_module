import eel
from auth import checkCorrectFlash, keyGet
from crypt import keyExists, createKey, load_key, encrypt, decrypt
from logger_config import createLogMessage, getLogs
from handler.Models.User import getAllUsers, deleteUser, createUser, getUserById
import logger_config
import hashlib
import os

file_hash = os.path.basename(__file__)
with open(file_hash, "rb") as f:
    file_bytes = f.read()  # read file as bytes
    readable_hash = hashlib.sha1(file_bytes).hexdigest()
    logger_config.createLogMessage(readable_hash, 'warning')


@eel.expose
def checkFlash(userName):
    return checkCorrectFlash(userName)


@eel.expose
def getKey():
    return keyGet()


@eel.expose
def logWrite(messageText, messageType):
    return createLogMessage(messageText, messageType)


@eel.expose
def logGet():
    return getLogs()


@eel.expose
def getUsers():
    return getAllUsers()


@eel.expose
def getUser(userId):
    return getUserById(userId)


@eel.expose
def delUser(userId):
    return deleteUser(userId)


@eel.expose
def createUsr(user):
    return createUser(user)


@eel.expose
def existKey():
    return keyExists()


@eel.expose
def generateKey():
    return createKey()


@eel.expose
def encryptFile(filename):
    return encrypt(filename, load_key())


@eel.expose
def decryptFile(filename):
    return decrypt(filename, load_key())


eel.init('web')
eel.start('pages/auth.html', size=(800, 400))
