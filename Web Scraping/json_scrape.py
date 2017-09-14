# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:43 2017

@author: jrbrad
"""

import requests
#port the data
my_wm_username = 'cljones01'
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season2015'
response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

jumpshot = []
for shot in response.json():
    if shot["ACTION_TYPE"] == "Jump Shot":
        jumpshot.append(shot["ACTION_TYPE"])
madeshot = []
for shot in response.json():
    if shot["ACTION_TYPE"] == "Jump Shot":
        if shot["EVENT_TYPE"]== "Made Shot":
            madeshot.append(shot["EVENT_TYPE"])
            
numJumpShotsAttempt = len(jumpshot)
numJumpShotsMade = len(madeshot)
percJumpShotMade = float(len(madeshot))/float(len(jumpshot))

# Write your program here to populate the appropriate variables
            
print my_wm_username
print numJumpShotsAttempt
print numJumpShotsMade
print percJumpShotMade
