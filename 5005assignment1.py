import re
import urllib2
from scrapy import Selector

target = "https://en.wikipedia.org/wiki/Yui_Aragaki"
res = urllib2.urlopen(target)
html = res.read()
selector = Selector(text=html, type="html")
text = selector.xpath('.//div[@id="mw-content-text"]').xpath('string(.)').extract_first()
t = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').replace(',', ' ').strip()
t = re.sub('\s+', ' ', t)
print t