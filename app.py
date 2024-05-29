import LearnLanguages.Users as l
import datetime

print("CADASTRO ESCOLA DE INGLES\n")



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

except l.ErroIdiomaInvalido as e:
    print(e)   

except l.ErroNivelInvalido as e:
     print(e)


