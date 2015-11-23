import csv
import os
from subprocess import call

inputFile = raw_input('Input file: ')
outputDir = raw_input('Output dir: ')

f = open(inputFile, 'rt')

try:
  reader = csv.reader(f)
  for row in reader:
    os.system('git clone ' + row[4] + ' ' + outputDir + "/" + row[0])
finally:
  f.close() 
