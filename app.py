import LearnLanguages.Users as l
import datetime

print("CADASTRO ESCOLA DE INGLES\n")

# A manipula;'ao do arquivo de entrada ser[a feita pelo app.py usando o modulo os

try:
    # input classe Idioma
    #idioma = input("Digite o idioma:")
    #nivel = input("Digite seu nível de proficiencia:")

    # Criar uma instância da classe Idioma com os valores fornecidos pelo usuário.
    #P1 = l.Idioma(idioma, nivel)
    P1 = l.Idioma("Inglês", "C1")
    print(P1)

    # Criar uma instância da classe Horario.
    H1 = l.Horario(datetime.time(9, 0), datetime.time(12, 0), "Segunda-feira")
    print(H1)

    # Criar uma instância da classe TipoDeAula.
    tipo_aula = l.TipoDeAula("Espanhol", "C1", 100, "AULA159")
    print(tipo_aula)  # Saída: Tipo de aula: Espanhol, preço 100, identificador AULA159

    # Criar uma instância da classe Aula.
    A1 = l.Aula("Prof Bruce Lee", "Felipe", "Inglês", "B2", 72.15, "521637-5", datetime.time(9, 0), datetime.time(12, 0), "Segunda-feira")
    print(A1)

    # Criar uma instância da classe Carteira
    CE = l.Carteira(200)
    CP = l.Carteira(200)

    print("Saldo inicial Estudante : ",  CE.saldo)
    print("Saldo inicial  Professor : ",  CP.saldo)


    CE.depositar(200)
    print("Saldo depois do deposito na carteira estudante : ",  CE.saldo)
    

    CE.sacar(50) # fica 350
    print("Saldo depois do saque na carteira estudante : ",  CE.saldo)
    
    CE.transferir(30, CP)
    print("Saldo depois da tranferencia da carteira estudante: ",  CE.saldo)
    print("Saldo depois de estudante tranferir para carteira professor : ",  CP.saldo)
    
    

except l.ErroIdiomaInvalido as e:
    print(e)   

except l.ErroNivelInvalido as e:
     print(e)


