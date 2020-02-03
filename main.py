from datetime import datetime, timedelta
import time
import ccxt
import yaml

# Open config file
with open('config.yaml', 'r') as myfile:
    config = yaml.load(myfile, Loader=yaml.Loader)

    messages = {}

    messages['EXCHANGE'] = config['MESSAGES']['message_1']
    messages['exchange_not_found'] = config['MESSAGES']['message_1_error_handler']

    messages['API_PUBLIC_KEY'] = config['MESSAGES']['message_2']

    messages['API_PRIVATE_KEY'] = config['MESSAGES']['message_3']

    messages['CANDLE_INTERVAL'] = config['MESSAGES']['message_4']


# Run main()

def main():

    # 1. Get name of exchange to pull data from and make sure exchange exists
    exchange_str = input(messages['EXCHANGE'])
    try:
        exchange = getattr(ccxt, exchange_str.lower())
    except:
        print(messages['exchange_not_found'].format(exchange_str))
        return

    #  2. Add API key if needed
    API_PUBLIC_KEY = input(messages['API_PUBLIC_KEY'])
    #  3. Add API secret if needed
    API_PRIVATE_KEY = input(messages['API_PRIVATE_KEY'])

    #   4. Get candle_interval
    CANDLE_INTERVAL = input(messages['CANDLE_INTERVAL'])






if __name__ == '__main__':
    main()

    print('\nDone')


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
