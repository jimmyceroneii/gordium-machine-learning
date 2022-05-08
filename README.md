# gordium-machine-learning

The code in this repository requires some editing for use on anything other than my computer. Right now, in the `file_names.sh` file, I have hardcoded file access to specific files on my computer. To generalize it for use elsewhere, you'll have to go in and change those files.

## file_names.sh

This bash script exists because I'm a Python newbie. I found it easier to manipulate files in bash than Python. 

The essence of this script is the creation of a file with a list of file names in it. The file titles are later used in the `nlp.py` file to check for similarity. 

Why use file titles? Because it's so compute intensive to check a whole document. Sometime soon I will take a stab at that, but it will require careful thought not to blow up my computer.

The list of files created here is then passed into `nlp.py` as an input for the real action.

Usage of this script is of the form: `./file_names.sh PROBLEM_NAME`

The `PROBLEM_NAME` passed in is compared with the problems accumulated earlier, resulting in a similarity score that's output as part of `nlp.py`.

## nlp.py

The python file takes in a list of file names. In our particular case, the list of file names is a list of startup problems. Our goal is to generate novel connections based on the similarity of problems. 

The script relies on several common libraries: 

### spacy

`spacy` takes care of our natural language processing. We are currently using the `en_core_web_md` model for no particular reason other than it works.

We use `spacy` to compare each word in the problem passed in to each word of each problem in our database. Thus, we generate a similarity score for each problem.

The output of all that work is thus: 

```
{
	"PROBLEM_NAME": string,
	"SIMILARITY_SCORE": number
}
```

## pandas

Once we have the similarity scores, we need to display them in an efficient and sane way. To do that, we are leveraging the `pandas` library, which is awesome for all things data processing. 

I take the dictionary derived from the previous step and turn into into a `pandas` DataFrame object with columns of 'Title' and 'Score'.

Then I filter out the 10 problems with the highest similarity score. The output is as follows: 

```
#################### Title Similarity #####################



                                               Title     Score
0  We can heat things quickly but can't cool them...  7.281352
1     There are no board games that make fun of work  6.725839
2  There is not always a place you can drop off t...  6.660065
3  Few companies solve problems generally like we...  6.655237
4  It is hard to know what plants make a complete...  6.641575
5         Elders have a hard time remembering things  6.631287
6      It's hard to know where you are in a codebase  6.627610
7      We don't make good investment decisions alone  6.626899
8  When thru hiking, it is best to use a tarp ten...  6.595408
9  You don’t know an avocado is good until you op...  6.589247



################################################################
```