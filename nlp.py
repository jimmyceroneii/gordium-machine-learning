import sys
import os
import spacy
import pandas as pd

## grab the idea passed
currentIdea = sys.argv[3]

## swap the dashes for spaces
cleanedCurrentIdea = currentIdea.split('-')

## grab the file name from the command line
fileWithListOfFiles = sys.argv[2]

## create a list to hold the files
ideaFileNames = list()

## open the file of files (from ls)
with open(fileWithListOfFiles) as fileWithListOfFiles:
	## start to read the file 
	fileOfIdeaTitles = fileWithListOfFiles.read()

	## split the list of files on newlines
	uncleanedList = fileOfIdeaTitles.split('\n')

	## remove any empty strings from the list
	cleanedListOfIdeaFiles = [x for x in uncleanedList if len(x) > 0]

	## loop through the list of files
	for idea in cleanedListOfIdeaFiles:

		## remove the .md extension from the file name
		cleanedIdea = os.path.splitext(idea)
		
		## append the cleaned file name to the list
		ideaFileNames.append(cleanedIdea[0])

## Reference to model: https://spacy.io/models/en#en_core_web_md
nlp = spacy.load('en_core_web_md')

ideaScores = {}

## iterate through the words passed in
for word in cleanedCurrentIdea:

	## create a token for each word for processing
	token = nlp(word)

	## loop through the list of files
	for ideaTitle in ideaFileNames:
		## turn the title into a doc
		doc = nlp(ideaTitle)
		## count the number of words in the title
		count = 0
		## keeps the score of the similarity between the current one and the title
		ideaTotal = 0
		## loop through the words in the title
		for sentences in doc.sents:
			## add the similarity score of each word in the title to the running list
			ideaTotal += token.similarity(sentences)
			count += 1
		
		## average the similarity score of the words in the title
		if ideaTitle in ideaScores:
			ideaScores[ideaTitle] += ideaTotal / count
		else:
			ideaScores[ideaTitle] = ideaTotal / count

## sorts the scores by title
sortedFileScores = dict(sorted(ideaScores.items(),key= lambda x:x[1], reverse=True))

## create a dataframe from the sorted dictionary
display = list()
for key, value in sortedFileScores.items():
	temp = list()
	temp.append(key)
	temp.append(value)
	display.append(temp)

## print the dataframe all nice
df = pd.DataFrame(display, columns=['Title', 'Score'])
topIdeaMatches = df.head(10)
print("\n\n\n#################### Title Similarity #####################\n\n\n")
print(topIdeaMatches)
print("\n\n\n################################################################\n\n\n")

## scan these ten files in whole and resort them.

## start iterating through the list of files
# for idea in topIdeaMatches['Title']:
# 	cleanedIdea = idea.replace('\\', '')
## TODO: Fix the use of escaped characters in the file names
# 	ideaFileName = "/Users/jrcii/Documents/\"Gordium Brain\"/Gordium/Problems/% s.md" %cleanedIdea 
	
# 	with open(ideaFileName) as ideaFile:
# 		ideaFileContent =	ideaFile.read()

# 		lines = ideaFileContent.split('\n')

# 		print(lines)
	
## for each file, open it 
## iterate over each word in the title
## iterate over each word in the file (TODO: unless it's in a list of skip words)
## add the similarity score of each word in the title to the running list

## remaining approaches
## 1. Train a model manually using our pre-existing connections
## 2. Use similarity on the top 10 documents in the list
## 3. Classify the texts and then use that to group them	
