def dividirRestando(a,b):
    if a-b>=0:
        return 1+dividirRestando(a-b,b)
    return 0
def main():
    print("Ingrese Primer Numero: ")
    a=int(input())
    print("Ingrese Segundo Numero")
    b=int(input())
    print a,"/",b,"=",dividirRestando(a,b)
if __name__ =='__main__':
    main()
    
