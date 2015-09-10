#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from HTTPClient import HTTPClient
import time,datetime
millis = time.time() * 1000
dateFile = datetime.datetime.now().strftime("%Y-%m-%d")
host = 'www.jisilu.cn'
filePath = "/home/web/ben/index_fund_crawler/data/"
fundAPath = '/data/sfnew/funda_list/?___t=' + str(int(millis))
fundBPath = '/data/sfnew/fundb_list/?___t=' + str(int(millis))
fundMPath = '/data/sfnew/fundm_list/?___t=' + str(int(millis))
client = HTTPClient(host)
funda = client.get(fundAPath)
file_object = open(filePath + 'funda_' + dateFile + '.json', 'w')
file_object.write(str(funda))
file_object.close()
fundb = client.get(fundBPath)
file_object = open(filePath + 'fundb_' + dateFile + '.json', 'w')
file_object.write(str(fundb))
file_object.close()
fundm = client.get(fundMPath)
file_object = open(filePath + 'fundm_' + dateFile + '.json', 'w')
file_object.write(str(fundm))
file_object.close()
