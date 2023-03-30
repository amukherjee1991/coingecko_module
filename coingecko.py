import requests
import pandas as pd

class CoinGeckoAPI:
    def __init__(self, base_url='https://api.coingecko.com/api/v3/'):
        self.base_url = base_url

    '''
    This function gets current_price
    :para param1: coin_id
    :type param1: str
    '''
    def get_price_current(self, coin_id):
        if not isinstance(coin_id, str):
            raise TypeError("coin_id must be a string")
        url = f"{self.base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        response_json = response.json()
        price = response_json[coin_id]['usd']
        return price
    '''
    This function gets current_volume
    :para param1: coin_id
    :type param1: str
    '''
    def get_volume_current(self, coin_id):
        if not isinstance(coin_id, str):
            raise TypeError("coin_id must be a string")
        url = f"{self.base_url}/coins/{coin_id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
        response = requests.get(url)
        response_json = response.json()
        volume = response_json['market_data']['total_volume']['usd']
        return volume
    '''
    This function gets current_marketcap
    :para param1: coin_id
    :type param1: str
    '''
    def get_marketcap_current(self, coin_id):
        if not isinstance(coin_id, str):
            raise TypeError("coin_id must be a string")
        url = f"{self.base_url}/coins/{coin_id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
        response = requests.get(url)
        response_json = response.json()
        market_cap = response_json['market_data']['market_cap']['usd']
        return market_cap

    '''
    This function gets list of all coins on coingecko
    '''
    def coins(self):
        coin_list=[]
        url = f"{self.base_url}/coins/list"
        response = requests.get(url)
        response_json = response.json()
        # for data in response_json:
        #     coin_list.append(data['id'])
        coin_list=[data['id'] for data in response_json]
        return coin_list

    '''
    This function gets all prices based on parameter
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :default param2: max
    '''
    def all_price_data_daily(self,coin_id,days='max'):
        if not isinstance(days, str) or not isinstance(days, str):
            raise TypeError("coin_id and days must be a string")
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"
        response = requests.get(url)
        response_json = response.json()
        all_prices=[]
        for p in response_json['prices']:
        	prices=[]
        	prices.append(coin_id)
        	prices.append(p[0])
        	prices.append(p[1])
        	all_prices.append(prices)
        return all_prices

    '''
    This function gets all marketcap based on parameter
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :default param2: max
    '''
    def all_marketcap_data_daily(self,coin_id,days='max'):
        if not isinstance(days, str) or not isinstance(days, str):
            raise TypeError("coin_id and days must be a string")
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"
        response = requests.get(url)
        response_json = response.json()
        all_marketcap=[]
        for p in response_json['market_caps']:
        	marketcap=[]
        	marketcap.append(coin_id)
        	marketcap.append(p[0])
        	marketcap.append(p[1])
        	all_marketcap.append(marketcap)
        return all_marketcap
    '''
    This function gets all volume based on parameter
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :default param2: max
    '''
    def all_volume_data_daily(self,coin_id,days='max'):
        if not isinstance(days, str) or not isinstance(days, str):
            raise TypeError("coin_id and days must be a string")
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"
        response = requests.get(url)
        response_json = response.json()
        all_volume=[]
        for p in response_json['total_volumes']:
        	volume=[]
        	volume.append(coin_id)
        	volume.append(p[0])
        	volume.append(p[1])
        	# print(prices)
        	all_volume.append(volume)
        return all_volume

    '''
    This function gets all price,volume and marketcap based on parameter
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :default param2: max
    :returns data as a pandas df
    '''

    def pvmc_daily(self,coin_id,days='max'):
        if not isinstance(days, str) or not isinstance(days, str):
            raise TypeError("coin_id and days must be a string")
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"
        response = requests.get(url)
        response_json = response.json()
        all_marketcap=[]
        for p in response_json['market_caps']:
        	marketcap=[]
        	marketcap.append(coin_id)
        	marketcap.append(p[0])
        	marketcap.append(p[1])
        	all_marketcap.append(marketcap)
        all_volume=[]
        for p in response_json['total_volumes']:
        	marketcap=[]
        	marketcap.append(coin_id)
        	marketcap.append(p[0])
        	marketcap.append(p[1])
        	all_volume.append(marketcap)
        all_prices=[]
        for p in response_json['prices']:
        	marketcap=[]
        	marketcap.append(coin_id)
        	marketcap.append(p[0])
        	marketcap.append(p[1])
        	all_prices.append(marketcap)
        df1 = pd.DataFrame(all_prices, columns=['coin', 'ts', 'price'])
        df2 = pd.DataFrame(all_volume, columns=['coin', 'ts', 'volume'])
        df3 = pd.DataFrame(all_marketcap, columns=['coin', 'ts', 'market_cap'])
        merged_df = pd.merge(pd.merge(df1, df2, on=['coin', 'ts']), df3, on=['coin', 'ts'])
        return merged_df

    '''
    candles body:
    1 - 2 days: 30 minutes
    3 - 30 days: 4 hours
    31 days and beyond: 4 days
    arguments accepted are 1,7,14,30,90,180,365,max

    This function gets OHLC based on parameter
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :para param3: curr
    :type param3: str
    :default param3: usd
    :returns data as a pandas df

    '''
    def ohlc(self,coin_id,days='max',curr='usd'):
        if not isinstance(days, str) or not isinstance(days, str):
            raise TypeError("coin_id and days must be a string")
        url = f"{self.base_url}/coins/{coin_id}/ohlc?vs_currency={curr}&days={days}"
        response = requests.get(url)
        response_json = response.json()
        df1 = pd.DataFrame(response_json, columns=['ts', 'open', 'high','low','close'])
        return df1

    '''
    This function gets historical data based on coin_id and date
    :para param1: coin_id
    :type param1: str
    :para param2: days
    :type param2: str
    :default param2: max
    :returns a list (history_data)
    :date format DD-MM-YYYY

    '''
    def historical_data(self,coin_id,date):
        if not isinstance(coin_id, str) or not isinstance(date, str):
            raise TypeError("coin_id and date must be a string")
        url = f"{self.base_url}/coins/{coin_id}/history?date={date}"
        response = requests.get(url)
        response_json = response.json()
        history_data=[]
        for k,v in response_json.items():
            try:

                price_data=[response_json['market_data']['current_price'] for k,v in response_json.items()]
                hist_price=price_data[0]['usd']
                volume_data=[response_json['market_data']['total_volume'] for k,v in response_json.items()]
                hist_volume=volume_data[0]['usd']
                mc_data=[response_json['market_data']['market_cap'] for k,v in response_json.items()]
                hist_mc=mc_data[0]['usd']
                community_data=[response_json['community_data'] for k,v in response_json.items()][0]

                history_data.append(hist_price)
                history_data.append(hist_volume)
                history_data.append(hist_mc)
                history_data.append(community_data['facebook_likes'])
                history_data.append(community_data['twitter_followers'])
                history_data.append(community_data['reddit_average_posts_48h'])
                history_data.append(community_data['reddit_average_comments_48h'])
                history_data.append(community_data['reddit_subscribers'])
                history_data.append(community_data['reddit_accounts_active_48h'])
            except KeyError:
                print('market_data do not exist')
                history_data=["","","","","","","","",""]

            return history_data
