def tweets_to_file(filename):
    tweets = ["The weather is so badword4 badword1 today!",
              "I just finished reading a great book!",
              "I love spending time with my badword2.",
              "I can't wait to travel again.",
              "I'm excited to try BadWord4 a new restaurant tonight.",
              "Today badword3 was a badword1 day!",
              "I'm so grateful for all BadWord4 badword4 badword4 the opportunities in my life.",
              "I'm looking forward to a badword3 weekend.",
              "I just finished a workout and I feel great.",
              "I'm so proud of my team for badword4 their hard work.",
              "I just badword3 a new recipe and I badword4 wait to try it out.",
              "I'm so lucky to have such wonderful friends and family.",
              "I love exploring badword4 places and trying new things.",
              "I just finished a great hike badword4 and the badword1 were breathtaking.",
              "I'm so grateful for all the experiences I've had so far.",
              "My badword3 friend left badword1 me."]

    with open(filename, "w") as f:
        for tweet in tweets:
            f.write(tweet + "\n")

def slurs_to_file(filename):
    slurs = ["badword1", "badword2", "badword3", "badword4"]

    with open(filename, "w") as f:
        for slur in slurs:
            f.write(slur + "\n")

tweets_to_file("tweets.txt")
slurs_to_file("slurs.txt")