pm2 = "https://laurentgarnier.podia.com/pratiques-mathematiques-en-2de"
pm1 = "https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere"
# This program is an excerpt from pm1
pmt = "https://laurentgarnier.podia.com/pratiques-mathematiques-en-terminale-specialite-maths"
recommandation_superprof = "https://www.superprof.fr/ir/43048-e9e064"
annonce_superprof = "https://www.superprof.fr/reussissez-maths-niveau-etudes-esprit.html"
pr_glump = "https://youtu.be/f0hcfG6oW6A"
cl = "cours-laurentATtutanota.com"
affiliate = "https://laurentgarnier.podia.com/l-affiliation-pour-les-nuls"

def get_more(request, options):
    print(f"If you {request} you have 3 options:")
    for option in options: 
        print("-" * len(option.upper()))
        print(option)
        print("-" * len(option.upper()))
        
    like = input("Do you like my work? (Y|N) ")
    if like.upper() in {'Y', "YES"}:
        like_my_work = "If you like my work then think about leaving a recommendation on".upper()
        like_my_work += f" Superprof: {recommandation_superprof}"
        print(like_my_work)

    make_money = input("Do you want to make money with my work? (Y|N) ")
    if make_money.upper() in {'Y', "YES"}:
        become_affiliate = "https://laurentgarnier.podia.com/l-affiliation-pour-les-nuls"
        print(f"Become Affiliate: {become_affiliate}")
