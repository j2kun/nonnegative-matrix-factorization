
def loadRaw():
   with open('comments-jan.txt', 'r', encoding="utf-8") as infile:
      lines = [line.split(maxsplit=1) for line in infile]

   return dict((int(storyId), comments) for (storyId, comments) in lines)


def loadCleaned():
   with open('tokenized.txt', 'r') as infile:
      lines = [line.split('|') for line in infile]

   return dict((int(storyId), words.split(',')) for (storyId, words) in lines)
