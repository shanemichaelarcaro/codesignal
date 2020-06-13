def tennisSet(score1, score2):
    if score1 == 6 or score2 == 6:
        if max(score1, score2) == 7 or min(score1, score2) < 5:
            return True
        return False
    if max(score1, score2) == 7 and min(score1, score2) != 7 and min(score1, score2) >= 5:
        return True
    else:
        return False