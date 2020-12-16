from music import Music


def test_play():
    X=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",1)
    Y=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",3)
    Z=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",5)
    assert X.play()=='https://www.youtube.com/watch?v=1zd0Eqg04Kk'
    assert Y.play()=='https://www.youtube.com/watch?v=aTOu1g5-Z2M'
    assert Z.play()=='https://www.youtube.com/watch?v=1hZa60t8wSE'
    
    output=Music("https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",1)
    assert output.get_links()==['https://www.youtube.com/watch?v=VlP5E5yen7I', 
                                'https://www.youtube.com/watch?v=1zd0Eqg04Kk', 
                                'https://www.youtube.com/watch?v=VltAuKIJNZE',
                                'https://www.youtube.com/watch?v=aTOu1g5-Z2M', 
                                'https://www.youtube.com/watch?v=0a-yqNc5JYY', 
                                'https://www.youtube.com/watch?v=1hZa60t8wSE',
                                'https://www.youtube.com/watch?v=NozOwySZiYA',
                                'https://www.youtube.com/watch?v=FoYyqHqbnxc', 
                                'https://www.youtube.com/watch?v=eOliwArdKPs',
                                'https://www.youtube.com/watch?v=6yTvuFy9_ik', 
                                'https://www.youtube.com/watch?v=oxGcr-KrlUA', 
                                'https://www.youtube.com/watch?v=86Rr_rTdzIo',
                                'https://www.youtube.com/watch?v=ueSgCa6KefQ',
                                'https://www.youtube.com/watch?v=o5G-Qtf_gac',
                                'https://www.youtube.com/watch?v=FwsL5qKzodg']
    

    