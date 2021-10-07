def creer_file():
    '''
    créer une file (vide)
    '''
    return []

def enfiler(f, elt):
    '''
    placer un élément en file d'attente
    '''
    f.append(elt)
    
def longueur(f):
    '''
    donne la longueur de la file
    '''
    return len(f)

def est_vide(f):
    '''
    vérifier si la file est vide ou non
    '''
    return longueur(f) == 0
def tete(f):
    '''
    retourne le premier élément entrée
    '''
    if not est_vide(f):
        return f[0]
    else:
        print("la pile est vide")

def defiler(f):
    '''
    faire sortir le premier élément de la file
    '''
    if not est_vide(f):
        return f.pop(0)
    else :
        print("la file est vide")
        