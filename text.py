fh = open("text.txt)
file = fh.read().split()
 
def revword(word):
   word = word.lower()[::-1]
   return word

def countword():
    count = 1
    word = file[0]
    for i in file[1:]:
        w = revword(i)
        if w == word:
            count = count + 1      
    return count
 













