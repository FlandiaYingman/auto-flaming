import logging
import time

import schedule

import flaming

FLAMING_TIME = '09:00'
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def work():
    logging.info("Start auto flaming...")
    flaming.re_login()
    flaming.flame()
    logging.info("Wait for next auto flaming...")


if __name__ == '__main__':
    schedule.every().day.at(FLAMING_TIME).do(work)
    logging.info("Wait for auto flaming...")
    while True:
        schedule.run_pending()
        time.sleep(1.0)
