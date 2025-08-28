
import configparser
import pandas as pd
import numpy as np
from api import AlphaVantageAPI, TickerInterval

URL = "https://www.alphavantage.co/query"


def find_dips(close_prices: pd.Series, threshold_factor: int = 2) -> pd.Series:
    log_returns = np.log(close_prices).diff()

    mean = log_returns.mean()
    sigma = log_returns.std()

    threshold = mean - threshold_factor * sigma
    dips = log_returns < threshold

    return dips


def get_dca_buys(close_prices: pd.Series, invest_amount: float = 10) -> pd.Series:
    invested = close_prices - close_prices + invest_amount
    bought = invest_amount / close_prices
    return bought, invested


def get_dips_buys(close_prices: pd.Series, invest_amount: float = 10) -> pd.Series:
    dips = find_dips(close_prices)
    invested = close_prices[dips] - close_prices[dips] + invest_amount
    bought = invest_amount / close_prices[dips]
    return bought, invested


def get_portfolio_value(bought: pd.Series, close_prices: pd.Series) -> pd.Series:
    total_owned = bought.cumsum()
    total_value = total_owned * close_prices[total_owned.index]
    return total_value


def get_roi(total_value: pd.Series, invested: pd.Series) -> float:
    total_investment = invested.sum()
    last_value = total_value.iloc[-1]
    roi = (last_value - total_investment) / total_investment
    return roi


def main():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    API_KEY = config['AlphaVantage']['api_key']

    api = AlphaVantageAPI(API_KEY)

    ASSETS_TICKERS = [
        "MSFT",
        "HLN",
        "PSO",
        "SOS",
        "UL",
        "BRK.B",
    ]

    for ASSET_TICKER in ASSETS_TICKERS:
        print(f"--- Running analysis for: {ASSET_TICKER} ---")
        asset_data = api.fetch_ticker_data(
            ASSET_TICKER, interval=TickerInterval.DAILY)
        asset_data = asset_data[asset_data.index >= "2018-01-01"]
        close_prices = asset_data['Close']

        # Amount of stocks bought
        dca_buys, dca_invested = get_dca_buys(close_prices)
        dips_buys, dips_invested = get_dips_buys(close_prices)
        combined_buys = dca_buys.add(dips_buys, fill_value=0)
        combined_invested = dca_invested.add(dips_invested, fill_value=0)

        # Value of portfolios
        dca_value = get_portfolio_value(dca_buys, close_prices)
        dips_value = get_portfolio_value(dips_buys, close_prices)
        combined_value = get_portfolio_value(combined_buys, close_prices)

        # ROI
        dca_roi = get_roi(dca_value, dca_invested)
        dips_roi = get_roi(dips_value, dips_invested)
        combined_roi = get_roi(combined_value, combined_invested)

        print(f"DCA ROI: {dca_roi:.2%}")
        print(f"Dips ROI: {dips_roi:.2%}")
        print(f"Combined ROI: {combined_roi:.2%}")
        print("\n")


if __name__ == "__main__":
    main()
