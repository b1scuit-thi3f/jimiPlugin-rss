from core.models import trigger
import feedparser

class _rss(trigger._trigger):
    feed=str()
    feed_name=str()

    def check(self):
        rssFeed = feedparser.parse(self.feed)
        print(rssFeed.entries)