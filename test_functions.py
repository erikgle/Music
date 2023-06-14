from music import MusicScale
from music import notes_in


def test_notes_in():
    assert callable(notes_in)
    assert notes_in(['A', 'F#', 'C']) == [['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']]
    
    
def test_find_scale():
    g = MusicScale('G')
    assert callable(g.find_scale)
    assert g.find_scale() == ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']


    
def test_chord_progression():
    c = MusicScale('C')
    assert callable(c.chord_progression)
    assert c.chord_progression([1,4,5]) == {1: ['C', 'E', 'G'], 
                                            4: ['F', 'A', 'C'], 
                                            5: ['G', 'B', 'D']}
    assert c.chord_progression(['C','F','G']) == {'C': ['C', 'E', 'G'], 
                                                  'F': ['F', 'A', 'C'], 
                                                  'G': ['G', 'B', 'D']}
