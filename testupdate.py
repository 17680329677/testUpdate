# -*- coding: utf-8 -*-

#检查网页是否更新
import hashlib,os,requests,pathlib
url = "http://news.sina.com.cn/"
html = requests.get(url).text.encode('utf-8-sig')

md5 = hashlib.md5(html).hexdigest()		#以网页内容的16进制MD5码判断
path = pathlib.Path('E:/python/autotest/oldmd5.txt')
if path.exists():
	with open('E:/python/autotest/oldmd5.txt','r') as f:
		oldmd5 = f.read()
	with open('E:/python/autotest/oldmd5.txt','w') as f:
		f.write(md5)
else:
	with open('E:/python/autotest/oldmd5.txt','w') as f:
		f.write(md5)
if md5 != oldmd5:
	print('数据已更新...')
else:
	print('数据未更新...')