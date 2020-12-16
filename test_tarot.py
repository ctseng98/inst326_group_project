from tarot import Tarot



def test_image():
    "this is for happy path"
    C=Tarot(1)
    assert C.image(5) == '/images/tarotcards/tarot-hierophant.jpg'
    assert C.image(55)=='/images/tarotcards120px/tarot-swords-02.jpg'
    assert C.image(71) == '/images/tarotcards120px/tarot-pentacles-04.jpg'
    
    
    "this is for edge part"
    assert C.image(1) == '/images/tarotcards/tarot-magician.jpg'
    assert C.image(22) == '/images/tarotcards120px/tarot-wands-14.jpg'
    assert C.image(23)=='/images/tarotcards120px/tarot-wands-13.jpg'
    assert C.image(36) == '/images/tarotcards120px/tarot-cups-14.jpg'
    assert C.image(37) == '/images/tarotcards120px/tarot-cups-13.jpg'
    assert C.image(50) == '/images/tarotcards120px/tarot-swords-14.jpg'
    assert C.image(51)=='/images/tarotcards120px/tarot-swords-13.jpg'
    assert C.image(77) == '/images/tarotcards120px/tarot-pentacles-10.jpg'
    


def test_num():
     x = Tarot(1)
     
     assert x.num(label = "Ace") == 1
     assert x.num(label = "Page") == 11
     assert x.num(label = "King") == 14
     assert x.num(label = "Ten") == 10   
    