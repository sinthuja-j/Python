Happiness Score Calculation Program

📝 Overview

The Happiness Score Calculation Program analyzes tweets based on sentiment values tied to specific keywords. It calculates the 'happiness' score for different regions (Eastern, Central, Mountain, and Pacific) based on the presence of keywords in the tweets. The program utilizes sentiment values (ranging from 1 to 10) to compute the average sentiment for each region and provides a summary of the results.

The happiness score is derived through multiple calculations using user-provided files containing tweets and keywords with associated sentiment values.

🔑 Key Features

Happiness Score Calculation: Computes a happiness score for tweets in each region based on sentiment values associated with keywords.
Region-based Analysis: Divides tweets into four U.S. regions (Eastern, Central, Mountain, and Pacific) based on geographical coordinates (latitude and longitude).
Keyword Sentiment: Utilizes keywords that are associated with sentiment values ranging from 1 to 10 to determine the overall sentiment of the tweets.
Results Summary: Displays the happiness score, number of keyword tweets, and total tweets for each region.

⚙️ How It Works

The program prompts the user to input the name of the file containing the list of tweets and the file containing the keywords with their corresponding sentiment values.
Sentiment Calculation:

The program reads and analyzes the provided keywords file to classify keywords into sentiment categories (1 to 10).
It processes the tweets by extracting the relevant information (latitude, longitude, and tweet content) and analyzes the presence of keywords.

Region-based Sentiment:

Based on the geographical coordinates in each tweet, the program categorizes tweets into one of the four regions: Eastern, Central, Mountain, and Pacific.
Results:

The program calculates and prints:

Happiness Score: Average sentiment of the keywords in the region.
Keyword Tweets: The number of tweets that contain at least one keyword.
Total Tweets: The total number of tweets in the region.
Error Handling:

If the file paths are incorrect or files are not found, the program will print an error message and exit gracefully.

🛠️ Technologies Used

Python: The program is written in Python and utilizes basic file handling and string operations to read, analyze, and compute the necessary data.
Sentiment Analysis: Keywords and sentiment values are used to calculate the sentiment score for tweets.
