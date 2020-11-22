from pydub import AudioSegment

import sys
import os 

if len(sys.argv) > 1:
    audi1 = sys.argv[1]
else: 
	audi1=input("Enter 1st wav file: ")

if len(sys.argv) > 1:
    audi2 = sys.argv[2]
else: 
	audi2=input("Enter 2nd wav file: ")

if (len(audi1) <= 1 or len(audi2) <= 1):
	print("invalid input \n")
	exit()



if len(sys.argv) > 1:
    audi3 = sys.argv[3]
else: 
	audi3="output.wav"
  
sound1 = AudioSegment.from_file(audi1)
sound2 = AudioSegment.from_file(audi2)

combined = sound1.overlay(sound2)

combined.export(audi3, format='wav')
print("success", audi3)