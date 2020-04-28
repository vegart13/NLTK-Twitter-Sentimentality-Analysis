# NLTK-Twitter-Sentimentality-Analysis
Using NLTK (Natural Language Toolkit) this program evaluates the sentimentality of tweets with inserted keywords

You will need to install both GetOldTweets3 as well as NLTK. Both are available through pip.

After NLTK is installed you will have to open up the NLTKinstall.py file and run it. Then select the top option (all) to install everything. This will take a while but once you've done this it should be able to run and you can opt to delete NLTKinstall.py.

This program does the following:
1. Fetch tweets using GetOldTweets3 using the parameters of:
- What keywords would you like to search for in tweets
- How far back in time would you like to search for tweets
- What is the maximum amount of tweets you would like to retrieve (note that a number pushing above 2000 can take a while)
2. Store the text from all the tweets into a variable
3. Cleans/converts the text removing punctuations and special characters
4. Tokenizes the text by dividing all the words into units and excluding stop words into a list with NLTK
5. Analyzes sentimentality of the tokenized and processed list of text from tweets
6. Prints out values as well as a notation of whether the general sentiment is either positive or negative.
