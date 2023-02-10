# Profanity of each Twitter tweets
This repository contains a simple Python script that filters out profanity from tweets stored in a text file. The script will output the profanity score for each tweet in the tweets.txt file.


Assumptions
- The tweet text file contains one tweet per line, with no extra information.
- The slur text file contains one slur per line, with no extra information.
- The slurs and tweet in the slur text file and tweet text file are case-insensitive, i.e., they match both uppercase and lowercase versions of the slurs.
- The script performs a simple count of the number of slurs present in each tweet and returns the score for each tweet.
- The assumption is that all the tweets are in English and the slurs used are also English words.
## Running the Script
Clone the repository to your local machine. 

Run the following two code:
```
python file_creator.py   
python profinity_check.py
```
The script will output the profanity score for each tweet in the tweets.txt file.
