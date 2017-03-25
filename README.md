# Slick-Flick

Slick-Flick is a Python Program that scrapes reviews of any movie from Rotten Tomatoes that is provided by both, the common user and the movie critic. Then, Sentimental Analysis is applied on the reviews to determine if the review is either *Fresh* or *Rotten*. The results are pushed into the a csv file and visualized via Tableau for better data understanding.

## Steps to run the program

### 1. Step One:
> Run scrape.py

User reviews are scraped and saved into `reviews.txt`

### 2. Step Two:
> Run critic_scrape.py

* Either `Fresh` or `Rotten` is written into `critic_review.txt` based on the scraped critic review. 
* The results are then added into the `review.csv` 

`Note: The values that are added into review.csv file are percentage values`

### 3. Step Three:
> Run user_sentiment.py

![logan_review](https://cloud.githubusercontent.com/assets/15202558/24163146/1dd3baf4-0e40-11e7-851f-1979c8042386.png) ![getout_review](https://cloud.githubusercontent.com/assets/15202558/24171258/14644a0a-0e5a-11e7-9380-10916f554b40.png)
