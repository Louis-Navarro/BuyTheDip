# Should you buy the dip?

## Table of Contents

- [Introduction](#introduction)
- [Strategies](#strategies)
  - [Dollar Cost Averaging (DCA)](#dollar-cost-averaging-dca)
  - [Only Buying The Dip (OBTD)](#only-buying-the-dip-obtd)
  - [Combining Dollar Cost Averaging and Buying The Dip (DCA+BTD)](#combining-dollar-cost-averaging-and-buying-the-dip-dcabtd)
- [Results](#results)

## Introduction

In this repository, we backtest a "buying the dip" (BTD) strategy to determine whether long term investors benefit from buying the dip. We compare buying the dip to Dollar Cost Averaging (DCA), another very common investment strategy among long-term retail investors.

The motivation behind this backtest, is that theoretically, there should be almost no advantage to buying the dip. If the stock market is at least weakly efficient, the movement of a stock's price stems from new public information. Therefore, the return of a stock with or without a dip should be the same, assuming the dip does not have an important impact on future public information.

On the other hand, we can also expect institutional investors to overreact to negative news, or miss important nuance published later, meaning the price of the stock will be adjusted in the following days. Hence backtesting both a BTD and a DCA strategy gives insight into how efficient the market is, and if buying the dip is useful for long-term, mostly passive investors.

## Strategies

### Dollar Cost Averaging (DCA)

DCA is a very common strategy among long-term passive investors. The idea is to invest a fix amount of cash into an asset at regular intervals, independently on the market's movement. For example, an investor could commit to invest $100 into the S&P500 at the end of every month.

This strategy smooths out the gains and the losses. As it name implies, it averages out the average buying price of the stock, decreasing volatility, and hence risk, of the investor's position.

### Only Buying The Dip (OBTD)

To measure the effetiveness of buying the dip, we first develop a strategy where we only buy a stock whenever it dips. We define a _dip_ in the stock when the daily log return falls below the $2\sigma$ range for the daily log returns.

Specifically, given daily stock prices $p_0, p_1, ..., p_n$, we calculate the log return: $r_i = \log(\frac{p_i}{p_{i-1}})$ for all $i \ge 1$.

The mean of the log return is given by:

$$\bar r = \frac{1}{n}\sum\limits_{i=1}^n{r_i}$$

And the standard deviation of the log return is defined as:

$$\sigma = \sqrt{\frac{1}{n}\sum\limits_{i=1}^n{(r_i-\bar r)^2}}$$

We then create a sequence of days $d_1, d_2, ..., d_m$ of log losses outside the $2\sigma$ range, in other words, $r_{d_i} < \bar r - 2\sigma$ for $1\le i \le m$

The OBTD strategy consists of investing $100 into the asset on the dip days $d_1, d_2, ..., d_m$

### Combining Dollar Cost Averaging and Buying The Dip (DCA+BTD)

To test a more realistic strategy in which the investor buys every dip, we backtest a strategy that mixes DCA with BTD. Indeed, long-term investments don't necessarily wait for a dip, but rather invest in a stock, and simply invest a higher amount when a dip occurs.

For this DCA+BTD strategy, we simply invest $10 into the asset every day, and an additional $10 on "dip days", as defined in the previous part

## Results

Results TBA soon
