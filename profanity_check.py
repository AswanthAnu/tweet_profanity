def profanity_score(tweet, slurs):
    words = tweet.split()
    score = 0
    for word in words:
        if word in slurs:
            score += 1
    return score

def get_profanity_scores(tweet_file, slurs):
    scores = []
    with open(tweet_file, 'r') as f:
        for line in f:
            tweet = line.strip().lower()
            score = profanity_score(tweet, slurs)
            scores.append(score)
    return scores

def unpack_slur(slur_file):
    slurs = []
    with open(slur_file, 'r') as f:
        for line in f:
            slur = line.strip().lower()
            slurs.append(slur)
    return slurs

slurs = unpack_slur('slurs.txt')
scores = get_profanity_scores('tweets.txt', slurs)
print(scores)
