import feedparser

d = feedparser.parse('http://www.reddit.com/.rss')

print d['feed']['title']
#title of feed
print d.headers
print len(d['entries'])
#h_length

for post in d.entries:
    print post.title + ": " + post.link + " "
    #post and their titles/links
