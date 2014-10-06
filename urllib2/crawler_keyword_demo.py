#coding:utf-8
import urllib2
import urllib
import re
import time
from random import choice

ipList = ['111.1.44.24:80', '116.236.216.116:8080', '61.234.123.64:8080']
listKeywords = ['php','python']

for item in listKeywords:
    ip = choice(ipList)
    keywords = urllib.quote(item)
    url = "http://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word=" + keywords
    headers = {
                  "GET": url,
                  "Host": "sug.so.360.cn",
                  "Referer": "http://www.so.com/index.html",
                  "User-Agent": "Mozilla/5.0 (X11; Linux i6 \
                      86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36",
              }

    # proxy
    proxy_handler = urllib2.ProxyHandler({'http': 'http://'+ip})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)

    req = urllib2.Request(url)
    for key in headers:
        req.add_header(key, headers[key])

    result = urllib2.urlopen(req).read()
    filterResult = re.findall("\:\"(.\D*?)\"", result)
    for item in filterResult:
        print item

    time.sleep(1)

