import logging
import os


def setup_logger():
    log_dir = os.path.dirname(os.path.abspath(__file__)) + "/logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # logging.basicConfig(filename=log_dir + "gpu-scraper.log", filemode='w', level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)
    logFormatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

    fileHandler = logging.FileHandler(log_dir + "scraper.log")
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    logger.setLevel(logging.DEBUG)

    return logger


logger = setup_logger()
