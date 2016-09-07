#!/usr/bin/python

# Import everything I might need
import os
import objc
import time
from tqdm import tqdm
import urllib
import requests
import webbrowser
from lxml import etree
from bs4 import BeautifulSoup
import feedparser

# List of URLs for RSS feeds I want
url_list = []

# CNN
url_list.append('http://rss.cnn.com/rss/cnn_topstories.rss')
url_list.append('http://rss.cnn.com/rss/money_latest.rss')
url_list.append('http://rss.cnn.com/rss/cnn_tech.rss')

# CNBC
url_list.append('http://www.cnbc.com/id/100003114/device/rss/rss')
url_list.append('http://www.cnbc.com/id/10001147/device/rss/rss')
url_list.append('http://www.cnbc.com/id/19854910/device/rss/rss')

# Misc news
url_list.append('http://feeds.nytimes.com/nyt/rss/Technology')
url_list.append('http://feeds.reuters.com/reuters/technologyNews')
url_list.append('http://www.wsj.com/xml/rss/3_7455.xml')
url_list.append('http://www.forbes.com/businesstech/index.xml')
url_list.append('http://www.marketwatch.com/rss/topstories')
url_list.append('http://investorplace.com/category/stock-picks/stocks-to-buy/feed/')
url_list.append('http://finance.yahoo.com/rss/topstories')

# Tech specific
url_list.append('http://feeds.feedburner.com/TechCrunch/')
url_list.append('http://www.computerweekly.com/rss/All-Computer-Weekly-content.xml')
url_list.append('http://www.infoworld.com/index.rss')
url_list.append('http://www.computerworld.com/index.rss')
url_list.append('http://www.techtimes.com/rss/archives/all.xml')



# List of microchip manufacturers
chip_companies = ['Agere', 'Agilent', 'Alcatel', 'Altera', 'AMD', \
                    'Analog Devices', 'Applied Materials', 'ARM', \
                    'ATI Technologies', 'Atmel', 'ams AG', 'Allegro MicroSystems' \
                    'Broadcom', 'Commodore Semiconductor', 'CML Microcircuits' \
                    'CSR plc', 'Cypress Semiconductor', 'Dallas Semiconductor' \
                    'Fairchild Semiconductor', 'Ferranti Computer', \
                    'Freescale Semiconductor', 'Fujitsu', 'Genesis Microchip', \
                    'GlobalFoundries', 'GMT Microelectronics', 'Hitachi, Ltd.', \
                    'Horizon Semiconductors', 'HP jet', 'IBM', 'Infineon Technologies', \
                    'Integrated Device Technology', 'Intel', 'Intersil', 'Jennic Limited', \
                    'Lattice Semiconductor', 'Linear Technology', 'LSI Logic', \
                    'LSI Computer Systems', 'Maxim Integrated Products', \
                    'Marvell Technology', 'Microchip Technology', 'Micron Semiconductor', \
                    'MicroSystems International', 'MOS Technology', 'Mostek', \
                    'National Semiconductor', 'Nordic Semiconductor', 'Novellus', \
                    'Nvidia', 'NXP Semiconductors', 'ON Semiconductor', 'Parallax', \
                    'Plessey', 'PMC-Sierra', 'Renesas Technology', 'Rohm', 'Realtech', \
                    'Samsung', 'Sondrel', 'STMicroelectronics', 'System to ASIC', \
                    'Texas Instruments', 'Toshiba', 'TSMC', 'Triad Semiconductor', \
                    'u-blox', 'Verdi Semiconductor', 'VIA Technologies', \
                    'Volterra Semiconductor', 'Wolfson Microelectronics', 'Xilinx', \
                    'XMOS', 'ZiLOG']

# Loop through and search all feeds
post_num = 0
feed_hit = 0
for url in url_list:

    # Get current RSS feed
    current = feedparser.parse(url)
    #print current
    for post in current.entries:
        for company in chip_companies:
            if company in post.title:
                post_num += 1
                if feed_hit == 0:
                    print ('-----------------------------------------')
                    print url
                    print ('-----------------------------------------')
                    feed_hit = 1
                print post_num, ' ', post.title

    # Reset feed_hit
    feed_hit = 0
