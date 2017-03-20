"""
This Script performs Sentimental Analysis on the the scraped reviews
Script Version : 3.3.2
"""

import time
import csv


def writeto():
    rcnt = 0
    fcnt = 0
    fine = open('sentiment.txt', 'r')
    for line in fine:
        word=line.strip()
        if word == '-1':
            rcnt = rcnt + 1
        elif word == '1':
            fcnt = fcnt + 1
        else:
            pass

    print (rcnt, fcnt)
    listBlank = []
    listBlank.append(rcnt)
    listBlank.append(fcnt)
    print(listBlank)
    fine.close()

    with open('review.csv', 'a+') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        #writer.writerow(['Rotten', 'Fresh'])
        for i in range(0,1):
                #Write item to outcsv
            writer.writerow(["User",listBlank[0], listBlank[1]])


#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set() #no dups , fast search
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    decisions=[]
    reviews=[]
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')

    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        posList=[] #list of positive words in the review
        negList=[] #list of negative words in the review

        line=line.lower().strip()
        reviews.append(line)


        words=line.split(' ') # slit on the space to get list of words
        fw = open('sentiment.txt', 'w')
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                posList.append(word) #update the positive list for this review

            if word in negLex: # if the word is in the negative lexicon
                negList.append(word) #update the negative list for this review

        decision=0  # 0 for neutral
        if len(posList)>len(negList): # more pos words than neg
            decision=1 # 1 for positiv
        elif len(negList)>len(posList):  # more neg than pos
            decision=-1 # -1 for negative
        decisions.append(decision)

    fin.close()
    return reviews, decisions


if __name__ == "__main__":
    reviews,decisions=run('reviews.txt')
    fw = open('sentiment.txt', 'w')
    for i in range(len(reviews)):
        time.sleep(1)
        fw.write(str(decisions[i]) + "\n")
        print(reviews[i], decisions[i])
    fw.close()
    writeto()
