import time

import soma as sm
import subtrai as sb
import multiplica as mt
import divide as dv

def Calculadoraf(v1, v2, oper):
    if (oper == '+'):
        return sm.somaf(v1, v2)
    if (oper == '-'):
        return sb.subtraif(v1, v2)
    if (oper == '*' or oper == 'x'):
        return mt.multiplicaf(v1, v2)
    if (oper == '/'):
        return dv.dividef(v1, v2)

x, operacao, y = input('Insira o calculo que deseja fazer: ').split(" ")
print('O resultado é:', Calculadoraf(int(x), int(y), operacao))

