from music import Music


def test_play():
    X=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",1)
    Y=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",3)
    Z=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",5)
    assert X.play()=='https://www.youtube.com/watch?v=1zd0Eqg04Kk'
    assert Y.play()=='https://www.youtube.com/watch?v=aTOu1g5-Z2M'
    assert Z.play()=='https://www.youtube.com/watch?v=1hZa60t8wSE'
    

    