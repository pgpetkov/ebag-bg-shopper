# Shopper: Automatic Shopping for Ebag Service

Shopper is a procedure for forecasting time series data.  It is based on an additive model where non-linear trends are fit with yearly and weekly seasonality, plus holidays. It works best with daily periodicity data with at least one year of historical data. Prophet is robust to missing data, shifts in the trend, and large outliers.


## Important links


- Homepage: https://github.com/pgpetkov/ebag-bg-shopper
- HTML documentation: https://github.com/pgpetkov/ebag-bg-shopper/docs/quick_start.html
- Issue tracker: https://github.com/pgpetkov/ebag-bg-shopper/issues
- Source code repository: https://github.com/pgpetkov/ebag-bg-shopper
- Python Selenium package: http://selenium-python.readthedocs.io/

## Installation

Prophet is on PyPI, so you can use pip to install it:

```
# bash
$ pip install ebag-shopper
```

The major dependency that shopper has is `selenium`.   Selenium has its own [installation instructions](http://selenium-python.readthedocs.io/).
But you will need to run `requirements.txt` as there are some other small dependencies.

After installation, you can [get started!](#)

## Changelog


### Version 0.1 (2018.04.11)

- Initial release