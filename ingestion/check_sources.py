import urllib.robotparser
from urllib.parse import urlparse
import feedparser

FEEDS = {
    "VnExpress": "https://vnexpress.net/rss/tin-moi-nhat.rss",
    "TuoiTre":   "https://tuoitre.vn/rss/tin-moi-nhat.rss",
    "DanTri":    "https://dantri.com.vn/rss/home.rss",
}
UA = "NewsRAG-VN-student-project"

for name, url in FEEDS.items():
    print(f"\n=== {name} ===")
    feed = feedparser.parse(url, agent=UA)
    print("HTTP status:", feed.get("status"), "| số bài:", len(feed.entries))
    if feed.entries:
        e = feed.entries[0]
        print("Tiêu đề:", e.get("title"))
        print("Có published:", "published" in e, "->", e.get("published"))
        print("Độ dài summary:", len(e.get("summary", "")))
        print("Link:", e.get("link"))

    # kiểm tra robots.txt
    p = urlparse(url)
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
    try:
        rp.read()
        print("robots cho phép RSS:", rp.can_fetch(UA, url))
        if feed.entries:
            print("robots cho phép bài:", rp.can_fetch(UA, feed.entries[0].link))
        print("crawl-delay:", rp.crawl_delay(UA))
    except Exception as ex:
        print("Không đọc được robots:", ex)
