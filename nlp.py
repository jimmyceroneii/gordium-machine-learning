import sys
import os
import spacy

## grab the idea passed
currentIdea = sys.argv[3]

## swap the dashes for spaces
cleanedCurrentIdea = currentIdea.split('-')

## grab the file name from the command line
file = sys.argv[2]

## create a list to hold the files
fileNames = list()

## open the file of files (from ls)
with open(file) as file:
	## start to read the file 
	fileOfFiles = file.read()

	## split the list of files on newlines
	uncleanedList = fileOfFiles.split('\n')

	## remove any empty strings from the list
	cleanedList = [x for x in uncleanedList if len(x) > 0]

	## loop through the list of files
	for idea in cleanedList:

		## remove the .md extension from the file name
		cleanedIdea = os.path.splitext(idea)
		
		## append the cleaned file name to the list
		fileNames.append(cleanedIdea[0])

## Reference to model: https://spacy.io/models/en#en_core_web_md
nlp = spacy.load('en_core_web_md')

fileScores = {}

## iterate through the words passed in
for word in cleanedCurrentIdea:

	## create a token for each word for processing
	token = nlp(word)

	## loop through the list of files
	for file in fileNames:
		## turn the title into a doc
		doc = nlp(file)
		## count the number of words in the title
		count = 0
		## keeps the score of the similarity between the current one and the title
		docTotal = 0
		## loop through the words in the title
		for sent in doc.sents:
			## add the similarity score of each word in the title to the running list
			docTotal += token.similarity(sent)
			count += 1
		
		## average the similarity score of the words in the title
		if file in fileScores:
			fileScores[file] += docTotal / count
		else:
			fileScores[file] = docTotal / count

## sorts the scores by title
sortedFileScores = dict(sorted(fileScores.items(),key= lambda x:x[1]))
print(sortedFileScores)
