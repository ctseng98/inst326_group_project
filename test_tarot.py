from tarot import Tarot



def test_image():
    "this is for happy path"
    C=Tarot(1)
    assert C.image(5) == '/images/tarotcards/tarot-emperor.jpg'
    assert C.image(55)=='/images/tarotcards120px/tarot-swords-01.jpg'
    assert C.image(71) == '/images/tarotcards120px/tarot-pentacles-03.jpg'
    
    
    "this is for edge part"
    assert C.image(1) == '/images/tarotcards/tarot-fool.jpg'
    assert C.image(22) == '/images/tarotcards/tarot-world.jpg'
    assert C.image(23)=='/images/tarotcards120px/tarot-wands-14.jpg'
    assert C.image(36) == '/images/tarotcards120px/tarot-wands-10.jpg'
    assert C.image(37) == '/images/tarotcards120px/tarot-cups-14.jpg'
    assert C.image(50) == '/images/tarotcards120px/tarot-cups-10.jpg'
    assert C.image(51)=='/images/tarotcards120px/tarot-swords-14.jpg'
    assert C.image(78) == '/images/tarotcards120px/tarot-pentacles-10.jpg'
    
    
