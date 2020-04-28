import string
from datetime import date
import GetOldTweets3 as got
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_tweets():
    # Using GetOldTweets we are able to retrieve tweets older than what the API allows on basic access
    # Inputs are taken to give this program some flexibility. SearchString, StartDate and EndDate are all strings
    # while MaxTweets is an integer
    SearchString = input('What would you like to search for on Twitter? ')
    StartDate = input(
        'How far in time would you like to go back?' + ' Year-Month-Day ')
    # Set's the end-date until today since it starts from the back it felt unneccesary to include an end date.
    # Length will be determined with amount of tweets fetched
    EndDate = str(date.today())
    MaxTweets = int(input(
        'What\'s the maximum number of tweets you would like to retrieve? '))

    # TweetCriteria is inherited from
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(SearchString)\
        .setSince(StartDate)\
        .setUntil(EndDate)\
        .setMaxTweets(MaxTweets)

    # The list objects are saved into a variable named 'tweets'
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Iterates through the tweets list then stores them in tweet
    # Gets the text and store it as a list inside text_tweets
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


# Converts the retrieved tweet data into text for it to be processed
text = " "
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text

# Converts text into lower case for sentimentality purposes
lower_case = text.lower()

# Convert lower case text into a cleaned version. The punctuation excludes special characters
# Str 1 ('') specifies list of characters that need to be replaced
# Str 2 ('') specifies list of characters with which the str 1 needs to be replaced with
# Str 3 (string.punctuation) specified the list of characters that needs to be deleted
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Breaks down a sentence and splits it into individual words into a list
# Uses NLTK to both remove stop words and clean the text up in whatever language you would like

tokenized_words = word_tokenize(cleaned_text, 'english')

# The final list of words from the text that's being analyzed
final_words = []

# Excludes words that appear in the stop_words list, adding the rest to final_words list
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Function to print polarity of the sentimality


def sentiment_analyzer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print('The sentiment for your search is negative')
    elif pos > neg:
        print('The sentiment for your search is positive ')
    else:
        print('The sentiment for your search is neutral')
    print(score)


sentiment_analyzer(cleaned_text)
