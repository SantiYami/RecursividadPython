from random import randint
from random import shuffle

def dimensionpalos(lista):
        if lista==[]:
                return 0
        else:
                return 1 + dimensionpalos(lista[1:])
    
def palos (lista):
        if dimensionpalos(lista)<48:
                if lista==[]:
                        lista.append('A')
                        return palos(lista)
                elif lista[-1]=='A':
                        lista.append('2')
                        return palos(lista)
                elif lista[-1]=='9':
                        lista.append('J')
                        return palos(lista)
                elif lista[-1]=='J':
                        lista.append('Q')
                        return palos(lista)
                elif lista[-1]=='Q':
                        lista.append('K')
                        return palos(lista)
                elif lista[-1]=='K':
                        lista.append('A')
                        return palos(lista)
                elif int(lista[-1])<9:
                        lista.append(str(int(lista[-1])+1))
                        return palos(lista)
        else:
                return lista
def valor (val):
    if val=='A':
        return 1
    elif val=='2':
        return 2
    elif val=='3':
        return 3
    elif val=='4':
        return 4
    elif val=='5':
        return 5
    elif val=='6':
        return 6
    elif val=='7':
        return 7
    elif val=='8':
        return 8
    elif val=='9':
        return 9
    elif val=='J'or val=='K'or val=='Q':
        return 10
    
def cartas(num,lista,s):
        if num==21:
                return num
        if num==-1:
                return -1 
        elif num<21:
                print ("mas cartas ?")
                if raw_input()=="n":
                        print ("CPU jugando")
                        if cartascpu(0,num,lista)==0:
                                return -1
                        else:
                                return num
                else:
                    shuffle(lista)
                    if lista[0]=='A':
                        if num+11>21:
                            print ("nueva carta : ",lista[0]," suma de cartas: ",num+valor(lista[0]))
                            return cartas(num+valor(lista[0]),lista,s)
                        else:
                            print ("nueva carta : ",lista[0]," suma de cartas: ",num+11)
                            return cartas(num+11,lista,s+1)
                    print ("nueva carta : ",lista[0]," suma de cartas: ",num+valor(lista[0]))
                    return cartas(num+valor(lista[0]),lista,s)
        elif num>21&s==0:
                return -1
        elif num>21&s>0:
                 print ("A reducida : Nueva suma de cartas = ",num-10)
                 return cartas(num-10,lista,s-1)
            
    
def cartascpu(num,user,lista):
        if (num<21)&(num>user):
                return 0
        if num==21:
                return 0
        if num > 21:
                return 1
        if num<21:
                shuffle(lista)
                print ("nueva carta : ",lista[0]," suma de cartas: ",num+valor(lista[0]))
                return cartascpu(num+valor(lista[0]),user,lista)


#inicio del programa

    
print ("juego de cartas 21")
print ("\nuse 'y' para mas cartas y 'n' para no recibir mas cartas")

if cartas(0,palos (lista=[]),0)==(-1):
    print("\nHa perdido!!!!")
else:
    print("\nHa ganado!!!!")
