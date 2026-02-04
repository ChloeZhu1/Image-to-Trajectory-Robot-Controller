#coding=gbk
import string
import model_1

temp=raw_input("请输入全诗正文\n")
poem=[0 for i in range(len(temp)/2)]

for i in range(len(temp)/2):
	poem[i]=str(temp[2*i])+str(temp[2*i+1])

for j in range(4):
	for i in range(7):
		writeachar(poem[4-j+4*i])