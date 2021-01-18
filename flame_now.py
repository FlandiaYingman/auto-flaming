import logging

import flaming

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    logging.info("Start auto flaming...")
    flaming.re_login()
    flaming.flame()
    logging.info("Wait for next auto flaming...")
