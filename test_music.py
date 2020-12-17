from music import Music


def test_play():
    # Playlist 1
    url = "http://www.youtube.com/feeds/videos.xml?playlist_id=PLsH19NHPTD44m-5CCyx5jKLKAGir3iL2L"
    m1 = Music(url=url, tarot=0)
    m2 = Music(url=url, tarot=10)
    m3 = Music(url=url, tarot=12)
    m4 = Music(url=url, tarot=20)
    m5 = Music(url=url, tarot=33)
    m6 = Music(url=url, tarot=41)

    assert m1.play() == "https://www.youtube.com/watch?v=i0A3-wc0rpw"
    assert m2.play() == "https://www.youtube.com/watch?v=McIYdE4s-gY"
    assert m3.play() == "https://www.youtube.com/watch?v=AGlKJ8CHAg4"
    assert m4.play() == "https://www.youtube.com/watch?v=rQD9EBCwlQc"
    assert m5.play() == "https://www.youtube.com/watch?v=Vab5GT1pd1k"
    assert m6.play() == "https://www.youtube.com/watch?v=5kJZuhyFFCQ"

    # Playlist 2
    X = Music(
        "https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
        1,
    )
    Y = Music(
        "https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
        3,
    )
    Z = Music(
        "https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
        5,
    )
    assert X.play() == "https://www.youtube.com/watch?v=1zd0Eqg04Kk"
    assert Y.play() == "https://www.youtube.com/watch?v=aTOu1g5-Z2M"
    assert Z.play() == "https://www.youtube.com/watch?v=1hZa60t8wSE"

    output = Music(
        "https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
        1,
    )
    assert output.get_links() == [
        "https://www.youtube.com/watch?v=VlP5E5yen7I",
        "https://www.youtube.com/watch?v=1zd0Eqg04Kk",
        "https://www.youtube.com/watch?v=VltAuKIJNZE",
        "https://www.youtube.com/watch?v=aTOu1g5-Z2M",
        "https://www.youtube.com/watch?v=0a-yqNc5JYY",
        "https://www.youtube.com/watch?v=1hZa60t8wSE",
        "https://www.youtube.com/watch?v=NozOwySZiYA",
        "https://www.youtube.com/watch?v=FoYyqHqbnxc",
        "https://www.youtube.com/watch?v=eOliwArdKPs",
        "https://www.youtube.com/watch?v=6yTvuFy9_ik",
        "https://www.youtube.com/watch?v=oxGcr-KrlUA",
        "https://www.youtube.com/watch?v=86Rr_rTdzIo",
        "https://www.youtube.com/watch?v=ueSgCa6KefQ",
        "https://www.youtube.com/watch?v=o5G-Qtf_gac",
        "https://www.youtube.com/watch?v=FwsL5qKzodg",
    ]
