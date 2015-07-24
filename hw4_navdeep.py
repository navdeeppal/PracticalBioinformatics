#! /usr/bin/env python
# Homework 4
# Practical Bioinformatics
# Navdeep Pal
# Date: 3/28/2014

import sys
Input=sys.argv[1] # locate input file
Input1=sys.argv[2]
output=sys.argv[3]
idlist1=open(Input,'rU')
idlist2=open(Input1,'rU')
ids={}
ids2={}
ids3={}
ids4={}
num=0
for Line in idlist1:
	ids[Line] = num
	num+=1
num=0
for Line in idlist2:
	ids2[Line] = num
	num+=1
idlist1.close()
idlist2.close()
choice='yes'
while choice.upper()=='YES' or choice.upper()== 'Y':
	out = open(output, 'w')
	userchoice= str(raw_input("What do want to do? \n1. Intersection of two lists \n2.\
 Unique to List 1 \n3. Unique to List 2 \n4. Union of two lists\n\
Please choose any one of the options given above:"))
	num=0
	if(userchoice=='1'): #finding intersection of two files
		for key in ids.keys():
			if key in ids2.keys():
				num+=1
				out.write(key.rstrip('\n')+'\r\n')
				print key .rstrip('\n')
	elif userchoice=='2': # finding unique ids in list1
		for key in ids.keys():
			if key not in ids2.keys():
				ids3[key]=num
				num+=1
				out.write(key.rstrip('\n')+'\r\n')
				print key .rstrip('\n')
	elif(userchoice=='3'):# finding unique ids in list2
		for key in ids2.keys():
			if key not in ids.keys():
				ids4[key]=num
				num+=1
				out.write(key.rstrip('\n')+'\r\n')
				print key .rstrip('\n')
	elif(userchoice=='4'): # finding union of two lists
		for key in ids.keys():
			ids4[key]=num
			num+=1
			print key .rstrip('\n')
			out.write(key.rstrip('\n')+'\r\n')
		for key in ids2.keys():
			ids4[key]=num
			
			if key not in ids.keys():
				num+=1
				print key .rstrip('\n') 
				out.write(key.rstrip('\n')+'\r\n')
	else:
		print 'Incorrect Input, Please choose from above options'
		continue
	out.close()
	sys.stderr.write(str(num)+' ids found per your request\n')
	choice=raw_input("Do you want to run another option? [Yes/No]")