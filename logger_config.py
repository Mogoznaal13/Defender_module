import logging


logging.basicConfig(level=logging.INFO, filename='logs/py_log.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',  datefmt='%H:%M:%S')


def createLogMessage(messageText: str, messageType: str):
    if messageType == 'debug':
        logging.debug(messageText)
    elif messageType == 'info':
        logging.info(messageText)
    elif messageType == 'critical':
        logging.critical(messageText)
    elif messageType == 'warning':
        logging.warning(messageText)

    return 'success'


def getLogs(filename='logs/py_log.log'):
    log = list()
    with open(filename, 'r') as file:
        for line in file:
            log.append(line)

    return log
