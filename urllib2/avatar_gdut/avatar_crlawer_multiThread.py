#coding:utf-8
#!/usr/bin/python2.7

"""抓取GDUT学生工作信息管理系统学生头像

多线程抓取GDUT学生工作信息管理系统学生头像
学号规则：
    男生： 31 + 入学年份后两位 + 六位排序数字 => 3112000001
    女生： 32 + 入学年份后两位 + 六位排序数字 => 3212000002

    spliderGradeThread: 线程抓取图片
    getImgUrlNum: 获取登录后的随机分配的随机数
    initDir: 初始化图片存储目录
"""

__authors__ = [
    '"Yannyezixin" <646840080@qq.com>'
]

import urllib
import urllib2
import cookielib
import re
import os
import threading
import Queue
import sys
import gdutsyslogin
import ipproxy
import time
from random import choice

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

        print "准备抓取图片中..."
        for i in range(self.preNum, self.nextNum):
            sno = self.structureSno(i, self.enrolYear)
            url = "http://gdutfile.eswis.cn/upfiles/{num}/userpic/20{enrolYear}/{sno}.jpg".format(
                    num = num, enrolYear = str(self.enrolYear), sno = sno)
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
            urllib2.urlopen(req, timeout=2)
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
            global imageDownCount
            imageDownCount += 1
            print "成功下载：%s 的学生的头像" % url
        except:
            pass

    def replaceSnoUrlSto(self, stuSno, url, storagePath):
        """替换学号，URL，存储路径,重新下载"""

        boy = re.compile(r'boy')
        boySno = re.compile(r'/31')
        url = boySno.sub('/32', url)
        storagePath = boy.sub('girl', storagePath)
        storagePath = boySno.sub('/32', storagePath)

        # 重新下载
        if self.checkImgUrlStatus(url, True):
            self.downloadImg(url, storagePath)


    def structureSno(self, i, enrolYear):
        """构造学号函数"""

        strNum = str(i)
        length = len(strNum)
        if length == 4:
            num = strNum
        else:
            num = '0' * (4 - length) + strNum

        return "31{enrolYear}00{num}".format(
                enrolYear = str(enrolYear), num = num)

    def getStoragePath(self, enrolYear, filename):
        """获取存储路径"""

        enrolYear = '20' + str(enrolYear)
        dest_dir = os.path.join('img', 'boy', enrolYear, filename)

        return dest_dir

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

    directory = os.path.join('img')
    boyDir = os.path.join(directory, 'boy')
    girlDir = os.path.join(directory, 'girl')
    if not os.path.exists(directory):
        print '目录初始化中...'
        os.mkdir(directory)
        os.mkdir(boyDir)
        os.mkdir(girlDir)
        for i in range(2011,2015):
            os.mkdir(os.path.join(boyDir, str(i)))
            os.mkdir(os.path.join(girlDir, str(i)))

if __name__ == '__main__':

    #图片下载数量
    imageDownCount = 0

    username = '3113006386'
    password = '130608q'

    while True:
        login = gdutsyslogin.login(username, password)
        result = login.result
        if result == None:
            print "登陆超时, 重新登录中..."
        else:
            print "登录成功"
            break

    #获取代理ip
    ip = ipproxy.getiplist()
    ipList =  ip.getSelfIpList()

    #获取的随机数
    num = getImgUrlNum(result)

    #初始化目录
    initDir()

    #设置范围
    firstN = 0
    LastN = 1
    #多线程下载
    #开启多线程下载
    print "开启多线程下载"
    queue = Queue.Queue()
    for enrolYear in range(10, 12):
        for i in range(firstN, LastN):
            preNum = i * (10000/LastN) #起始下载
            nextNum = i * (10000/LastN) + (10000/LastN) - 1 #末尾
            name = '201' + str(enrolYear) +'-' + str(i * 10000/LastN) #线程名
            splider = spliderGradeThread(name, queue,
                enrolYear, num, preNum, nextNum, ipList)
            splider.setDaemon(True)
            splider.start()

    while 1:
        time.sleep(30)
        print "图片下载数量： %s 张" % imageDownCount
        pass
