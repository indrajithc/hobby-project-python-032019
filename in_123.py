import audioSegmentation as ad
import timeit
import numpy
import sys
import os
from terminaltables import AsciiTable
import spinner
import record_audio as ra
from operator import itemgetter

spinner = spinner.Spinner()

if len(sys.argv) > 1:
    audi = sys.argv[1]
else: 
	audi=input("Enter a wav file: ")

if len(audi) <= 1:
	print("invalid input \n")
	exit()

print("\n")
if (audi == 'rec' and len(sys.argv[2]) ):
	if sys.argv[2].isdigit():
		seconds = int(sys.argv[2])
		tmpa = " recording : " +str(seconds)+"s"
		print(tmpa)x
		spinner.start(tmpa)
		record = ra.record(seconds, "audio.wav")
		spinner.stop()
		print(" saved file name : ", record , "\n\n")
		audi =record
	else:
		print("invalid input \n")
		exit()


 
 
spinner.start(" analysing audio ...")
 

filename = audi
n_speakers = -1
mt_size=2.0
mt_step=0.2
st_win=0.05
lda_dim=35
plot_res=False

cls = ad.speakerDiarization(filename, n_speakers, mt_size, mt_step, st_win, lda_dim, plot_res)
 
a = numpy.array(range(len(cls)))*mt_step+mt_step/2.0    

a= cls

spinner.stop()

print("Number of speakers in the audio: ",len(set(a)))

 
# print( "Data : ", cls)
# print( "Data : ", a)


# exit()


print("\n")
b=list(set(a))
 
# COMM 
itere=0.05
itere=2.0
itere=0.2
itere=5

 
count=[[int(a[0]), 1]]
 
for ind in range (1,len(a)-1):  
	tmp = int(a[ind]);
	revtmp = int(a[ind-1]);
	if(tmp == revtmp):
		count[len(count)-1][1]+=1
	else:
		count.append([tmp, 1])

count[len(count)-1][1]+=1
 



countPri=[]

tmpInTimeFrom = 0.0
interTemp = 0.0
for ind, term in  count:
	tmpInTime = (term / itere)
	tmpInTimeTo=tmpInTimeFrom + tmpInTime
	countPri.append([ind, term,  interTemp, tmpInTimeTo ])
	tmpInTimeFrom= tmpInTimeTo
	interTemp = tmpInTimeFrom+0.1
	 
 #sorted data
countPri.sort(key=itemgetter(0))  
	
  

table_data = [['person', 'Time From [in m]', "Time To [in m]"] ]


tmpInTimeFrom = 0.0 
for ind, term, tmpInTimeFrom, tmpInTimeTo in  countPri:   
	table_data.append([ " person "+str( ind), "%.2f" % (tmpInTimeFrom/60), "%.2f" % (tmpInTimeTo/60)  ]);
	 
 
	



table = AsciiTable(table_data)
print(table.table)















exit()
print("==========================================");
print("===================================");
print("================ =========================");

#=================
#============================== test ======
#=================





countNext=b; 
for el in  range (0,len(b)):  
	countNext[el] = [int(b[el]), 0]; 
 

for el in  range (0,len( countNext )): 
	for elIn in  range (0,len( count )): 
		if(countNext[el][0] == count[elIn][0]): 
			countNext[el][1] += count[elIn][1]

	 
 




#	print(count);
#print("op=>", a);
#print("count",count) 

simpi = 1
for ind, term in  countNext:  
#	print(" person ", simpi, "[ id: ",ind, "] " , "{",term, itere, "}" ,"->", "%.2f" % (term * itere) )
	print(" person ", simpi, "[ id: ",ind, "] " ,"=>", "%.2f" % (term * itere), "s" )
	simpi+=1;
	


