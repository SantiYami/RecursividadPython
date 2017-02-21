def DecimalABinario(n):
    if n == 0:
        return '0'
    else:
        return DecimalABinario(n//2) + str(n%2)
def main():
    print(DecimalABinario(int(input("Ingrese un numero decimal: "))))
if __name__ =='__main__':
    main()

    
