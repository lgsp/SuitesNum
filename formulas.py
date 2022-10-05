def build_basic_formulas():
    arithmetic = {
        'rec' : ('Définition par récurrence', 'u(n + 1) = u(n) + r'),
        'exp0' : ('Définition explicite', 'u(n) = u(0) + n*r'),
        'expP' : ('Définition explicite générale', 'u(n) = u(p) + (n - p)*r'),
        'N' : ('S = 1 + ... + n', 'S = n * (n + 1) / 2'),
        'S0' : ('S(n) = u(0) + ... + u(n)', 'S(n) = (n + 1) * ( u(0) + u(n) ) / 2'), 
        'Sp' : ('S(n, p) = u(p) + ... + u(n)', 'S(n, p) = (n - p + 1) * ( u(p) + u(n) ) / 2'), 
    }
    geometric = {
        'rec' : ('Définition par récurrence', 'u(n + 1) = u(n) * q'),
        'exp0' : ('Définition explicite', 'u(n) = u(0) * q**n'),
        'expP' : ('Définition explicite générale', 'u(n) = u(p) * q**(n - p)'),
        'N' : ('S = 1 + q + ... + q**n', 'S = ( q**(n + 1) - 1 ) / ( q - 1 )'),
        'S0' : ('S(n) = u(0) + ... + u(n)', 'S(n) = u(0) * ( q**(n + 1) - 1 ) / ( q - 1 )'), 
        'Sp' : ('S(n, p) = u(p) + ... + u(n)', 'S(n, p) = u(p) * ( q**(n - p + 1) - 1 ) / ( q - 1 )'),
    }    
    return arithmetic, geometric


def print_formulas(topic, title):
    print(f"\n{title}\n")
    for k in topic: 
        for elt in topic[k]: 
            print(elt)
        print()



def watch_basic_formulas(arithmetic, geometric):
    menu = '''
    1) Suites arithmétiques
    2) Suites géométriques
    Q) Quitter
    Choix : '''
    cond = True
    while cond:
        choix = input(menu)
        if choix == '1': print_formulas(topic=arithmetic, title="Suites arithmétiques")
        elif choix == '2': print_formulas(topic=geometric, title="Suites géométriques")
        elif choix.upper() == 'Q': cond = False
        else: print('Entrer 1 ou 2 ou Q')