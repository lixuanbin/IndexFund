#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import httplib

REMOTE_SERVER_HOST = "www.csair.com"
REMOTE_SERVER_PATH = "/"

class HTTPClient:
    def __init__(self, host):
        self.host = host
    def fetch(self, path):
        http = httplib.HTTP(self.host)

        http.putrequest("GET", path)
        http.putheader("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0")
        http.putheader("Accept", "*/*")
        http.endheaders()

        try:
            errcode, errmsg, headers = http.getreply()
        except Exception, e:
            print "Client failed error code: %s message: %s headers: %s" % (errcode, errmsg, headers)
        else:
            print "Got page from %s" % self.host
        file = http.getfile()
        return file.read()
    def get(self, path):
        try:
            httpClient = httplib.HTTPConnection(self.host, 80, timeout=30)
            httpClient.request('GET', path)
            response = httpClient.getresponse()
            print response.status
            print response.reason
            return response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Client Example")
    parser.add_argument("--host", action="store", dest="host", default=REMOTE_SERVER_HOST)
    parser.add_argument("--path", action="store", dest="path", default=REMOTE_SERVER_PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print client.get(path)
