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
Returns
The current price of the cryptocurrency in USD (float).
```
