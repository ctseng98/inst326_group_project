from music import Music
import feedparser


def test_get_links():
     url = "http://www.youtube.com/feeds/videos.xml?playlist_id=PLsH19NHPTD44m-5CCyx5jKLKAGir3iL2L"
     feed = feedparser.parse(url) 
     assert get_links(url) == output
    