# Python Finance

Python projects and coursework for quantitative finance — data analysis, statistical modeling, and financial backtesting.

## Contents

`pandas-course/` — Kaggle Pandas course exercises and notes

`data-viz-course/` — Kaggle Data Visualization exercises and notes

`projects/` — Quantitative finance projects

## Projects

**Pairs Trading Analysis** (`projects/pairs_trading.ipynb`)

A quantitative investigation into statistical arbitrage using the Engle-Granger cointegration test across multiple asset pairs. Tested NVDA/AMD and GLD/SLV - both failed to show significant cointegration. Found a cointegrated pair in KO/PEP (p-value: 0.0095 over 2015-2024) and built a full backtested strategy using log prices, OLS hedge ratio estimation, and z-score signal generation. The strategy returned +0.50 cumulative log returns with a Sharpe of 0.44 and max drawdown of -0.17.

## Stack

- Python 3.x
- pandas, numpy, matplotlib, seaborn
- statsmodels, yfinance

## About

Built over Summer 2026 as part of a self-directed curriculum toward quantitative 
research in finance. Currently a mathematics major at The Ohio State University.

