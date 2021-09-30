def creer_pile():
    '''
    créér une pile
    '''
    return []
def empiler(p,x):
    '''
    ajouter une élément à la pile
    '''
    return p.append(x)
def hauteur(p):
    '''
    Donner la taille de la pile
    '''
    return len(p)
def est_vide(p):
    '''
    tester si la pile est vide ou non
    '''
    return hauteur(p) == 0
def sommet(p):
    '''
    donner l'élément au sommet
    '''
    return p[-1]
def depiler(p):
    '''
    si n'est pas vide, faire sortir le dernier émlément de la pile
    '''
    if est_vide(p):
        print("La pile est vide!")
    else:
        return p.pop()
if __name__ == "__main__":
    p = creer_pile()
    print(hauteur(p))
    N = int(input("saisir un nombre d'éléments : "))
    for i in range(N):
        empiler(p, i)
    print(p)
    print(hauteur(p))
    for i in range(hauteur(p)):
        depiler(p)
    print(p)


    
