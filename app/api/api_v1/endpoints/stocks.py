from fastapi import APIRouter
from ...services.financeInfo import StockInfo

V1 = APIRouter()

@V1.get("/summary/{stock}")
def read_root(stock: str):
    stockInfo = StockInfo(stock)
    return stockInfo.getStockInfo()

@V1.get("/dividends/{stock}")
def read_root(stock: str):
    stockInfo = StockInfo(stock)
    return stockInfo.getStockDividends()

@V1.get("/news/{stock}")
def read_root(stock: str):
    stockInfo = StockInfo(stock)
    return stockInfo.getStockNews()

@V1.get("/chart/{stock}")
def read_root(stock: str):
    stockInfo = StockInfo(stock)
    return stockInfo.getFinanceChart()

@V1.get("/quote/{stock}")
def read_root(stock: str):
    stockInfo = StockInfo(stock)
    return stockInfo.getQuote()

@V1.get("/historical-prices/{stock}")
def read_root(stock: str, interval: str = "1d", range: str = "1mo"):
    stockInfo = StockInfo(stock)
    return stockInfo.getHistoricalPrices(interval, range)