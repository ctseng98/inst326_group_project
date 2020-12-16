from music import Music


def test_get_links():
     x = Music(
            url= rss_feed_test,
        )
     assert get_links(x) == output
    