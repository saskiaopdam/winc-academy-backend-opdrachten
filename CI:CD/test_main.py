import main

def test_index():
    assert main.index() == 'Hello, world!'
    
def test_cow():
    assert main.cow() == 'MOoooOo!'
    
def test_donkey():
    assert main.donkey() == 'Iaah, iaah!'
    
def test_duck():
    assert main.duck() == 'Kwa kwa!'