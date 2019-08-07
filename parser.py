import feedparser

def FeedBurner():
    myfeed = feedparser.parse("http://www.couponchief.com/rss/")

    for item in myfeed['items']:
        print item.title
        print item.link
        print item.description
        print ""

FeedBurner()


