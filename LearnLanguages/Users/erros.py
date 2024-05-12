"""Modulo que implementa todas as classes de erro!"""

class ErroIdiomaInvalido(Exception):
    """Não é permitido idioma maior que 50 caracteres"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroIdiomaInvalido (" + self.__msg +")"
    

class ErroNivelInvalido(Exception):
    """Não é permitido níveis que sejam diferente do conteúdo de NIVEL_PROFICIENCIA"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroNivelInvalido (" + self.__msg +")"   

