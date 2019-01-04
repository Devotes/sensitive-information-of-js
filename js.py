#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import requests
import re
import jsbeautifier
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def readjs(url):
	try:
		r = requests.get(url,verify=False, allow_redirects=True)
		if r.status_code ==200:
			fsr=open('config/jsconment.txt','w')
			fsr.write(jsbeautifier.beautify(r.text).encode('utf-8'))
			fsr.close()
			f=open('config/keyword.txt','r')
			for keyword in f:
				keyword=keyword.strip('\n\r')
				sr=re.compile(keyword,re.I)
				if sr.findall(r.text):
					search_line(sr)
			f.close()
		else:
			print 'fail to connect '+url
	except:
		print 'fail to connect '+url



def search_line(sr):
    fl = open('config/jsconment.txt', 'r') 
    line =0
    while True:
        lines = fl.readline() 
        if not lines:  
            break
        line += 1
        if sr.findall(lines):
            key=str(sr.findall(lines))
            report_line(key,line,lines)
            continue
    fl.close()

def report_line(key,line,lines):
	fs.write('-'*60+'\n')
	fs.write("[*] on line : "+ str(line)+"--> "+key+'\n')
	fs.write(str(lines).strip('\r\n')+'\n\n')


if __name__ == '__main__':
	fjs=open('js-url.txt','r')
	for url in fjs:
			url=url.strip('\r\n')		
			fs=open('result/'+str(url.split('/')[-1])+'.txt','w')
			readjs(url)
			print url+' audit successfully!'
			fs.close()
	fjs.close()

	