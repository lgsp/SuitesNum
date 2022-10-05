import random
from pub import *
from formulas import *
from scores import *
from difflib import SequenceMatcher


    
def practice_basics(topic):
    score = 0
    attempts = 0
    for key in topic:
        attempts += 1
        exercice = input(f"{topic[key][0]} : ")
        solution = topic[key][1]
        score = incr_score(score, condition=exercice==solution, answer=solution)
    
    final_score(attempts, score)
    review_formulas = input("Veux-tu revoir les formules ? (O)ui ou (N)on ? ")
    if review_formulas.upper() == 'O': watch_basic_formulas(arithmetic, geometric)

def arith(u_0, r, n): return round(u_0 + n * r, 2)
def sum_arith(p, u_p, r, n, u_n): return (n - p + 1)*(u_p + u_n)/2
def geom(u_0, q, n): return round(u_0 * q**n, 2)
def sum_geom(p, u_p, q, n, u_n): return u_p*(q**(n - p + 1) - 1)/(q - 1)    

def numerical_practice():
    attempts = 0
    score = 0
    cond = True
    while cond:
        u_0 = round(random.uniform(-10, 10), 2) 
        q = round(random.uniform(-10, 10), 2)
        r = round(random.uniform(-10, 10), 2)
        while u_0 * q * r == 0:
            u_0 = round(random.uniform(-10, 10), 2)
            q = round(random.uniform(-10, 10), 2)
            while q == 1:
                q = round(random.uniform(-10, 10), 2)
            r = round(random.uniform(-10, 10), 2)
        
        m, n = random.randint(0, 10), random.randint(0, 10)
        u_m, u_n = arith(u_0, r, m), arith(u_0, r, n) 
        s, t = random.randint(0, 10), random.randint(0, 10)
        v_s, v_t = geom(u_0, q, s), geom(u_0, q, t)

        def nature(i0, i1, ui0, ui1, name):
            q_nat = f"Soient {name}_{i0} = {ui0} et {name}_{i1} = {ui1}, "
            q_nat += f"quelle est la nature de la suite {name} ?\nRépondre au choix :\n"
            q_nat += f"La suite {name} est arithmétique\n"
            q_nat += f"La suite {name} est géométrique\n"
            q_nat += f"La suite {name} est n'est ni arithmétique ni géométrique\n"
            return q_nat

        def raison(nature, name, n, u_n, u_0):
            q_raison = f"Déterminer la raison de la suite {nature} {name} "
            q_raison += f"telle que {name}_{n} = {u_n} et {name}_0 = {u_0}"
            return q_raison

        def calcul(name, final_index, nature, i0, ui0, i1, ui1):
            q_calcul = f"Calculer {name}_{final_index} sachant que {name} "
            q_calcul += f"est {nature} et {name}_{i0} = {ui0} et u_{i1} = {ui1}"
            return q_calcul

        def somme(initial_index, final_index, name, uii, ufi):
            q_sum = f"Calculer la somme S_{initial_index},{final_index} = "
            q_sum += f"{name}_{initial_index} + ... + {name}_{final_index}\n"
            q_sum += f"S_{initial_index},{final_index} = {uii} + ... + {ufi}"
            return q_sum
            
        questions = [
            nature(i0=m, i1=n, ui0=u_m, ui1=u_n, name="u"),
            raison(nature="arithmétique", name="u", n=n, u_n=u_n, u_0=u_0),
            calcul(name="u", 
                   final_index=s+t, 
                   nature="arithmétique", 
                   i0=m, 
                   ui0=u_m, 
                   i1=n, 
                   ui1=u_n),
            somme(initial_index=min(m,n), 
                  final_index=m+n, name="u", 
                  uii=arith(u_0, r, min(m, n)), 
                  ufi=arith(u_0, r, m+n)),
            nature(i0=s, i1=t, ui0=v_s, ui1=v_t, name="v"),
            raison(nature="géométrique", name="v", n=t, u_n=v_t, u_0=u_0),
            calcul(name="v", 
                   final_index=m+n, 
                   nature="géométrique",
                   i0=s, 
                   ui0=v_s, 
                   i1=t, 
                   ui1=v_t),
            somme(initial_index=min(s,t), 
                  final_index=s+t, name="v", 
                  uii=arith(u_0, q, min(s, t)), 
                  ufi=arith(u_0, q, s+t))
        ]
    
        answers = [
            "La suite u est arithmétique",
            r,
            arith(u_0, r, s+t),
            sum_arith(p=min(m, n), 
                      u_p=arith(u_0, r, min(m, n)), 
                      r=r, 
                      n=m+n, 
                      u_n=arith(u_0, r, m+n)),
            "La suite v est géométrique",
            q,
            geom(u_0, q, m+n),
            sum_geom(p=min(s, t), 
                     u_p=geom(u_0, q, min(s, t)), 
                     q=q, 
                     n=s+t, 
                     u_n=geom(u_0, q, s+t))
        ]

        q_and_a = dict(zip(questions, answers))
        for q in q_and_a:
            print(q)
            right_ans = q_and_a[q]
            if isinstance(right_ans, float) or isinstance(right_ans, int):
                print("Arrondir à 2 décimales")
                user_ans = float(input("Votre réponse = "))
                score = incr_score(score, abs(right_ans - user_ans) < 0.01, right_ans)
                attempts += 1
            else:
                user_ans = input("Votre réponse = ")
                similarity = SequenceMatcher(a=right_ans, b=user_ans).ratio()
                score = incr_score(
                    score, 
                    similarity > 0.95, 
                    right_ans)
                if similarity < 0.95:
                    score -= 1
                    score += similarity
                    score = round(score, 2)
                    print(f"Votre réponse est juste à {round(similarity, 2)*100}%.")
                    print(f"Ton score est désormais {score}")
                attempts += 1
            continuer = input("Souhaitez-vous continuer ? (O|N) ")
            if continuer.upper() == "N": 
                cond = final_score(attempts, score)
                break
        cond = final_score(attempts, score)


arithmetic, geometric = build_basic_formulas()       
menu = '''
0) Créer des fichiers de leçons
1) Revoir les formules de base
2) Pratiquer les suites arithmétiques
3) Pratiquer les suites géométriques
4) Pratiquer avec des valeurs numériques
5) Concrete HARD WORK
6) Do you find it too much difficult?
7) Do you want more?
8) Do you find it too easy?
9) Do you want private lessons with me?
Q) Quit
Your choice: '''
cond = True
while cond:
    choice = input(menu)
    if choice == '0':
        create_lesson_files()
    elif choice == '1':
        watch_basic_formulas(arithmetic, geometric)
    elif choice == '2':
        practice_basics(arithmetic)
    elif choice == '3':
        practice_basics(geometric)
    elif choice == '4':
        numerical_practice()
    elif choice == '6':
        request = "find these exercises too much difficult"
        options = [
            f"Review previous level: {pm2}", 
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}"
        ]
        get_more(request, options)     
    elif choice == '7':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice == '8':
        request = "want private lessons with me"
        options = [
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"If you are okay to pay me with bitcoins you can contact me at: {cl}",
            f"Join my affiliate program to access to Podia chat: {affiliate}"
        ]
        get_more(request, options)
    elif choice == '9':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice.upper() == 'Q':
        cond = False
        request = "want to leave"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
        print('Goodbye. See you soon.')
    else:
        print("ERROR!!! Please type '1' or '2' or 'Q'")
    

    