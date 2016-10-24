import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

from loader import loadRaw

# Replace all non-word characters with whitespace. Exclude apostrophes
def removeNonWordCharacters(s):
   s = re.sub(r"[^a-zA-Z']+", " ", s)
   s = re.sub(r"( ')|(' )", " ", s)
   return s


# Remove all urls from a string
def removeURLs(s):
   return re.sub(r'https?:\/\/.*? ', '', s)


# Remove all HTML tags from a string
def removeHTML(s):
   return BeautifulSoup(s).get_text()


def clean(s):
   s = s.strip()
   s = removeHTML(s)
   s = removeURLs(s)
   s = removeNonWordCharacters(s)
   return s


allWords = None
def words():
   global allWords
   if allWords is None:
      with open('one-grams.txt', 'r') as infile:
         lines = [line.split()[0] for line in infile]

      allWords = set(lines)
   return allWords


# Extract a list of tokens from a cleaned string.
def tokenize(s):
   wordList = words()
   stopWords = set(stopwords.words('english'))
   wordsToInclude = wordList - stopWords

   return set(x for x in s.lower().split()
                  if x in wordsToInclude and len(x) > 3)


def process():
   print("Loading comments...")
   storyDict = loadRaw()

   print("Cleaning and tokenizing comments...")
   i = 1

   for storyId in storyDict:
      storyDict[storyId] = tokenize(clean(storyDict[storyId]))
      if i % 100 == 0:
         print(i)
      i += 1

   print("Writing to disk...")
   with open('tokenized.txt', 'w') as outfile:
      for storyId, wordSet in storyDict.items():
         wordList = ','.join(list(sorted(list(wordSet))))
         outfile.write('%d|%s\n' % (storyId, wordList))

   print("Done!")


process()
