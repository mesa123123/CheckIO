from Pawn_Brotherhood import safe_pawns

def test_one():
    assert(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6)

def test_two():
    assert(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1)