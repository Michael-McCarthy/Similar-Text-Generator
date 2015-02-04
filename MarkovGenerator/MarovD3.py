'''
Created on Nov 19, 2014

@author: MIKE
'''
import random


FILEARRAY = []

FILEARRAY.append(raw_input("Enter the path to the .txt file you would like to use \n"))


addFile = 1

while addFile == 1:
    moreFile = raw_input("Would you like to add more files? \n Type 'y' for yes \n")
    if not str(moreFile) == 'y':
        addFile = 0
        break
    else:
        FILEARRAY.append(raw_input("Enter the path to the .txt file you would like to use \n"))


words = []
for i in range(0, len(FILEARRAY)):
    f = open(str(FILEARRAY[i]), "r")
    for line in f.readlines():
        for word in line.split():
            words.append(word)
wordSize = len(words)
database = {}
    
for i in range (0,wordSize-4):
    key = (words[i], words[i+1], words[i+2])
    if not database.has_key(key):
        database.update({key:[words[i+3]]})
    else:
        database[key].append(words[i+3])
        

seed = random.randint(0, wordSize - 4)
w1, w2, w3 = words[seed], words[seed+1], words[seed+2]
gen_sent = [""]
periods = 0
while periods < 10:
    gen_sent.append(w1)
    if str(w1).endswith('.'):
        periods = periods + 1
        gen_sent.append('\n')
    w1, w2, w3 = w2, w3, random.choice(database[(w1,w2,w3)])

print ' '.join(gen_sent)
print "\n"

save = raw_input("Would you like to save this generated text? Type 'y' to save")
if str(save) == ("y"):
    with open("./best.txt", "a+") as s:
        s.write("\n ------------------------------------------- \n")
        s.write(' '.join(gen_sent))
    print "SAVED"

'''
Created on Nov 19, 2014

@author: MIKE
'''
