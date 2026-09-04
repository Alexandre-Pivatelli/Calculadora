<<<<<<< HEAD
def soma (num1,num2):
    return num1+num2

num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))

print(soma(num1,num2))
=======
def somaf(num1,num2):
    return num1+num2

def main():
    assert somaf(2, 3) == 5, "Erro: 2 + 3 deveria ser 5"
    assert somaf(2.5, 3.7) == 6.2, "Erro: 2.5 + 3.7 deveria ser 6.2"
    assert somaf(-1.5, 4.5) == 3.0, "Erro: -1.5 + 4.5 deveria ser 3.0"
    assert somaf(0, 5) == 5, "Erro: 0 + 5 deveria ser 5"
    assert somaf(5, 0) == 5, "Erro: 5 + 0 deveria ser 5"
    assert somaf(1.1, 1.1) == 2.2, "Erro: 1.1 + 1.1 deveria ser 2.2"
    print("Todos os testes passaram com sucesso!")
    return

if __name__ == "__main__":
    main()
    