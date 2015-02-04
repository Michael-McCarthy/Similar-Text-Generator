'''
Created on Nov 19, 2014

@author: MIKE
'''
import random


FILEARRAY = []

FILEARRAY.append(raw_input("Enter the path to the .txt file you would like to use \n"))


addFile = 1

while addFile == 1:
    moreFile = raw_input("Would you like to add more files? \nType 'y' for yes \n")
    if not str(moreFile) == ("y"):          
        addFile = 0
        break
    else:
        FILEARRAY.append(raw_input("Enter the path to the .txt file you would like to use \n"))

words = []
for i in range(0, len(FILEARRAY)):
    with open(str(FILEARRAY[i]), "r") as f:
        for line in f.readlines():
            for word in line.split():
                words.append(word)
wordSize = len(words)
database = {}
sBase = {}
    
    

for i in range (0,wordSize-3):
    sKey = words[i]
    if not sBase.has_key(sKey):
        sBase.update({sKey:[words[i+1]]})
    else:
        sBase[sKey].append(words[i+1])
    key = (words[i], words[i+1])
    if not database.has_key(key):
        database.update({key:[words[i+2]]})
    else:
        database[key].append(words[i+2])
        

seed = random.randint(0, wordSize - 3)
w1 = words[seed]
count = 0
while not str(w1) == str(w1).capitalize():
    seed = random.randint(0, wordSize - 3)
    w1 = words[seed]
    count = count + 1
    if count > 2500:
        break
w1 = words[seed]
w2 = random.choice(sBase[w1])
gen_sent = [""]
periods = 0
while periods < 10:
    gen_sent.append(w1)
    if str(w1).endswith('.'):
        periods = periods + 1
        gen_sent.append('\n \n')
    if random.randint(0,15) >= 0:
        w1, w2 = w2, random.choice(database[(w1,w2)])
    else:
        w1, w2 = w2, random.choice(sBase[w2])
print ' '.join(gen_sent)
print "\n"
save = raw_input("Would you like to save this generated text? Type 'y' to save")
if str(save) == ("y"):
    with open("./best.txt", "a+") as s:
        s.write("\n ------------------------------------------- \n")
        s.write(' '.join(gen_sent))
    print "SAVED"