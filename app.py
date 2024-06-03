import LearnLanguages.Users as l
import datetime

#print("CADASTRO ESCOLA DE INGLES\n")

# A manipula;'ao do arquivo de entrada ser[a feita pelo app.py usando o modulo os

try:
    # input classe Idioma
    #idioma = input("Digite o idioma:")
    #nivel = input("Digite seu nível de proficiencia:")

    # Criar uma instância da classe Idioma com os valores fornecidos pelo usuário.
    #P1 = l.Idioma(idioma, nivel)
    #P1 = l.Idioma("Inglês", "C1")
    #print(P1)

    # Criar uma instância da classe Horario.
    #H1 = l.Horario(datetime.time(9, 0), datetime.time(12, 0), "Segunda-feira")
    #print(H1)

    # Criar uma instância da classe TipoDeAula.
    #tipo_aula = l.TipoDeAula("Espanhol", "C1", 100, "AULA159")
    #print(tipo_aula)  # Saída: Tipo de aula: Espanhol, preço 100, identificador AULA159

    # Criar uma instância da classe Aula.
    #A1 = l.Aula("Prof Bruce Lee", "Felipe", "Inglês", "B2", 72.15, "521637-5", datetime.time(9, 0), datetime.time(12, 0), "Segunda-feira")
    #print(A1)

    # Criar uma instância da classe Carteira
    #CE = l.Carteira(200)
    #CP = l.Carteira(200)

    #print("Saldo inicial Estudante : ",  CE.saldo)
    #print("Saldo inicial  Professor : ",  CP.saldo)


    #CE.depositar(200)
    #print("Saldo depois do deposito na carteira estudante : ",  CE.saldo)
    

    #CE.sacar(50) # fica 350
    #print("Saldo depois do saque na carteira estudante : ",  CE.saldo)
    
    #CE.transferir(30, CP)
    #print("Saldo depois da tranferencia da carteira estudante: ",  CE.saldo)
    #print("Saldo depois de estudante tranferir para carteira professor : ",  CP.saldo)


    

    # Exemplo de uso
    C1 = l.Carteira(300)
    C2 = l.Carteira(300)
    
    #Objetos Estudante e professor
    E = l.Estudante(nome="Felipe", email="felipedata20@gmail.com", paisOrigem="Brasil", paisAtual="EUA", carteira=C1)
    P = l.Professor(nome="Bruce lee", email="pucrs20@gmail.com", paisOrigem="Brasil", paisAtual="Alemanhã", carteira=C2)

    #Aula estudante
    E.adicionar_idioma(l.Idioma("Inglês", "A1"))
    E.adicionar_idioma(l.Idioma("Espanhol", "C2"))

    # Agendar aula para o estudante
    P.adicionar_idioma(l.Idioma("Inglês", "A1"))
    P.adicionar_idioma(l.Idioma("Espanhol", "C2"))
    
    # Adicionar professores ao histórico do estudante
    aula1 = l.Aula(
        professor="Professor A",
        estudante="Felipe",
        idioma="Francês",
        nivel="B2",
        preco=100,
        identificador="AULA001",
        hora_inicio=datetime.time(10, 0),
        hora_fim=datetime.time(11, 0),
        dia_semana="Segunda"
    )
    
    # Imprimir relatório do estudante
    E.agendar_aula(aula1)
    E.confirmar_aula_concluida(aula1)
    
    E.historico_professores.append("Professor A")
    E.historico_professores.append("Professor B")
    E.historico_professores.append("Professor A")

    # Imprimir relatórios
    print("RELATORIO ESTUDANTE")
    E.imprimirRelatorio()
    print("\n")
    print("RELATORIO PROFESSOR")
    P.imprimirRelatorio()

#Class Usuario    
except l.ErroNomeInvalido as e:
    print(e) 

except l.ErroEmailInvalido as e:
    print(e) 

except l.ErroPaisDeOrigemInvalido as e:
    print(e) 

except l.ErroPaisAtualInvalido as e:
    print(e) 

#Class Idioma
except l.ErroIdiomaInvalido as e:
    print(e)   

except l.ErroNivelInvalido as e:
     print(e)

#Class Carteira 
except l.ErroSaldoInvalido as e:
     print(e)

except l.ErroDepositoInvalido as e:
     print(e)

except l.ErroSaqueIndisponivel as e:
     print(e)

except l.ErroContaInvalida as e:
     print(e)

except l.ErroSaldoInsuficiente as e:
     print(e)


