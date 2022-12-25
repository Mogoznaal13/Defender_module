import wmi
from logger_config import createLogMessage
from handler.Models.User import getUserByName
import hashlib
import uuid


c = wmi.WMI()


def hash_password(password):
    number = uuid.uuid4().hex
    return hashlib.sha1(number.encode() + password.encode()).hexdigest() + ':' + number


def checked_password(hashed_password, user_password):
    password, number = hashed_password.split(':')
    return password == hashlib.sha1(number.encode() + user_password.encode()).hexdigest()


def keyGet():
    for drive in c.Win32_DiskDrive():
        if drive.InterfaceType == "USB":
            key = hash_password(drive.SerialNumber)
        else:
            key = False

    return key


def checkCorrectFlash(userName):
    user = getUserByName(userName)
    result = dict()

    if user is not None:
        for drive in c.Win32_DiskDrive():
            if drive.InterfaceType == "USB":
                result = {
                    'user': {
                        'name': user.name,
                        'role': user.role,
                        'auth_status': checked_password(user.serial_number, drive.SerialNumber)
                    }
                }
                if result['user']['auth_status']:
                    createLogMessage(f"Успешная авторизация у {user.name}!", 'warning')
                else:
                    createLogMessage(f"Пользователь {user.name} пытается зайти с помощью чужой флешки!", 'critical')
                    result = {
                        'user': {
                            'name': user.name,
                            'role': user.role,
                            'auth_status': checked_password(user.serial_number, drive.SerialNumber)
                        }
                    }
            else:
                createLogMessage(f"Попытка авторизации без флешки у {user.name}!", 'error')
                result = {
                    'user': {
                        'name': user.name,
                        'role': user.role,
                        'auth_status': checked_password(user.serial_number, drive.SerialNumber)
                    }
                }
    else:
        createLogMessage(f"Попытка авторизации для несуществующего пользователя", 'error')
        result = False

    return result
