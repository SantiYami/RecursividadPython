def SepararLista(lista):
    if len(lista)==1:
        return Minimo(lista[0])
    else:
        return Minimo(lista[0])+SepararLista(lista[1:])

def Minimo(lista):
    if len(lista)==1:
        return lista[:1]
    elif lista[0]<lista[-1]:
        return Minimo(lista[:-1])
    else:
        return Minimo(lista[1:])

def main():
    parentlist = []
    listatemp=[]
    print "Ingrese cantidad de elementos de la lista de listas: "
    k = int(raw_input())

    for i in range(k):
        print "Ingrese cantidad de elementos de una lista: "
        n = int(raw_input())
        print "Ingrese los elementos: "
        for j in range(n):
            str1 = raw_input()
            listatemp.append(str1.split())
        parentlist.append(listatemp)
        listatemp=[]

    print SepararLista(parentlist)

if __name__ == "__main__":
    main()
