#coding=gbk
import re
file="李.svg"
f=open(file,"r")
content=f.readlines()
fw='李.txt'
fp=open(fw,'w+')
fp.write("s\n")
# x=[0 for n in range(len(str.split(mth[0])))]
# y=[0 for n in range(len(str.split(mth[0])))]
# dx=[0 for n in range(len(str.split(mth[0]))-1)]
# dy=[0 for n in range(len(str.split(mth[0]))-1)]

# def orgs():
	# for i in range(len(content)):
		# if content[i].find("fill:None")==-1:
			# if content[i].find("points")!=-1:
				# myStr=content[i]
				# mth=re.findall('"(.*?)"',myStr)
				# line=str.split(mth[0])[3]
				# org_x=int(line.split(',')[1])
				# org_y=int(line.split(',')[0])
	# return org_x,org_y
global org_x,org_y
	
for i in range(len(content)):
	if content[i].find("fill:None")==-1:
			if content[i].find("points")!=-1:
				myStr=content[i]
				mth=re.findall('"(.*?)"',myStr)
				line=str.split(mth[0])[3]
				org_x=int(line.split(',')[1])
				org_y=int(line.split(',')[0])
				print ("original=")
				print org_x,org_y
	if content[i].find("fill:None")!=-1:
		myStr=content[i]		
		mth=re.findall('"(.*?)"',myStr)
		# print mth
		x=[0 for n in range(len(str.split(mth[0])))]
		y=[0 for n in range(len(str.split(mth[0])))]
		for j in range(len(str.split(mth[0]))):
			line=str.split(mth[0])[j]
			y[j]=int(line.split(',')[0])
			x[j]=65535-int(line.split(',')[1])
			print j,65535-x[j]
			fp.write(str((x[j]-org_x)/700))
			fp.write("\t")
			fp.write(str((y[j]-org_y)/700))
			fp.write("\n")
			
		fp.write("s\n")				
fp.close()
# print org_x
# print org_y
# raw_input=("press")
