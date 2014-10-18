#coding:utf-8
#!/usr/bin/python2.7

"""登录GDUT学生工作管理系统

    login:登录类，接收学好，密码
"""
__authors__ = [
    '"Yannyezixin" <646840080@qq.com>'
]

import urllib2
import urllib
import cookielib
import re

class login(object):
    """登录GDUT学生工作信息管理系统

    使用：接收用户名，密码。再通过属性
        result可获得登录后的结果

    Attributes:
        loginUrl: 登录URL
        name: 用户名
        password: 用户密码
        html: 获取登录URL页面的HTML
        result: 登录后的结果
    """

    def __init__(self, username, password):
        self.loginUrl = 'http://eswis.gdut.edu.cn/default.aspx'
        self.name = username
        self.password = password
        self.html = self.getHtml(self.loginUrl)
        if self.html != None:
            self.result = self.login(self.html)
        else:
            self.result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def getHtml(self, url):
        """获取给定URL的HTML"""

        try:
            print '获取页面中'
            req = urllib2.Request(url)
            html = urllib2.urlopen(req, timeout=5).read()
            return html
        except urllib2.URLError, e:
            print e
            return None

    def getExtraPostData(self, html):
        """获取给定HTML的Hidden表单字段

        Returns:
            返回Hidden表单字段列表
        """

        filtHiddenForm = re.compile(r'input.*hid.*ue="(.*?)"')
        result = filtHiddenForm.findall(html)

        return result

    def login(self, html):
        """登录

        Args:
            hiddenPostData: 隐藏表单字段列表
            cookie: 登录URL页面COOKIE
            header: http头
            postdata: 表单

        Returns:
            如果登录成功则返回登录后的HTML，否则返回None
        """
        hiddenPostData = self.getExtraPostData(html)
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        headers = {
                    'POST': 'http://eswis.gdut.edu.cn/default.aspx',
                    'Host': 'eswis.gdut.edu.cn',
                    'Referer': 'http://eswis.gdut.edu.cn/',
                    'Cookie': 'ASP.NET_SessionId=v2aba03ra5j3dvrrmo2dnq45',
                    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                    }
        postdata = urllib.urlencode({
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': hiddenPostData[0],
            'ctl00$dft_page$log_username': self.name,
            'ctl00$dft_page$log_password': self.password,
            'ctl00$dft_page$logon': '',
            '__PREVIOUSPAGE': hiddenPostData[1],
            '__EVENTVALIDATION': hiddenPostData[2]
            })
        req = urllib2.Request(
            url = self.loginUrl,
            data = postdata,
            headers = headers
            )

        try:
            print '登录中'
            result = opener.open(req).read()
            return result
        except urllib2.URLError, e:
            print e
            return None
