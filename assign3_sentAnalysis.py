#initiazlie the lists that will contain the keywords according to their value
sentiment1= []
sentiment2= []
sentiment3= []
sentiment4= []
sentiment5= []
sentiment6= []
sentiment7= []
sentiment8= []
sentiment9= []
sentiment10= []
emptyList= []
#compute tweets function that opens the files from the user analyzes their sentiment values and returns the average, total tweets and keyword tweets for each region
def compute_tweets(tweets, keywords):
    try:
        keywords= open(keywords, "r", encoding="utf-8")
        tweets= open(tweets, "r", encoding="utf-8")
        analyze_keywords(keywords)
        return tweet_analysis(tweets)
    except:
        return emptyList

def analyze_keywords(keywords):
    #reads in each line of the keywords file
    line=keywords.readline()
    global sentiment1
    global sentiment2
    global sentiment3
    global sentiment4
    global sentiment5
    global sentiment6
    global sentiment7
    global sentiment8
    global sentiment9
    global sentiment10

    for line in keywords:

        #splits the line based on the dilimeter comma
        words= line.rsplit(",")
        key_value= words[1].strip("/n")

        #if sentiment value is 1 then puts the keyword into the sentiment 1 list
        if int(key_value) == 1:
            sentiment1.append(words[0])
        elif int(key_value) == 2:
            sentiment2.append(words[0])
        elif int(key_value) == 3:
            sentiment3.append(words[0])
        elif int(key_value) == 4:
            sentiment4.append(words[0])
        elif int(key_value) == 5:
            sentiment5.append(words[0])
        elif int(key_value) == 6:
            sentiment6.append(words[0])
        elif int(key_value) == 7:
            sentiment7.append(words[0])
        elif int(key_value) == 8:
            sentiment8.append(words[0])
        elif int(key_value) == 9:
            sentiment9.append(words[0])
        elif int(key_value) == 10:
            sentiment10.append(words[0])

#function reads tweets, gets rid of punctuation and seperates into seperate tweet words, lat, long lists
def tweet_analysis(tweets):
    tweet_Words =[]
    lat_Coordinate= []
    long_Coordinate= []

    line= tweets.readline()
    for line in tweets:
        #eliminates the punctuation within the tweet and splits the function into 5 indexes
        tweet= line.replace("!", "").replace("[", "").replace("\n","").replace("]", "").replace("@", "").replace("#", "").split(" ", 5)
        #elimanates the comma in the latitude and longitude
        tweet[0]= tweet[0].replace(",", "")
        #adds the 5th index- the tweet to the list of tweets
        tweet_Words.append(tweet[5])
        #adds the float value of the first value which is the longitude coordinate to the list
        lat_Coordinate.append(float(tweet[0]))
        #adds the float value of the first value which is the longitude coordinate to the list
        long_Coordinate.append(float(tweet[1]))

        #calls the function location finder, finds the region of that tweet

    return location_finder(tweet_Words, lat_Coordinate, long_Coordinate)
#function calculates the sentiment of the tweet based on the region
#returns the average sentiment and number of keyword tweets in that region
def sentiment_calculation(region):
        #refer to the global lists created
        global sentiment1
        global sentiment2
        global sentiment3
        global sentiment4
        global sentiment5
        global sentiment6
        global sentiment7
        global sentiment8
        global sentiment9
        global sentiment10

        key=0
        averagesentiment= 0
        for i in range(0, len(region)):
            #strips the punctuation and splits the line into individual words
            counter= False
            sentiment=0
            keywordcounter= 0
            tweetWords= region[i].strip('"[]#,@#$%&*,.?:;!').split(" ")
            #assigns each keyword a value that was specified in the value
            for word in tweetWords:
                if word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment1:
                    #adds sentiment
                    sentiment+= 1
                    #adds counter
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment2:
                    sentiment+= 2
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment3:
                    sentiment+= 3
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment4:
                    sentiment+= 4
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment5:
                    sentiment+= 5
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment6:
                    sentiment+= 6
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment7:
                    sentiment+= 7
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment8:
                    sentiment+= 8
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment9:
                    sentiment+= 9
                    counter= True
                    keywordcounter+= 1
                elif word.lower().strip('"[]#,@#$%&*,.?:;!') in sentiment10:
                    sentiment+= 10
                    counter= True
                    keywordcounter+= 1
            if counter == True:
                key += 1 #the number of keywords is the value of the counter

            #avoids divison by 0 error
            if sentiment != 0:
                #calculates the average sentiment in the region
                sentiment= sentiment/keywordcounter
                averagesentiment= sentiment + averagesentiment

        length=len(region)
        finalsentiment= averagesentiment/key
        #creates a tupule with the three values of happiness score, number of keyword tweets and the total tweets in the region
        return finalsentiment, key, length
#function to find the region of each time zone
def location_finder(tweet_Words, lat_Coordinate, long_Coordinate):
    #create lists to store the tweets according to their region
    finalresults= []
    easternTweets= []
    centralTweets= []
    mountainTweets= []
    pacificTweets= []

    length_list= len(lat_Coordinate)
    for i in range(0, length_list):
        #checks to see if latitude is within the entire region
        if 49.189787 >= lat_Coordinate[i] >= 24.660845:
            if -67.444574 >= long_Coordinate[i] >= -87.518395:
                #if tweet is in this region it appends the tweet to the corresponding region
                easternTweets.append(tweet_Words[i])
            elif -87.518395 > long_Coordinate[i] >= -101.998892:
                centralTweets.append(tweet_Words[i])
            elif -101.998892 > long_Coordinate[i] >= -115.236428:
                mountainTweets.append(tweet_Words[i])
            elif -115.236428 > long_Coordinate[i] >= -125.242264:
                pacificTweets.append(tweet_Words[i])
    #calculates the sentiment of functions using the following sentiment calculation function
    eastern_Sentiment= sentiment_calculation(easternTweets)
    central_Sentiment= sentiment_calculation(centralTweets)
    mountain_Sentiment= sentiment_calculation(mountainTweets)
    pacific_Sentiment= sentiment_calculation(pacificTweets)
    #calls the results function that put the results in a tuple
    finalresults.append(eastern_Sentiment)

    finalresults.append(central_Sentiment)

    finalresults.append(mountain_Sentiment)

    finalresults.append(pacific_Sentiment)
    #returns a list containing a series of tupules with the average, keyword tweets, total tweets for the 4 regions
    easternTweets.clear()
    centralTweets.clear()
    mountainTweets.clear()
    pacificTweets.clear()
    return finalresults
