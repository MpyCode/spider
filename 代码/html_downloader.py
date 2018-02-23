# -*- coding:utf-8 -*-

import urllib2

class HtmlDownload(object):
    def download(self, newUrl):
        if newUrl is None:
            return None
        read = "null"
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers={'User-Agent':user_agent}
            req=urllib2.Request(newUrl,None,headers)
            response = urllib2.urlopen(req)
            code = response.getcode()
            read = response.read()
            if code != 200:
                return None
        except Exception as err:
            print err.__str__()
        return read
