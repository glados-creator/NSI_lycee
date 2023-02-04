def main():

    default_lenth = 100

    def get_random_list_of_numbers(lenth=default_lenth):
        from random import randint
        return [ randint(1,100) for j in range(lenth) ]
    
    def exemeple_1(lenth = default_lenth):
        from random import randint

        # création d'une liste d'entiers au hasard
        L = [ randint(1,100) for j in range(lenth) ]
        print('Contenu de la liste L :\n', L)
        # création d'une nouvelle liste
        # même contenu que L
        # mais triée :
        M=sorted(L)
        print('Contenu de la liste M=sorted(L) :\n ',M)
        # L est inchangée :
        print('Contenu de la liste L :\n', L)
    
    def exemple_2():
        L = [ 'choucroute','barbapapa', 'tsointsoin', 'abracadabra' ]
        print('Contenu de la liste L :\n', L)
        L.sort()
        print('Contenu de la liste L :\n', L)

    def tri_selection(L=get_random_list_of_numbers()):
        n = len(L)
        i = 0 # tete rouge
        while i < n:
            j = i
            while j < n:
                # tete noire but reperer le min
                # 3 cas possible L[j] > L[i] / L[j] = L[i] / L[j] < L[i] 
                # print(i,j,"L[j]",L[j],"L[i]",L[i],L,bool(L[j] < L[i]))
                if L[j] < L[i]:
                    L[i] , L[j] = L[j] , L[i] # swap
                j += 1
            
            i += 1
        print(L)
        print("O(n) = n²")
        
    def tri_insertion(L=get_random_list_of_numbers()):
        L = [ 5, 12, 3, 7, 4 ]
        n = len(L)
        for j in range(1,n):
            key = L[j]
            i = j - 1
            while i >= 0 and L[i] > key:
                # print("j",j,"key",key,"i,",i,"L[i]",L[i])
                L[i+1] = L[i]
                i -= 1
            L[i+1] = key
        print(L)
        print("O(n) = n²")
    
    def pylabexe():
        from random import randint
        from time import time
        from pylab import plot, show, polyfit

        def creationListe(n=default_lenth) :
            """ crée une liste de n éléments,
            éléments au hasard entre 1 et 2n."""
            return [randint(1,2*n) for j in range(n)]
        def triselection(L) :
            """ tri la liste suivant le tri par sélection
            et retourne le temps d'exécution."""
            start=time()
            #
            pass
            #
            return time()-start
        # liste de tailles de listes :
        TailleListe = range(50, 8000, 200)
        # liste des temps d'exécution :
        TempsTri = [triselection(creationListe(n)) for n in TailleListe]
        # approximation par polynôme second degré :
        p=polyfit(TailleListe, TempsTri, 2)
        Yp= [p[0]*x**2+p[1]*x+p[2] for x in TailleListe]
        # courbes (taille de la liste, Temps d'exécution)
        # et (taille de la liste, polynôme second degré approchant) :
        plot(TailleListe, TempsTri,'r--',TailleListe, Yp, 'b*')
        # on lance une visualisation de la courbe :
        show()

        
    
    # print(dir())

    pylabexe()

    # boilerplate 

    #import profile
    # profile.run(main(input("prog ID : ")))
    # if (0):
    #     for x in range(1,10):
    #         print("profile : ",x,"\n")
    #         profile.run(main(x))


    

if __name__ == "__main__":
    main()
    