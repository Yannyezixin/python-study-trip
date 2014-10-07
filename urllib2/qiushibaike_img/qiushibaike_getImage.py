#coding=utf-8
import urllib2
import urllib
import re

def getHtml(url):
    headers = {
                "GET": url,
                "Host": "www.qiushibaike.com",
                "Referer": "http://www.qiushibaike.com/hot",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36",
              }

    req = urllib2.Request(url)
    for key in headers:
        req.add_header(key, headers[key])

    html = urllib2.urlopen(req).read()
    return html

def getImageUrl(html):
    filtHtmlgetImgRe = re.compile(r'src="(.*\/picture.*\.jpg)"')
    result = filtHtmlgetImgRe.findall(html)
    return result

def getImageName(url):
    filtUrlNameImgRe = re.compile(r'medium\/(.*\.jpg)')
    result = filtUrlNameImgRe.findall(url)
    return result[0]

def downImg(imgUrlList):
    for imgUrl in imgUrlList:
        name = getImageName(imgUrl)
        urllib.urlretrieve(imgUrl, '%s' % name)
        print '成功下载 %s , 保存为:%s' % (imgUrl, name)

i = 1
url = "http://www.qiushibaike.com/hot/page/"
while i < 150:
    html = getHtml(url+str(i))
    imageUrl = getImageUrl(html)
    downImg(imageUrl)
    i+=1
