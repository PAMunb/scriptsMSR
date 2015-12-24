import os, csv, random, time

#csvFile = raw_input('Input Log File (log.txt):')
csvTemp = "temp.csv"

dirproject = 'Projects/'
dirProjects = os.path.abspath(dirproject)+"/"

projects = [dirProjects+d for d in os.listdir(dirProjects) if os.path.isdir(dirProjects+"/"+d)]


def listOfCommits(fileCsv):
	commits = []
	with open(fileCsv, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			commits.append(row[0])
		f.close()
	return commits


def removeTemFile(tempFile):
	os.remove(tempFile)

def sample(listOfCommits):
	if len(listOfCommits) > 100:
		return random.sample(listOfCommits, 100)
	else:
		return listOfCommits



#cria um arquivo temporario temp.csv como os dados do commit de 1 projeto por vez

for project in projects:
	#git --git-dir Projects/bitcoin/.git log --pretty=tformat:%H
	os.system("git --git-dir "+ project + "/.git log --pretty=tformat:%H, >> "+ csvTemp)

	sampleCommits = sample(listOfCommits(csvTemp))

	for c in sampleCommits:
		os.system("git --git-dir "+ project +  "/.git  checkout -b " + c)
#----------------------------------------------------------------------------------------
		print "wait to analysis in project: "+project+" commit:"+c+" ..."

		#aqui realizar a chamada ao sistema de um Jar....

		time.sleep(1)
#----------------------------------------------------------------------------------------

	removeTemFile(csvTemp)

	break

