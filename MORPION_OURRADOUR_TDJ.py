# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:11:29 2021

@author: 33783
"""

import copy
from math import inf as infinity


    
grille= [['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)],['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)], ['. ' for i in range(12)]]


def AfficherGrille():
        grille
        retour='   1 2 3 4 5 6 7 8 9 10 11 12\n'
        for i in range(12):
            if i<9:
                retour += str(i+1) + "  "
            else:
                retour += str(i+1) + " "
            for j in range(12):   
                if j<9:
                    retour += str(grille[i][j])
                else:
                    retour += ' ' +str(grille[i][j])
                    
            retour += '\n'
        print(retour)

def VerifPartie(grille): 
     fini = False
     croix = False
     for i in range(9):
        for j in range(9):
         
         test = grille[i][j]
         if(test=='X '):
             croix = True
         if(test=='O ' or test=='X '):
           if(i==0 and j==0):
               if(grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]==grille[i+3][j+3]):
                   fini=True
            
           if(i<4 and j<4):
            if (grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j] or grille[i][j]==grille[i][j+1]==grille[i][j+2]==grille[i][j+3]):
                #print('Fini')
                fini = True  
           if(i>3 and i<10 and j<4):
            if (grille[i][j]==grille[i+1][j+1]==grille[i+3][j+3]==grille[i+2][j+2] or grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j] or grille[i][j]==grille[i-1][j]==grille[i-2][j]==grille[i-3][j] or grille[i][j]==grille[i-1][j+1]==grille[i-2][j+2]==grille[i-3][j+3]):
                #print('Fini')
                fini = True  
           if(i>9 and j<4):
            if (grille[i][j]==grille[i][j-1]==grille[i][j-3]==grille[i][j-2]):
                #print('Fini')
                fini = True  
           if(i<4 and j>3 and j<10):
            if (grille[i][j]==grille[i][j-1]==grille[i][j-3]==grille[i][j-2] or grille[i][j]==grille[i][j+1]==grille[i][j+3]==grille[i][j+2]):
                #print('Fini')
                fini = True  
           if(i>3 and j>3 and i<10 and j<10):
            if (grille[i][j]==grille[i+1][j+1]==grille[i+3][i+3]==grille[i+2][i+2] or grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j] or grille[i][j]==grille[i][j+1]==grille[i][j+2]==grille[i][j+3] or grille[i][j]==grille[i-1][j-1]==grille[i-2][j-2]==grille[i-3][j-3] or grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2]==grille[i+3][j-3] or grille[i][j]==grille[i][j-1]==grille[i][j-2]==grille[i][j-3] or grille[i][j]==grille[i-1][j+1]==grille[i-2][j+2]==grille[i-3][j+3]):
                #print('Fini')
                fini = True  
           if(i>9 and j<10 and j>3):
            if (grille[i][j]==grille[i][j+1]==grille[i][j+2]==grille[i][j+3] or grille[i][j]==grille[i][j-1]==grille[i][j-2]==grille[i][j-3]):
                #print('Fini')
                fini = True  
           if(j>9 and i<4):
            if (grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j]):
                #print('Fini')
                fini = True  
           if(j>9 and i>3 and i<10):
            if (grille[i][j]==grille[i+1][j]==grille[i+2][j]==grille[i+3][j] or grille[i][j]==grille[i-1][j-1]==grille[i-2][j-2]==grille[i-3][j-3] or grille[i][j]==grille[i+1][j-1]==grille[i+2][j-2]==grille[i+3][j-3]):
                #print('Fini')
                fini = True
     if(fini == True):
        if (croix == True):
            #print('Croix gagne')
            return [True,1]
        else:
            #print ('Rond gagne')
            return [True,-1]
     if(fini == False):
         #print('Ok')
         return [False,0]



def FinDeJeuCarPlateauPlein(): 
     global grille
     for e in range(12):
         for j in range(12):
                if (grille[e][j]=='. '):
                    return False
     return True
    
       

def MaxValue(s,profondeur):
    if(VerifPartie(grille)[0]==True or profondeur==0):
        return VerifPartie(grille)[1]==1
    
    V = -infinity
    for a in ActionsPossibles(s):
        V = max(V, MinValue(Resultat(a,'O '),profondeur-1))
    return  V   
    

def MinValue(s,profondeur):
    if(VerifPartie(grille)[0]==True or profondeur==0):
        return VerifPartie(grille)[1]==0
    
    V = + infinity
    for a in ActionsPossibles(s):
        V = min(V, MaxValue(Resultat(a, 'X '),profondeur-1))
    
    return V

def MinMax_Decision(s,profondeur):
    liste_action = []
    for a in ActionsProche(s):  
        mini=MinValue(Resultat(a,'O '),profondeur)
        mini2=(mini,a)
        liste_action.append(mini2)
    
    res = liste_action[0]
    for elem in liste_action:
        if res[0] < elem[0]:
            res = elem
    
    return res[1]

def Jouer(i):
   
   global grille
   coordonnees = [i for i in range(12)]
   if (i==2):
    signe = 'O '  
    iteration=0
    while(VerifPartie(grille)[0] == False): 
       
       AfficherGrille()
       bool_partie = False
       
       if (signe == 'O '):
           while (bool_partie is False):
               print("Ou souhaitez vous jouer?:")
               y = int(input("Saisir la colonne :\n"))
               x = int(input("Saisir la ligne :\n"))               
               if (x-1 in coordonnees and y-1 in coordonnees and grille[x-1][y-1] == '. '):
                   bool_partie = True
                   grille[x-1][y-1] = signe
                   signe = 'X ' 
               else:
                   print("La case est déja prise, veuillez réessayer !")
           
        
       else: 
           print("\nL'IA réfléchis à son coup ! (attention, méfies toi, elle est très smart)")
           
           
           
           alpha=-25
           beta=0
           (alpha,beta)= DebutJeu(alpha, beta) 
           grille[alpha][beta]='X '                              
           signe = 'O '
           iteration+=1
     
    AfficherGrille() 
    if (signe == 'O '):
        print("L'IA GAGNE !")
    elif(FinDeJeuCarPlateauPlein()):
        print("Pas de gagnant !")
    else:
        print("Le joueur est gagnant !")
         
   if(i==1):
    
     signe = 'X '
     iteration=0
     while(VerifPartie(grille)[0] == False): 
       if iteration!=0:
           AfficherGrille()
       bool_partie = False
       
       if (signe == 'X '):
           print("\nL'IA réfléchis... ")
          
           if iteration==0: 
               grille[7][7]='X '
           elif iteration==1:
               grille[6][6]='X '
           elif iteration==2:
               grille[5][5]='X '
               
           
           else:  #pour les coups suivants
               print(grille)
               grille = copy.deepcopy(MinMax_Decision(signe,1))
               print(grille)
           signe = 'O '
           iteration+=1
           
           
        
       else: 
           while (bool_partie is False):
               print("Ou souhaitez vous jouer? :")
               y = int(input("Saisir la colonne :\n"))
               x = int(input("Saisir la ligne :\n"))               
               if (x-1 in coordonnees and y-1 in coordonnees and grille[x-1][y-1] == '. '):
                   bool_partie = True
                   grille[x-1][y-1] = signe
                   signe = 'X '
               else:
                   print("Veuillez réessayer !")
     
   AfficherGrille()
    
   if (signe == 'O '):
        print("L'IA est la grande gagnante de cette partie !")
   elif(FinDeJeuCarPlateauPlein()):
        print("Pas de gagnant !)")
   else:
        print("Le joueur est gagnant (bravooooo) !")

    



def DebutJeu(alpha,beta):
    i=0
    n=0
    liste=[]
    for i in range(12):
        for j in range(12):
            if grille[i][j] == 'O ':
                 liste.append([i,j])   
                
    while alpha==-25 or grille[alpha][beta]!='. ':
        alpha=liste[n][0]
        b=liste[n][1]
        if i<1 and alpha<11:
            alpha+=1
        if i>1 and beta<11:
            beta+=1
        if i>2 and alpha>0:
            alpha-=1
        if i>3 and beta>0:
            beta-=1
        if i>4 and alpha<11 and beta<11: 
            beta+=1
            alpha+=1
        if i>5 and b>0 and alpha>0:
            alpha-=1
            beta-=1
        if i>6 and beta>0 and alpha>0:
            alpha+=1
            beta-=1
        if i>6 and beta>0 and alpha>2:
            alpha-=1
            beta+=1
        i+=1
        if i>8:
            n=1
            i=0               
    return (alpha, beta)               

def ActionsPossibles(s): 
    global grille  
    listePositions = []
    for i in range(12):
        for j in range(12):
            if grille[i][j] == '. ':
                listePositions.append((i,j))   
    actionsPossibles = []
    for e in listePositions:
        actionsPossibles.append(PlacerCoupIA(e[0], e[1]))
    return actionsPossibles

def Fautour(i,j): 
    global grille
    try:
        return grille[i+1][j+1]!='. '
    except:
        pass
    try:
        return grille[i-1][j-1]!='. '
    except:
        pass        
    try:
        return grille[i-1][j+1]!='. '
    except: 
        pass
    try:
        return grille[i+1][j-1]!='. '
    except: 
        pass
    try:
        return grille[i-1][j]!='. '
    except: 
        pass
    try:
        return grille[i+1][j]!='. '
    except: 
        pass
    try:
        return grille[i][j+1]!='. '
    except: 
        pass
    try:
        return grille[i][j-1]!='. '
    except: 
        pass


    
def TestCaseVide(i,j):
    rep=False
    if grille[i][j]=='. ':
        rep=True
    return rep
    

def ActionsProche(s):
    
    listePositions = []
    for i in range(12):
        for j in range(12):
            if (TestCaseVide(i,j)==True):
                if (Fautour(i,j)==True):
                    listePositions.append((i,j))
    
    actions = []
    for e in listePositions:
        actions.append(PlacerCoupIA(e[0], e[1]))
        
    return actions
    



def Resultat(a,s): 
    global grille
    copiegrille=[['. ' for i in range(12)] for j in range(12)]
    for i in range(12):
        for j in range(12):
            copiegrille[i][j]=grille[i][j]
    
    copiegrille = a
    
    grille=[['. ' for i in range(12)] for j in range(12)]
    for i in range(12):
        for j in range(12):
            grille[i][j]=copiegrille[i][j]
    return s
    
        
        
def PlacerCoupIA(ligne, colonne): 
    global grille
    copiegrille=[['. ' for i in range(12)] for j in range(12)]
    for i in range(12):
        for j in range(12):
            copiegrille[i][j]=grille[i][j]
    
    copiegrille[ligne][colonne] = 'X '    
    return copiegrille

def Jeu():
    
    i=int(input("Qui commence la partie? (Tapez 1 pour l'IA ou tapez 2 pour le joueur)\n")) 
    
    Jouer(i)

Jeu() 