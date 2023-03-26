# CoinGeckoAPI

The `CoinGeckoAPI` class provides a simple interface for accessing cryptocurrency prices from the CoinGecko API.

## Initialization

To create a new instance of the `CoinGeckoAPI` class, you can optionally specify the `base_url` parameter. If not specified, the default base URL is `https://api.coingecko.com/api/v3/`.

```
api = CoinGeckoAPI(base_url='https://api.coingecko.com/api/v3/)
```
## Methods

`get_price_current(coin_id)`
This method retrieves the current price of a cryptocurrency based on its `coin_id`.
get_volume_current and get_marketcap_current are similar and accepts the same Parameters

```Parameters
coin_id (str): The ID of the cryptocurrency, as defined by CoinGecko.
Returns The current price of the cryptocurrency in USD (float).
```
`get_coins()`
This method retrieves list of coins on coingecko on current date

```Parameters
This method do not need any Parameters
```
`all_price_data_daily(self,coin_id,days='max'`
This method retrieves price data for a particular coin based on its `coin_id` and `days`.
days is max by default and both the parameters are `str`.
`all_volume_data_daily` and `all_marketcap_data_daily` does the same for volume and marketcap respectively.
