#! /usr/bin/python
print
proteinseq1="AGGGGGCATCATCAGGGAAAGGGGGCATCATGAGAGAAAGGACATCATGCCCCACAGTCATCATGAAAGGGGGCATCATCAGGAGGGGTTGCCCCACAG"
proteinseq2="AGGGGGCATCATCAGGGAAAGGGGGGGCCTCACAGGGAAGCATCATGAGAGAAAGTGCGGGTCATCATCATGGAGGGGCATCAT"
proteinseq3="GGGGCATCATCAGGGAGAGGGGGCATCATCAGGGGGCATCATCAGGGATTAAGGGGGCTCCCACAGGGAAAGG"
NoCatseq="AGGGGGCACAGGGGGCAGGGATTAAGGGGGCTCCCACAGGGAA"
insertionCat="CAT"
print
print "First protein sequence is:", proteinseq1
print "Second protein sequence is:", proteinseq2
print "Third protein sequence is:", proteinseq3
print "Fourth protein sequence without 'Cat' insertion or NoCatseq is:",NoCatseq
print "insertion mutation sequence is:", insertionCat
print
print "The insertional 'cat' mutation in this protein causes 'Scratch a Cat' disease :)"
print
seqlength1=len(proteinseq1)
seqlength2=len(proteinseq2)
seqlength3=len(proteinseq3)
NoCatlength=len(NoCatseq)
CatInsertionLength=len(insertionCat)
print "Sequence Lengths"
print "Length of 1st sequence is:", seqlength1
print "Length of 2nd sequence is:", seqlength2
print "Length of 3rd sequence is:", seqlength3
print "Length of NoCatseq sequence is:", NoCatlength
print "Length of CAT insertional mutation is:", CatInsertionLength
print
seq1countA=proteinseq1.count('A')
seq1countG=proteinseq1.count('G')
seq1countC=proteinseq1.count('C')
seq1countT=proteinseq1.count('T')
seq2countA=proteinseq2.count('A')
seq2countG=proteinseq2.count('G')
seq2countC=proteinseq2.count('C')
seq2countT=proteinseq2.count('T')
seq3countA=proteinseq3.count('A')
seq3countG=proteinseq3.count('G')
seq3countC=proteinseq3.count('C')
seq3countT=proteinseq3.count('T')


print "First Sequence Counts:"
print "The total number of 'A' bases in the 1st sequence is:", seq1countA
print "The total number of 'G' bases in the 1st sequence is:", seq1countG
print "The total number of 'C' bases in the 1st sequence is:", seq1countC
print "The total number of 'T' bases in the 1st sequence is:", seq1countT
print
print "Second Sequence Counts:"
print "The total number of 'A' bases in the 2nd sequence is:", seq2countA
print "The total number of 'G' bases in the 2nd sequence is:", seq2countG
print "The total number of 'C' bases in the 2nd sequence is:", seq2countC
print "The total number of 'T' bases in the 2nd sequence is:", seq2countT
print
print "Third Sequence Counts:"
print "The total number of 'A' bases in the 3rd sequence is:", seq3countA
print "The total number of 'G' bases in the 3rd sequence is:", seq3countG
print "The total number of 'C' bases in the 3rd sequence is:", seq3countC
print "The total number of 'T' bases in the 3rd sequence is:", seq3countT
print
print "The first sequence has"
print "A:%.1f percent, G:%.1f percent, C:%.1f percent & T:%.1f percent"%(100.0*seq1countA/seqlength1,100.0*seq1countG/seqlength1,100.0*seq1countC/seqlength1,100.0*seq1countT/seqlength1)
print
print "The second sequence has"
print "A:%.1f percent, G:%.1f percent, C:%.1f percent & T:%.1f percent"%(100.0*seq2countA/seqlength2,100.0*seq2countG/seqlength2,100.0*seq2countC/seqlength2,100.0*seq2countT/seqlength2)
print
print "The third sequence has"
print "A:%.1f percent, G:%.1f percent, C:%.1f percent & T:%.1f percent"%(100.0*seq3countA/seqlength3,100.0*seq3countG/seqlength3,100.0*seq3countC/seqlength3,100.0*seq3countT/seqlength3)
print
print "Another way of reporting sequence lengths and base counts:"
print "The first sequence is %d bases long with %d 'A' bases, %d 'G' bases, %d 'C' bases and %d 'T' bases."%(seqlength1,seq1countA,seq1countG,seq1countC,seq1countT)
print "The second sequence is %d bases long with %d 'A' bases, %d 'G' bases, %d 'C' bases and %d 'T' bases."%(seqlength2,seq2countA,seq2countG,seq2countC,seq2countT)
print "The third sequence is %d bases long with %d 'A' bases, %d 'G' bases, %d 'C' bases and %d 'T' bases."%(seqlength3,seq3countA,seq3countG,seq3countC,seq3countT)
print
print "Is CAT mutation found in each sequence?"
print
if insertionCat in proteinseq1:
	print "Cat found in the first DNA sequence."
else:
	print "Cat Protein sequence not found in the first DNA sequence."
if insertionCat in proteinseq2:
	print "Cat found in the second DNA sequence."
else:
	print "Cat Protein sequence not found in the second DNA sequence."
if insertionCat in proteinseq3:
	print "Cat found in the third DNA sequence."
else:
	print "Cat Protein sequence not found in the third DNA sequence."
if insertionCat in NoCatseq:
	print "Cat found in the 'NoCatseq' DNA sequence."
else:
	print "Cat protein sequence not found in the 'NoCatseq' DNA sequence."
print

ProteinSeqCount=0
for insertionCat in proteinseq1:
	#Let's see what percent of total bases is CAT sequence in the first DNA sequence
	ProteinSeqCount=proteinseq1.count('CAT')
print "CAT insertion is seen these many times in the first sequence:",ProteinSeqCount
ProteinBasePercent=100.0*6.0*ProteinSeqCount/seqlength1
print "Percent of bases in the first DNA sequence that correspond to 'CAT' sequence is %d percent:"%(ProteinBasePercent)
print
ProteinSeqCount2=0
for insertionCat in proteinseq2:
	#Let's see what percent of total bases is CAT sequence in the first DNA sequence
	ProteinSeqCount2=proteinseq2.count('CAT')
print "CAT insertion is seen these many times in the second sequence:",ProteinSeqCount2
ProteinBasePercent2=100.0*6.0*ProteinSeqCount2/seqlength2
print "Percent of bases in the seconde DNA sequence that correspond to 'CAT' sequence is %d percent:"%(ProteinBasePercent2)
print
ProteinSeqCount3=0
for insertionCat in proteinseq3:
	#Let's see what percent of total bases is CAT sequence in the third DNA sequence
	ProteinSeqCount3=proteinseq3.count('CAT')
print "CAT insertion is seen these many times in the third sequence:",ProteinSeqCount3
ProteinBasePercent3=100.0*6.0*ProteinSeqCount3/seqlength3
print "Percent of bases in the third DNA sequence that correspond to CAT sequence is %d percent:"%(ProteinBasePercent3)
print
print "More number of insertions is known to be associated with more severe form of 'Scratch a Cat' disease"
print "Conclusion: Individual 'proteinseq1' is likely to have the most severe form of this disease than other three individuals"
print
print "Disclaimer: 'Scratch a Cat' is not a real disease as opposed to Cat-scratch disease :)"
print
print "THANK YOU :)"
print

