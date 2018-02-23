# -*- coding:utf-8 -*-

class UrlManager(object):

    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()


    def addNewUrl(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)



    def addNewUrls(self, newUrls):
        if newUrls is None or len(newUrls) == 0:
            return
        for url in newUrls:
            self.addNewUrl(url)


    def hasNewUrl(self):
        return len(self.newUrls) != 0


    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl

