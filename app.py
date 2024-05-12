import LearnLanguages.Users as u

try:
    idioma = input("Digite o idioma:")
    nivel = input("Digite seu nível de proficiencia:")
    P1 = u.Idioma(idioma, nivel)
    print(P1)
    del P1
except u.ErroIdiomaInvalido as e:
    print(f"Erro: {e}")
except u.ErroNivelInvalido as e:
    print(f"Erro: {e}")
except ValueError as e:
    print(f"Erro de entrada: {e}")