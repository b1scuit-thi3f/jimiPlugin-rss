from core.models import trigger
import feedparser, datetime, time

class _rss(trigger._trigger):
    feed=str()
    feed_name=str()
    lastEntryTimestamp = int()
    onlyNew = bool()

    def check(self):
        rssFeed = feedparser.parse(self.feed)
        for entry in rssFeed["entries"]:
            if self.onlyNew:
                if time.mktime(entry["published_parsed"]) > self.lastEntryTimestamp:
                    self.result["events"].append(entry)
            else:
                self.result["events"].append(entry)
        self.lastEntryTimestamp = datetime.datetime.now().timestamp()
        self.update(["lastEntryTimestamp"])