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
        MESSAGES['exchange_not_found'] = config['MESSAGES']['message_1_error_handler']
        MESSAGES['api_public_key'] = _config['MESSAGES']['message_2']
        MESSAGES['api_private_key'] = _config['MESSAGES']['message_3']
        MESSAGES['candle_interval'] = _config['MESSAGES']['message_4']

        # Save all variables to VARIABLES
        VARIABLES['exchange'] = config['VARIABLES']['EXCHANGE']
        if VARIABLES['exchange'] is None:
            VARIABLES['exchange'] =














def main():
    pass
    # 1. Get name of exchange to pull data from and make sure exchange exists
    # # exchange_str = input(MESSAGES['exchange'])
    # try:
    #     exchange = getattr(ccxt, exchange_str.lower())
    # except:
    #     print(MESSAGES['exchange_not_found'] % exchange_str)
    #     return

    #  2. Add API key if needed
    # api_public_key = input(MESSAGES['api_public_key'])
    #  3. Add API api_private_keyret if api_private_key    # API_PRIVATE_KEY = input(MESSAGES['API_PRIVATE_KEY'])

    #   4. Get candle_interval
    # candle_interval = input(MESSAGES['candle_interval'])






if __name__ == '__main__':
    setup()
    main()


'''
To-Do
- [ ] Display all candle interval options
- [ ] Input of a specific start date
'''

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
