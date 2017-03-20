"""
This Script scrapes critic data for any movie from rottentomatoes
Script Version : 3.8.5
"""

from bs4 import BeautifulSoup
import re
import time
import requests
import csv

def writeto():
        rcnt = 0
        fcnt = 0
        fin = open('critic_review.txt', 'r')
        for line in fin:
            word=line.strip()
            if word == 'rotten':
                rcnt = rcnt + 1
            elif word == 'fresh':
                fcnt = fcnt + 1
            else:
                pass

        print (rcnt, fcnt)
        listBlank = []
        listBlank.append(rcnt)
        listBlank.append(fcnt)
        print(listBlank)

        with open('review.csv', 'w') as outcsv:
            #configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow([' ','Rotten', 'Fresh'])
            for i in range(0,1):
                #Write item to outcsv
                writer.writerow(["Critic", listBlank[0], listBlank[1]])

def run(url):
    moviename = input(">> ")
    moviename = moviename.lower()
    if ' ' in moviename:
        moviename = moviename.replace(" ", "_") #replace the whitespaces with underscores
    else:
        pass

    print("Scrapping", moviename)

    #pageNum=1 # number of pages to collect

    fw=open('critic_review.txt','w') # output file

    for p in range(1,51): # for each page

        print ('page',p)
        html=None
        pageLink=url+ moviename +'/reviews/?page='+str(p)+'&sort='

         # url for page 1

        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs


        if not html:continue # couldnt get the page, ignore

        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs
        if not reviews:
            moviename = moviename + '_2017'
            pageLink=url+ moviename +'/reviews/?page='+str(p)+'&sort='

             # url for page 1

            for i in range(5): # try 5 times
                try:
                    #use the browser to access the url
                    response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                    html=response.content # get the html
                    break # we got the file, break the loop
                except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                    print ('failed attempt',i)
                    time.sleep(2) # wait 2 secs


            if not html:continue # couldnt get the page, ignore

            soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html

            reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs
        else:
            pass

        for review in reviews:

            rating='NA' # initialize critic and text
            #ratingChunk=review.find('div',{'class':'review_icon icon small fresh'})
            if (review.find('div',{'class':'review_icon icon small fresh'})):
                rating = 'fresh'
                fw.write(rating+'\n')

            elif (review.find('div',{'class':'review_icon icon small rotten'})):
                 rating = 'rotten'
                 fw.write(rating+'\n')
            else:
                break                                                # rating=ratingChunk.text#.encode('ascii','ignore')
    fw.close()
    writeto()


if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/'
    run(url)
