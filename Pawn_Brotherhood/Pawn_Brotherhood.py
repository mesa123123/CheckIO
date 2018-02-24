
def safe_pawns(positions):
    return len(set([protected_pawn for protected_pawn in positions for defending_pawn in positions
                    if abs(ord(protected_pawn[0])- ord(defending_pawn[0])) == 1
                    and int(protected_pawn[1]) - int(defending_pawn[1]) == 1 ]))



