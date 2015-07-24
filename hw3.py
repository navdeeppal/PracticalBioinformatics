#! /usr/bin/env python
#Using mymodule program to correct the given path 
from mymodule import *
import sys
if 0: 
	print 'Please select appropriate files with appropriate address'
	sys.exit()
else:
	input=sys.argv[1]
	sampleid=sys.argv[2]
	output=sys.argv[3]
infile=open(sampleid,'rU') 
sample={}
N=0;
for Line in infile:
	Line=Line.strip()
	sample[Line]=N 
	N+=1
sys.stderr.write(str(N)+' samples in '+sampleid+'\n')
infile.close()
input=cygwinpath(input)
output=cygwinpath(output)
infile=open(input,'rU') 
outfile=open(output,'w') 
status=0
ncol=0 # Assigning # of columns in Input file
for Line in infile:
	Line=Line.strip('\n') #strip end-of-line
	if Line[0]=='#': 
		if Line[1]!='#': #title line 
			varname=Line.split('\t')
			ncol=len(varname)
			outfile.write('\t'.join(varname[0:9])) #write the first 9 columns
			write={} 
			for i in range(9,ncol):
				if(varname[i] in sample): 
					outfile.write('\t'+varname[i])
					write[i]=True
				else:
					write[i]=False
			outfile.write('\n') #end of the line
		else:
			outfile.write(Line+'\n') #meta info remain untouched
		continue #ignore the following commands
	col=Line.split('\t') 
	outfile.write('\t'.join(col[0:9])) #write the first 9 columns
	for i in range(9,ncol):
		if(write[i]): #check whether this column needs to be written
			outfile.write('\t'+col[i])
	outfile.write('\n') #end of the line
	status+=1
#Status Check with each 100 lines
	if status%100==0:
		Status=str(status);
		sys.stderr.write(Status+'\r')
infile.close() 
outfile.close() 
print 'Lines scanned in VCF file=',status, ',Please check output file for results'