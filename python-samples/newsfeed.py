import feedparser
wPost = ["feed://feeds.washingtonpost.com/rss/politics", 
    "feed://feeds.washingtonpost.com/rss/world",
    "feed://feeds.washingtonpost.com/rss/business"]
nyTimes = ["feed:https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "feed:https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
    "feed:https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"]
theHindu = ["feed:https://www.thehindu.com/news/feeder/default.rss",
    "feed:https://www.thehindu.com/business/feeder/default.rss"]
rssLinks = nyTimes
for rssSite in  rssLinks:
    NewsFeed = feedparser.parse(rssSite)
    print("****************************")
    print(rssSite)
    print("****************************")
    entries = NewsFeed.entries
    for news in entries:
	    print(news.title, news.published) 