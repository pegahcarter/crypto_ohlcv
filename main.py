import ccxt


def main():

    # 1. Get name of exchange to pull data from
    input_exchange = input('Please enter exchange to pull OHLCV data from:  ')
    print('\n')
    try:
        exchange = getattr(ccxt, input_exchange.lower())
        #  1a. Add API key if needed

        #  1b. Add API secret if needed

    except AttributeError as e:
        return AttributeError(f'ERROR: Exchange  `{input_exchange}`  is not available.')
    else:
        # Continue on with input
        #   2. Get candle_interval
        input_interval = input('Please enter your candle interval as an abbreviation.  \nExamples:  "5m", "1h", "1d":  ')



if __name__ == '__main__':
    main()

    print('\nDone')



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
