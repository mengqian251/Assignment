import re
import urllib2
from scrapy import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf8')

target = "https://en.wikipedia.org/wiki/The_Big_Bang_Theory"
res = urllib2.urlopen(target)
html = res.read()
selector = Selector(text=html, type="html")
text = selector.xpath('.//div[@id="mw-content-text"]').xpath('string(.)').extract_first()
t = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace(',', ' ').strip()
t = re.sub('\s+', ' ', t)
# print t
f = open("a.txt", "w")
f.write(t)
f.close()
