# Spicy Hot Internet Topics

Using the MAX text sentiment analysis model provided by IBM, create a discord bot that filters selected subreddit content.

# Installation
1. Set up an instance with the IBM text sentiment classifier at https://github.com/IBM/MAX-Text-Sentiment-Classifier follow instructions given at the README file there.
2. In the discordBot.py file, edit line 70 with the discord channel id you want your bot to send posts to, and edit line 88 for your bot's token.
3. This project assumes you have the text classifier installed locally, if not you can change the url on line 13 at getSentiment.py

# Usage
* Every 10 minutes or so, the bot will go through a list of controversial subreddits and select the most controversial post based on title.
* You can also invoke ```!rate "text"``` to have the given text's sentiment classified.
