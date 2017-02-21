# -*- coding: utf-8 -*-
#El algoritmo de Euclides para encontrar MCD(A,B) es como sigue:
##Si A = 0 entonces MCD(A,B)=B, ya que el MCD(0,B)=B, y podemos detenernos.
##Si B = 0 entonces MCD(A,B)=A, ya que el MCD(A,0)=A, y podemos detenernos.
##Escribe A en la forma cociente y residuo (A = B ⋅Q + R).
##Encuentra MCD(B,R) al usar el algoritmo de Euclides, ya que MCD(A,B) = MCD(B,R).
def m_c_d(num1,num2):
    if(num1==0):
        return num2
    else:
        if(num2==0):
            return num1
        else:
            return m_c_d(num2, num1%num2)

print 'Ingrese los numeros que les desea hallar su M.C.D.'
print m_c_d(int(input()),int(input()))
