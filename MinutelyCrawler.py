#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from HTTPClient import HTTPClient
import time,datetime,os,Persist

millis = time.time() * 1000
dateFile = datetime.datetime.now().strftime("%Y-%m-%d")
filePath = "D:/index_fund/" + dateFile + "/" # FIXME change it
if not os.path.exists(filePath): os.makedirs(filePath)
minuteFile = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
host = 'www.jisilu.cn'
fundAPath = '/data/sfnew/funda_list/?___t=' + str(int(millis))
fundBPath = '/data/sfnew/fundb_list/?___t=' + str(int(millis))
fundMPath = '/data/sfnew/fundm_list/?___t=' + str(int(millis))
client = HTTPClient(host)
funda = client.get(fundAPath)
filePathName = filePath + 'funda_' + minuteFile + '.json'
Persist.saveData2File(funda, filePathName)
fundb = client.get(fundBPath)
filePathName = filePath + 'fundb_' + minuteFile + '.json'
Persist.saveData2File(fundb, filePathName)
fundm = client.get(fundMPath)
filePathName = filePath + 'fundm_' + minuteFile + '.json'
Persist.saveData2File(fundm, filePathName)
