from selenium import webdriver
from datetime import datetime
import os
import pandas as pd
class AmericanaScrapy:
    def __init__(self):
        self.produtos = []
        self.drive = os.path.join(os.getcwd(), "chromedriver.exe")
        self.offset = 0
        self.webdriver = webdriver.Chrome(self.drive)
        self.url = f"https://www.americanas.com.br/busca/celular?limit=24&offset={self.offset}"
        self.max = 500
    def __str__(self):
        return self.produtos
    def returnProdutos(self):
        return self.produtos
    def scrapy(self):
        chrome = self.webdriver
        chrome.get(self.url)
        produtos = chrome.find_elements_by_css_selector(".col__StyledCol-sc-1snw5v3-0.epVkvq.src__ColGridItem-sc-122lblh-0.bvfSKS")
        for produto in produtos:
            try:
                titulo = produto.find_element_by_css_selector(".src__Text-sc-154pg0p-0.src__Name-sc-1k0ejj6-4.kpvRnK")
                preco = produto.find_element_by_css_selector(".src__Text-sc-154pg0p-0.src__PromotionalPrice-sc-1k0ejj6-8.gxxqGt")
                link = produto.find_element_by_css_selector(".src__Wrapper-sc-1k0ejj6-3.eflURh > a").get_attribute("href")
                self.produtos.append({
                    "titulo": titulo.text,
                    "preco": preco.text.replace("R$", ""),
                    "link": link
                })
            except Exception as erro:
                ScrapyErrosLog.save(str(erro) + "\n")
        if(self.offset < self.max):
            self.generateUrl()
            self.scrapy()
    def generateUrl(self):
        self.offset = self.offset + 24
        self.url = f"https://www.americanas.com.br/busca/celular?limit=24&offset={self.offset}"
        print(self.url)
    def quit(self):
        self.webdriver.quit()

class SaveScrapy:
    def __init__(self, data):
        name_data = "test"
        self.name = f"scrapy_result-{name_data}.xlsx"
        self.data = data
        self.save()
    def save(self):
        # excel file
        try:
            df = pd.DataFrame(self.data)
            writer = pd.ExcelWriter(self.name, engine="xlsxwriter")
            df.to_excel(writer)
            writer.save()
        except Exception as e:
            print(e)
            return False

class ScrapyErrosLog:
    @staticmethod
    def save(exception):
        with open("exceptions.txt", "a") as file:
            file.write(exception)