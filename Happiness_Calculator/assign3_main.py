'''
Purpose: The purpose of this program is to allow the user to enter a file containing a list of tweets and a file containing a list of keywords with specific
values that will allow them to calculate 'happiness' values  for specific regions. The happiness values are created through a series of calculations of the given inputs
Class: CS1026 002
Professor: Bryan Sarlo
Author: Sinthuja Jeevarajhan
'''
#imports the file that contains compute_tweets to calculate the happiness values
import sentiment_analysis
emptyList= []
#creates sentiment lists from 1-10 to hold the keywords that match the corresponding sentiment values

try:
    #ask user to enter the name of file containing the list of tweets
    tweets_FileName= input("Please enter the name of the tweets file: ")
    #ask user to enter the name of file containing the list of keywords
    keyword_FileName= input("Enter the value of the keywords file: ")
    #call the function compute tweets from the sentiment analysis file to compute the calculations
    x= sentiment_analysis.compute_tweets(tweets_FileName,keyword_FileName)
    #Display the results to the user
    print("Eastern Region: Happiness Score: %.3f" % x[0][0], ", Keyword Tweets in Region : %d" % x[0][1], ", Total Tweets in Region: %d" % x[0][2])
    print("Central Region: Happiness Score: %.3f" % x[1][0], ", Keyword Tweets in Region : %d" % x[1][1], ", Total Tweets in Region: %d" % x[1][2])
    print("Mountain Region: Happiness Score: %.3f" % x[2][0], ", Keyword Tweets in Region : %d" % x[2][1], ", Total Tweets in Region: %d" % x[2][2])
    print("Pacific Region: Happiness Score: %.3f" % x[3][0], ", Keyword Tweets in Region : %d" % x[3][1], ", Total Tweets in Region: %d" % x[3][2])

#executed if there was an error processing the file name entered by the user
except:
    print("That file does not exist.")





