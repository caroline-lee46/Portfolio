# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:02 2016

@author: james.bradley
"""
#import the scraping package
import requests
from lxml import objectify

#make it easy to change the url in the future
num_periods = 6
parameter = 'tavg'
div = 0
state_id = 44
num_month = 8
year = '2016'
template_base = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?'
template_add = 'parameter=%s&state=%s&div=%s&month=%s&periods[]=%s&year=%s'
insert_these = (parameter,state_id,div, num_month, num_periods, year)
template_add = template_add % insert_these
url = template_base + template_add

#scrape the data
response = requests.get(url).content
root = objectify.fromstring(response)

#print the results (desired variables)
my_wm_username = 'cljones01'

print my_wm_username
print root['data']["value"]
print root['data']["twentiethCenturyMean"]
print root['data']["lowRank"]
print root['data']["highRank"]
