def incr_score(score, condition, answer):
    if condition:
        score += 1
        print(f"Bien joué ! Ton score actuel est : {score}")
    else:
        print(f"Faux ! Ton score est toujours : {score}")
    print(f"La bonne réponse était : {answer}")
    return score


def final_score(attempts, score):
    print(f"Ton score final est : {score}")
    if attempts < 2: print(f"Tu as fait {attempts} tentative.")
    else: print(f"Tu as fait {attempts} tentatives.")
    print(f"Donc ton pourcentage de succès est {100*score/attempts:.2f}%")
    ggb = "https://geogebra.org/classic"
    print(f"Va voir le site Geogebra pour expérimenter avec différentes valeurs : {ggb}")
