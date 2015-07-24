#! /usr/bin/env python
#Using mymodule program to correct file location
from mymodule import *
import sys
if 0: 
	print 'Please put appropriate address of files'
	sys.exit()
else:
	input=sys.argv[1]
	variantlist=sys.argv[2]
	output=sys.argv[3]
infile=open(variantlist,'rU') 
Variant={}
Variant={'col1':[],'col2':[]}
N=0;
for Line in infile:
	Line=Line.strip('\n')
	Variants=Line.split('\t')
	Variant['col1'].append(Variants[0])
	Variant['col2'].append(Variants[1])
	N+=1
sys.stderr.write(str(N)+' samples found in '+ variantlist+'\n')
infile.close()
input=cygwinpath(input)
output=cygwinpath(output)
infile=open(input,'rU') 
outfile=open(output,'w') 
status=0
ncol=0
for Line in infile:
	Line=Line.strip('\n') 
	if Line[0]!='#':
		col=Line.split('\t') 
		if (col[0] in Variant['col1'] and col[1] in Variant['col2']):
			outfile.write(Line+'\n')
	else:
		outfile.write(Line+'\n') 
		continue

#Checking progress
	status+=1
	if status%100==0:
		Status=str(status)+' scanned';
		sys.stderr.write(Status+'\r')
infile.close() 
outfile.close() 
print 'Lines scanned in VCF file=',status, ',Please check output file for results'