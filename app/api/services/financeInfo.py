# import yfinance as YF
import logging
import yahooquery as YQ
from ..utils import request

LOGGER = logging.getLogger("services.financeInfo")

class StockInfo:
    def __init__(self, stock):
        self.stock = stock
        # self.ticker = YF.Ticker(stock)
        self.tickerYQ = YQ.Ticker(stock, formatted=True)

    def getStockInfo(self):
        try:
            return dict(self.tickerYQ.asset_profile[self.stock], **self.tickerYQ.summary_detail[self.stock])

        except:
            LOGGER.exception("Error getting stock information")
            return None

    # def getStockDividends(self):
    #     try:
    #         return {
    #             "dividends": self.ticker.dividends,
    #         }

    #     except:
    #         LOGGER.exception("Error getting dividends")
    #         return None
    
    # def getStockNews(self):
    #     try:
    #         return {
    #             "news": self.ticker.news,
    #         }
        
    #     except:
    #         LOGGER.exception("Error getting stock news")
    #         return None
    
    # def getFinanceChart(self):
    #     try:
    #         return request.get("/v8/finance/chart/" + self.stock)
    #     except:
    #         LOGGER.exception("Error getting finace chart")
    #         return None

    # def getQuarterlyBalance(self):
    #     try:
    #         df = self.ticker.quarterly_balance_sheet
    #         return {
    #             "balance": df.dropna(), #removing NaN columns
    #         }

    #     except:
    #         LOGGER.exception("Error getting balance sheet")
    #         return None

    # def getEvents(self):
    #     try:
    #         return {
    #             "events": self.ticker.calendar,
    #         }

    #     except:
    #         LOGGER.exception("Error getting stock events")
    #         return None
    
    def getQuote(self):
        try:
            return request.get("/v6/finance/quote", {"symbols":self.stock})

        except:
            LOGGER.exception("Error getting stock quote")
            return None
    
    def getHistoricalPrices(self, interval, range):
        try:
            return request.get("/v8/finance/spark", {"symbols":self.stock, "interval": interval, "range": range})

        except:
            LOGGER.exception("Error getting historical prices")
            return None


