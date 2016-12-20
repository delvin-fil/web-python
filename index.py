print ("Content-Type: text/html; charset=\'utf-8\'\n")
# -*- coding: utf-8 -*-
import decimal, locale, os, sys, re, urllib
from urllib.request import *
import translit_v4 as trans

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
name = "Delvin"
ver = sys.version
resul = (ver[0:9])
print ("<head>")
print ("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
print ("<link rel=\"stylesheet\" type=\"text/css\" href=\"my.css\" />")
print (f"<title> Python-3.6 cod by {name}</title>\n</head>")
print (f"<body>\n")
'''print ("<div id=\"header\">")
print ("<?php include (\'header.txt\'); ?>")
print ("</div>")'''
print ("<header>")
print ("<div id=\"header-py\" class=\"header-bg\">")
print ("Fuck this HEADER!")
print ("</div>")
print ("</header><BR>")
print ("<div id=\"content\">")
print (f"<H2>Hi {name}!</H2>")
print(f"<p>Python-{resul}")
print (f"<br><a href=index.php>Prev. page</a>")
#print ("<br>", f"FUSK", f"СУКА", f"Sheet")

url="http://bash.im/forweb/?u"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('UTF-8')
result = re.sub(r'\<[^>]*\>', '', html)
result = re.sub(r'var borq=\'\';', '', result)
#result = re.sub(r'Больше на bash.im!\'\;', '', result)
result = re.sub(r'&quot', '"',result)
result = re.sub(r'&lt', '<', result)
result = re.sub(r'&gt', '>', result)
result = re.sub(r'borq \+= \'', '',result)
result = re.sub(r'";', "\"", result)
result = re.sub(r'document.write\(borq\);', '',result)
result = re.sub(r' ]', ' ]\n',result)
result = re.sub(r'xxx', '\nxxx', result)
result = re.sub(r'yyy', '\nyyy', result)
result = re.sub(r'XXX', '\nXXX', result)
result = re.sub(r'YYY', '\nYYY', result)
result = re.sub(r';', '', result)
result = trans.transliterate(result)
result = re.sub(r'Bolshe na bash.im!', '', result)
print (f"<br>" +result)
print ("</div></body>")