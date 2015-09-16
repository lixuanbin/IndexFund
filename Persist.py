#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'lixuanbin'
def saveData2File(data, filePathName):
    print filePathName
    file_object = open(filePathName, 'w')
    file_object.write(str(data))
    file_object.close()
