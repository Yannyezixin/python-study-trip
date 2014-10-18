#coding:utf-8
#!/usr/bin/python2.7

"""获取代理IP

    getiplist: 获取代理IP
"""
__authors__ = [
    '"Yannyezixin" <646840080@qq.com>'
]

import urllib2
import re

class getiplist(object):
    """获取代理IP类

    Attributes:
        url: 解析HTML并获取IP的URL
    """

    url = 'http://www.56ads.com/article/7110.html'

    def __init__(self):
        print "获取代理IP中..."
        self.ipList = self.getIpList(self.getHtml())

    def getSelfIpList(self):
        return self.ipList

    def getHtml(self):
        """获取IP的HTML"""

        req = urllib2.Request(self.url)
        html = urllib2.urlopen(req).read()

        return html

    def getIpList(self, html):
        """过滤HTML，返回IP列表"""

        filtIp = re.compile(r'[^@](\d+\.\d+\.\d*.\d*:\d*)')
        ipList = filtIp.findall(html)

        return ipList
