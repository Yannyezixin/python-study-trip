#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import os
import threading
import Queue
import sys
from twisted.web.client import getPage
from twisted.internet import reactor
from random import choice


"""抓取GDUT学生工作信息管理系统学生头像爬虫
    @author: Yann
    @date: 2014.10.09-2014.10-10
    @summary: 学号的排序规则是: 男生起始为311, 女生为321
        入学年份：2011年则 100, 后四位则代表顺序
        ex: 2012年入学的男生 3112004586
            2013年入学的女生 3213004586
"""


class spliderGradeThread(threading.Thread):
    """下载图片类,继承threading.Thread,启用多线程
    """

    def __init__(self,name, queue, enrolYear, num, preNum, nextNum, ipList):
        """构造函数，传入七个参数

        Args:
            queue: 惯例
            enrolYear: 入学年份
            num: 随机数
            preNum: 下载起始数
            nextNum: 下载末尾数
            ipList: 代理IP列表
        """
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.enrolYear = enrolYear
        self.num = num
        self.preNum = preNum
        self.nextNum = nextNum
        self.ipList = ipList

    def run(self):
        """启动线程"""
        self.main(self.num)

    def main(self, num):
        """构造学好和下载链接，自身调用下载方法"""

        #相同的部分url
        urlhead = "http://gdutfile.eswis.cn/upfiles/" + num + "/userpic/"
        print "准备抓取图片中..."
        for i in range(self.preNum, self.nextNum):
            sno = self.getSno(i, self.enrolYear)
            url = urlhead + '201' + str(self.enrolYear) + "/" + '%s' % sno + '.jpg'
            storagePath = self.getStoragePath(self.enrolYear, sno + '.jpg')
            if self.checkImgUrlStatus(url, False):
                self.downloadImg(url, storagePath)
            else:
                self.replaceSnoUrlSto(sno, url, storagePath)

    def checkImgUrlStatus(self, url, second):
        """检查图片链接状态"""
        try:

            # TODO: 多线程下更好的方式开启代理IP
            """
            ip = choice(self.ipList)
            proxy_hander = urllib2.ProxyHandler({'http': 'http://' + ip})
            opener = urllib2.build_opener(proxy_hander)
            urllib2.install_opener(opener)
            """

            req = urllib2.Request(url)
            urllib2.urlopen(req)
            return True
        except urllib2.URLError, e:
            if second:
                if hasattr(e, 'code'):
                    print '线程：', self.getName(), '错误代码:', e.code, url
                elif hasattr(e, 'reason'):
                    print '线程：', self.getName(), '错误原因：', e.reason, url
            return False

    def downloadImg(self, url, storagePath):
        """下载图片"""

        try:
            urllib.urlretrieve(url, storagePath)
            print "成功下载：%s 的学生的头像" % url
        except:
            pass

    def replaceSnoUrlSto(self, stuSno, url, storagePath):
        """替换学号，URL，存储路径,重新下载"""

        boy = re.compile(r'boy')
        boySno = re.compile(r'/311')
        url = boySno.sub('/321', url)
        storagePath = boy.sub('girl', storagePath)

        # 重新下载
        if self.checkImgUrlStatus(url, True):
            self.downloadImg(url, storagePath)


    def getSno(self, i, enrolYear):
        """构造学号函数"""

        strNum = str(i)
        length = len(strNum)
        if length == 4:
            num = strNum
        else:
            num = '0' * (4 - length) + strNum

        return '311' + str(enrolYear) + '00' + num

    def getStoragePath(self, enrolYear, filename):
        """获取存储路径"""

        dest_dir = './img/boy/201' + str(enrolYear) + '/' + filename

        return dest_dir

class Login(object):
    """登录类，获取随机数

    Attributes:
        loginUrl: 登录URL
        name: 用户名
        password: 用户密码
        html: 获取登录URL页面的HTML
    """

    loginUrl = 'http://eswis.gdut.edu.cn/default.aspx'
    name = 'your-sno'
    password = 'your-password'
    html = None

    def __init__(self):
        self.html = self.getHtml(self.loginUrl)

    def getSelfHtml(self):
        """返回属性html"""

        return self.html

    def getHtml(self, url):
        """获取给定URL的HTML"""

        try:
            req = urllib2.Request(url)
            html = urllib2.urlopen(req, timeout = 5).read()
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
            result = opener.open(req).read()
            return result
        except urllib2.URLError, e:
            print e
            return None

class getProxyIp(object):
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

def getImgUrlNum(html):
    """接收登录后HTML过滤出随机数

    Returns:
        返回随机数
    """
    filtImgUrl = re.compile(r'img.*?upfiles\/(\d*)')
    number = filtImgUrl.findall(html)

    return number[0]


def initDir():
    """目录初始化函数"""

    #目录结构为
    # img/boy/2011
    #        /2012
    #        /2013
    #        /2014
    #   /girl/2011
    #        /2012
    #        /2013
    #        /2014

    directory = './img/'
    boyDir = directory + 'boy/'
    girlDir = directory + 'girl/'
    if not os.path.exists(directory):
        print '目录初始化中...'
        os.mkdir(directory)
        os.mkdir(boyDir)
        os.mkdir(girlDir)
        for i in range(2011,2015):
            os.mkdir(boyDir + str(i))
            os.mkdir(girlDir + str(i))

if __name__ == '__main__':

    while True:
        login = Login()
        html = login.getSelfHtml()

        if html == None:
            print "获取页面超时, 重新获取中..."
        else:
            print "正在登录中..."
            break

    while True:
        result = login.login(html)
        if result == None:
            print "登陆超时, 重新登录中..."
        else:
            print "登录成功"
            break

    #获取代理ip
    ip = getProxyIp()
    ipList =  ip.getSelfIpList()

    #获取的随机数
    num = getImgUrlNum(result)

    #初始化目录
    initDir()

    #设置范围
    firstN = 0
    LastN = 2
    #多线程下载
    #开启多线程下载
    print "开启多线程下载"
    queue = Queue.Queue()
    for enrolYear in range(1, 5):
        for i in range(firstN, LastN):
            preNum = i * (10000/LastN) #起始下载
            nextNum = i * (10000/LastN) + (10000/LastN) - 1 #末尾
            name = '201' + str(enrolYear) +'-' + str(i * 10000/LastN) #线程名
            splider = spliderGradeThread(name, queue,
                enrolYear, num, preNum, nextNum, ipList)
            splider.setDaemon(True)
            splider.start()

    while 1:
        pass
