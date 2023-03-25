import requests
import pandas as pd

class CoinGeckoAPI:
    def __init__(self, base_url='https://api.coingecko.com/api/v3/'):
        self.base_url = base_url

    def get_price_current(self, coin_id):
        url = f"{self.base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        response_json = response.json()
        price = response_json[coin_id]['usd']
        return price

    def get_volume_current(self, coin_id):
        url = f"{self.base_url}/coins/{coin_id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
        response = requests.get(url)
        response_json = response.json()
        volume = response_json['market_data']['total_volume']['usd']
        return volume

    def get_marketcap_current(self, coin_id):
        url = f"{self.base_url}/coins/{coin_id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"
        response = requests.get(url)
        response_json = response.json()
        market_cap = response_json['market_data']['market_cap']['usd']
        return market_cap

    def coins(self):
        coin_list=[]
        url = f"{self.base_url}/coins/list"
        response = requests.get(url)
        response_json = response.json()
        # for data in response_json:
        #     coin_list.append(data['id'])
        coin_list=[data['id'] for data in response_json]
        return coin_list

    def all_price_data_daily(self,coin_id,days='max'):
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

    def all_marketcap_data_daily(self,coin_id,days='max'):
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

    def all_volume_data_daily(self,coin_id,days='max'):
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



    def pvmc_daily(self,coin_id,days='max'):
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

    def historical_data(self,coin_id,date):
        return something
