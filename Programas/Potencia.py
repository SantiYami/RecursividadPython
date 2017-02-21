def potencia(n,m):
    if m>0:
        return n*potencia(n,m-1)
    return 1
def main():
    print("Ingrese Base: ")
    base=int(input())
    print("Ingrese Exponente")
    exponente=int(input())
    print base,"^",exponente,"=",potencia(base,exponente)
if __name__ =='__main__':
    main()
    
