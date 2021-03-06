'''
Created on Jan 20, 2012

@author: ppa
'''

# config constant


CONF_APP_MAIN = 'app_main'

BUY = 'buy'
SELL_SHORT = 'sell_short'
SELL = 'sell'
BUY_TO_COVER = 'buy_to_cover'

CONF_ANALYZER_SECTION = 'analyzer'
CONF_TRADE_TYPE = 'backtest.tradetype'
CONF_SYMBOL_FILE = 'backtest.symbolfile'
CONF_INDEX = 'backtest.index'
CONF_INIT_CASH = "backtest.initcash"
CONF_DAM = 'backtest.dam'
CONF_STRATEGY_NAME = 'backtest.strategy_name'
CONF_START_TRADE_DATE = 'backtest.start_trade_date'
CONF_END_TRADE_DATE = 'backtest.end_trade_date'
CONF_BUYING_RATIO = 'backtest.buying_ratio'

# period strategy
CONF_STRATEGY_PERIOD = 'backtest.strategy.period'

# app global
TICK = 'tick'
QUOTE = 'quote'
TRADE_TYPE = 'tradetype'
STOP_FLAG = "stopFlag"

# EVENT LIST
EVENT_TICK_UPDATE = 'tickUpdate'
EVENT_ORDER_EXECUTED = "orderExecuted"

# state saver
STATE_SAVER_ACCOUNT = "account"
STATE_SAVER_HOLDING_VALUE = "holdingValue"
STATE_SAVER_INDEX_PRICE = "indexPrice"
STATE_SAVER_UPDATED_ORDERS = "updatedOrders"
STATE_SAVER_PLACED_ORDERS = "placedOrders"
STATE_SAVER_METRICS_START_DATE = "startDate"
STATE_SAVER_METRICS_END_DATE = "endDate"
STATE_SAVER_METRICS_LOWEST_VALUE = "lowestValue"
STATE_SAVER_METRICS_HIGHEST_VALUE = "highestValue"
STATE_SAVER_METRICS_SHARPE_RATIO = "sharpeRatio"
STATE_SAVER_METRICS_MAX_DRAW_DOWN = "maxDrawDown"
STATE_SAVER_METRICS_R_SQUARED = "rSquared"
