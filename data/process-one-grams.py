
# open one-grams.txt and extract all words beginning with a
# output them to a file line by line

# word 12938


infile = open('one-grams.txt', 'r', encoding='utf-8')

# contents = infile.read() # get all the contents as a single string
# infile.readlines() # returns a list of all lines in the file

myWords = []

#for line in infile:
#   tokens = line.split()
#   word = token[0].lower()
#   if word[0] == 'a':
#      myWords.append(word)

myWords = [line.split()[0] for line in infile if line.split()[0][0] == 'a']


infile.close()



outfile = open('output.txt', 'w')

for word in myWords:
   outfile.write('%s\n' % word)

outfile.close()
