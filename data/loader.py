

def clean(s):
   # clean a line to remove non-word things like urls, stop words, and punctuation
   # not yet implemented!
   return s.strip()


def load():
   with open('comments-jan.txt', 'r') as infile:
      lines = [line.split(maxsplit=1) for line in infile]

   return dict((int(storyId), clean(comments)) for (storyId, comments) in lines)
