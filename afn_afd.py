#Transformare AFN->AFD
from collections import deque
f = open("turn_2.txt","r")
n =  int(f.readline()) #nr de stari in automat
init = f.readline()[0] # starea initiala
nrf = int(f.readline()) #nr de stari finale
sir = f.readline()
starif = [ x for x in sir.split()] # vector de stari finale
sir = f.readline()    # vector pt alfb
v_tranz = [  x for x in sir.split()]
nrtranz = int(f.readline()) # nr de tranzitii
lista = []
for i in range(nrtranz): # construim o matrice pt tranzitii
     sir2 = f.readline().split()
     a = sir2[0]     #lista de tranzitii de forma stare->tranz->stari in care poate ajunge cu tranz resp
     b = sir2[1]
     lista.append( ([a],b,sir2[2:]) )

final = [] #lista pt a reprezenta tranz in AFD ul obtinut
q = deque([])
q.append([init])
for x in lista:
    if x[0][0] == init:
         q.append(x[2]) #coada de prioritati in care punem starea initiala

vect_stari=[]#retinem starile nou obtinute in "tabel" pentru a sti  care dintre ele
 # au fost deja capete de linii si nu mai trebuie sa le calculam..in q facem pop si de asta nu ne putem folosi de el pt asta
while q != deque([]):
     x = q.popleft()  # in x se afla  starea curenta pentru care trebuie sa calculam linia
     for k in v_tranz: #0 sau 1 in cazul nostru
         m = []
         for i in x:  #reunim ce gasim in "tabel" corespunzator starilor componente din starea-multime
            for j in lista:
               if j[0][0] == i and j[1] == k:
                m = m+j[2]
         n = set(m) #eliminam duplicatele
         m = list(n)
         m.sort()
         if m != []  and (x,k) not in vect_stari:#daca au existat tranzitii pt starea resp si
                                            #aceasta stare , cu tranzitia coresp k nu a mai fost adugata, o adaugam
            q.append(m)
            final.append((x,k,m))
            vect_stari.append((x,k))
for x in final:
    print(x)
print("STARI FINALE")

#construim alt vect pt stari finale sa fie distincte
distinct = []
for k in  starif:
    for x in final:
        if k in x[2] and x[2] not in distinct:
            distinct.append(x[2])
        if  k==x[0][0] and x[0] not in distinct:
            distinct.append([k])
print(distinct)