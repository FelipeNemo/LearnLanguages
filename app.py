import LearnLanguages.Users as u
import datetime

T1 = u.TipoDeAula("Ingles",72,521637)
print(T1)


H1 = u.Horario(datetime.time(9, 0), datetime.time(12, 0), "Segunda-feira")
print(H1)


try:
    idioma = input("Digite o idioma:")
    nivel = input("Digite seu nível de proficiencia:")

    P1 = u.Idioma(idioma, nivel)
    print(P1)
    
    
except u.ErroIdiomaInvalido as e:
    print(f"Erro: {e}")
except u.ErroNivelInvalido as e:
    print(f"Erro: {e}")
except ValueError as e: # especificar o tipo de erro em erros.py para ele encerrar o programa ao receber o primeiro input
    print(f"Erro de entrada: {e}")