from datetime import datetime, timedelta
import time
import ccxt
import yaml


MESSAGES = {}
VARIABLES = {}


# Saving environment variables
def setup():

    # Open config file and save variables locally
    with open('config.yaml', 'r') as myfile:
        config = yaml.load(myfile, Loader=yaml.Loader)

        # Save all messages to MESSAGES
        MESSAGES['exchange'] = config['MESSAGES']['message_1']
        MESSAGES['exchange_not_found'] = config['MESSAGES']['message_1_error_handler']
        MESSAGES['api_public_key'] = config['MESSAGES']['message_2']
        MESSAGES['api_private_key'] = config['MESSAGES']['message_3']
        MESSAGES['ticker'] = config['MESSAGES']['message_4']
        MESSAGES['ticker_not_found'] = config['MESSAGES']['message_4_error_handler']
        MESSAGES['candle_interval'] = config['MESSAGES']['message_5']
        MESSAGES['candle_interval_not_found'] = config['MESSAGES']['message_5_error_handler']
        MESSAGES['start_date'] = config['MESSAGES']['message_6']
        MESSAGES['start_date_not_found'] = config['MESSAGES']['message_6_error_handler']
        MESSAGES['end_date'] = config['MESSAGES']['message_7']
        MESSAGES['end_date_not_found'] = config['MESSAGES']['message_7_error_handler']

        # Save all variables to VARIABLES
        VARIABLES['exchange'] = config['VARIABLES']['EXCHANGE']
        VARIABLES['start_date'] = config['VARIABLES']['START_DATE']
        VARIABLES['end_date'] = config['VARIABLES']['END_DATE']


def main():

    #  1. Enter exchange used
    if VARIABLES['exchange'] is None:
        VARIABLES['exchange'] = input(MESSAGES['exchange'])
    try:
        exchange = getattr(ccxt, VARIABLES['exchange'].lower())()
    except:
        print(MESSAGES['exchange_not_found'] % VARIABLES['exchange'])
        return

    #   2. Add API public key if needed
    # api_public_key = input(MESSAGES['api_public_key'])
    #  3. Add API private key if needed
    # API_PRIVATE_KEY = input(MESSAGES['API_PRIVATE_KEY'])

    #  4. Enter ticker
    VARIABLES['ticker'] = input(MESSAGES['ticker'])
    if VARIABLES['ticker'] not in exchange.fetch_tickers():
        print(MESSAGES['ticker_not_found'] % VARIABLES['TICKER'])
        return

    #  5. Enter candle_interval
    VARIABLES['candle_interval'] = input(MESSAGES['candle_interval'])
    try:
        exchange.fetch_ohlcv(VARIABLES['ticker'], VARIABLES['candle_interval'], limit=500)
    except:
        print(MESSAGES['candle_interval_not_found'] % VARIABLES['candle_interval'])
        return

    #  6. Enter start_date
    if VARIABLES['start_date'] is None:
        VARIABLES['start_date'] = input(MESSAGES['start_date'])

    #  7. Enter end_date
    if VARIABLES['end_date'] is None:
        VARIABLES['end_date'] = input(MESSAGES['end_date'])






if __name__ == '__main__':
    setup()
    main()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Old code used as reference to create this file
#
# ticker = 'BTC/USDT'
#
# start_date = datetime(year=2018, month=2, day=10, hour=22)
# df = []
#
# while start_date < datetime(year=2020, month=1, day=1, hour=1):
#     data = binance.fetch_ohlcv(ticker, '1h', limit=500, since=int(time.mktime(start_date.timetuple())*1000))
#     df.extend(data)
#
#     # fetching last date to
#     data = np.array(data)
#     last_date = datetime.fromtimestamp(data[-1, 0]/1000)
#     start_date = last_date + timedelta(hours=1)
#
#     time.sleep(.1)
#
# df = pd.DataFrame(df, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
# df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(x/1000))
#
# df.to_csv(f'binance/{ticker.replace("/", "-")}.csv', index=False)
