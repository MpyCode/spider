# -*- coding:utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, newUrl, htmlCont):
        if newUrl is None or htmlCont is None:
            return
        soup = BeautifulSoup(htmlCont,'html.parser',from_encoding='utf-8')
        newUrls = self._getNewUrls(newUrl,soup)
        newData = self._getNewData(newUrl,soup)
        return newUrls,newData

    def _getNewUrls(self, newUrl, soup):
        newUrls = set()
        
        links = soup.find_all('a',href=re.compile(r"\w.+/$"))
        for link in links:
            newLink = link['href']
            newFullLink=urlparse.urljoin(newUrl,newLink)
            newUrls.add(newFullLink)
        return newUrls

    def _getNewData(self, newUrl, soup):
        resData = set()

        newUrls=soup.find_all('a',href=re.compile(r".+(rpm|gz|deb|html)$"))
        for link in newUrls:
            newlink=link['href']
            newlink=urlparse.urljoin(newUrl,newlink)
            resData.add(newlink)

        return resData
