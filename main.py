from scrapy.americanaScrapy import AmericanaScrapy, SaveScrapy
import pandas as pd
if __name__ == "__main__":

    americanas = AmericanaScrapy()
    americanas.scrapy()
    data = americanas.returnProdutos()
    americanas.quit()

    SaveScrapy(data)
