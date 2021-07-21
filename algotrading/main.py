import pandas as pd
from selenium import webdriver
import requests as rq
import xlsxwriter
import math
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request
import numpy as np

apple_url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
print(apple_url)
uClient = uReq(apple_url)
result_html = uClient.read()
uClient.close()

page_soup = soup(result_html, "html.parser")
print(page_soup)
result = page_soup.findAll("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
print(result)
# target span is <span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)" data-reactid="33">+0.51 (
# +0.39%)</span>


