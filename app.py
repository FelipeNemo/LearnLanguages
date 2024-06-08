import LearnLanguages.Users as l
import datetime
#import modulo os

try:

    # Exemplo de uso:
    carteira_sistema = l.Carteira(0)

    carteira_estudante1 = l.Carteira(200)
    carteira_estudante2 = l.Carteira(200)

    carteira_professor1 = l.Carteira(0)
    carteira_professor2 = l.Carteira(0)

    estudante1 = l.Estudante("Felipe", "felipe@gmail.com", "Brasil", "Brasil", carteira_estudante1, [l.Idioma("Inglês", "Nativo")], [])
    estudante2 = l.Estudante("Eduardo", "eduardo@gmail.com", "Brasil", "Brasil", carteira_estudante2, [l.Idioma("Inglês", "Nativo")], [])
    professor1 = l.Professor("Dalvan", "Dalvan@exgmail.com", "Brasil", "Brasil", carteira_professor1, [l.Idioma("Português", "B2")], [])
    professor2 = l.Professor("Gabriel", "Gabriel@gmail.com", "Brasil", "Brasil", carteira_professor2, [l.Idioma("Português", "B2")], [])

    #Aula estudante
    estudante1 .adicionar_idioma(l.Idioma("Inglês", "A1"))
    estudante2.adicionar_idioma(l.Idioma("Espanhol", "C2"))

    # Agendar aula para o estudante
    professor1.adicionar_idioma(l.Idioma("Inglês", "A1"))
    professor2.adicionar_idioma(l.Idioma("Espanhol", "C2"))
    
    # Adicionar professores ao histórico do estudante
    aula1 = l.Aula(
        professor=professor1,
        estudante=estudante1,
        idioma="Francês",
        nivel="B2",
        preco=100,
        identificador="AULA001",
        hora_inicio=datetime.time(10, 0),
        hora_fim=datetime.time(11, 0),
        dia_semana="Segunda"
    )
    

    # Transferir saldo da carteira do estudante para a carteira do professor
    #carteira_estudante1.depositar(100)
    carteira_estudante1.transferir(100, carteira_professor1)
    


    # Imprimir relatório do estudante
    estudante1.agendar_aula(aula1)
    estudante1.confirmar_aula_concluida(aula1,carteira_sistema )



    # Criando alguns usuários
    

    # Listas de estudantes e professores
    estudantes = [estudante1,estudante2 ]
    professores = [professor1,professor2]

    # Imprimindo o relatório do sistema
    l.imprimirRelatorioSistema(estudantes, professores, carteira_sistema)
except l.ErroNomeInvalido as e:
    print(e)

except l.ErroEmailInvalido as e:
    print(e)

except l.ErroPaisDeOrigemInvalido as e:
    print(e)

except l.ErroPaisAtualInvalido as e:
    print(e)

except l.ErroAulaInvalida as e:
    print(e)



# Class Carteira
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
