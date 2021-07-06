import configparser
import logging
import os
from pytelegram import TelegramAPI
from pyokex import OKExAPI
import time


def load_cfg(filename):
    """Loads the config.ini file and returns a cfg dictionary
    """

    config = configparser.ConfigParser()
    config.read(filename)

    cfg = {}
    cfg['telegram'] = {}
    cfg['telegram']['api_key'] = config['TelegramAPI']['api_key']
    cfg['telegram']['base_url'] = config['TelegramAPI']['base_url']

    if debug:
        cfg['telegram']['channel_id'] = config['PriceTracker_debug']['channel_id']
        cfg['coin'] = config['PriceTracker_debug']['coin']
        cfg['update_rate'] = int(config['PriceTracker_debug']['update_rate'])

    else:
        cfg['telegram']['channel_id'] = config['PriceTracker']['channel_id']
        cfg['coin'] = config['PriceTracker']['coin']
        cfg['update_rate'] = int(config['PriceTracker']['update_rate'])

    return cfg


def get_last_price(coin):
    """Gets a coin price from OKEx ticker information
    """

    okex_tickers = okex.get_tickers()
    xch_ticker = [t for t in okex_tickers if t['instrument_id'] == coin][0]
    xch_ticker = xch_ticker['last']
    assert xch_ticker.replace(".", "", 1).isdigit()
    last_price = float(xch_ticker)
    return last_price


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # setting up a logger
    logging.basicConfig(filename='price.log',
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d T %H-%M-%S',
                        level=logging.DEBUG,
                        )
    debug = False

    # loading config.ini file
    cfg = load_cfg('config.ini')

    # initializing telegram API
    telegram = TelegramAPI(cfg['telegram']['api_key'],
                           cfg['telegram']['base_url'])

    # initializing OKEx API
    okex = OKExAPI()

    # posting iteration
    channel_id = cfg['telegram']['channel_id']
    while True:
        try:
            last_price = get_last_price(cfg['coin'])
            logging.info(f' {last_price:.1f}$')
            response = telegram.send_message(channel_id, f'{last_price:.1f}$')
        except:
            logging.info(f' An Error happened')
            time.sleep(cfg['update_rate'])

        time.sleep(cfg['update_rate'])
