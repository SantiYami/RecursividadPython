def multiplicarSumando(a,b):
    if b>0:
        return a+multiplicarSumando(a,b-1)
    return 0
def main():
    print("Ingrese Primer Numero: ")
    a=int(input())
    print("Ingrese Segundo Numero")
    b=int(input())
    print a,"*",b,"=",multiplicarSumando(a,b)
if __name__ =='__main__':
    main()
    
