
"""Modulo que implementa todas as classes de erro!"""

#Class Usuario
class ErroNomeInvalido(Exception):
    """Não é permitido nome maior que 50 caracteres"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroNomeInvalido (" + self.__msg +")"
    
class ErroEmailInvalido(Exception):
    """Não é permitido e-mail maior que 50 caracteres"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroEmailInvalido (" + self.__msg +")"
    
class ErroPaisDeOrigemInvalido(Exception):
    """Não é permitido país de origem maior que 10 caracteres"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroPaisDeOrigemInvalido (" + self.__msg +")"
    
class ErroPaisAtualInvalido(Exception):
    """Não é permitido país atual maior que 10 caracteres"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroPaisAtualInvalido (" + self.__msg +")"
    
class ErroAulaInvalida(Exception):
    """Aula não encontrada nos horários do estudante"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroAulaInvalida (" + self.__msg +")"
    
#Class Idioma
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
       
#Class Carteira  
    
class ErroSaldoInvalido(Exception):
    """Nenhuma carteira pode ter debitos, ou seja, saldo negativo"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroSaldoInvalido (" + self.__msg +")"  
    
class ErroDepositoInvalido(Exception):
    """Não é permitido depositar um valor negativo ou igual a zero"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroDepositoInvalido (" + self.__msg +")"   
    
 
class ErroSaqueIndisponivel(Exception):
    """Só é possivel sacar um valor menor que o saldo na carteira"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroValorIndisponivel (" + self.__msg +")"   
    
class ErroContaInvalida(Exception):
    """Não é permitido tranferir para carteiras não existentes"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroContaInvalida (" + self.__msg +")" 
     
    
class ErroSaldoInsuficiente(Exception):
    """Não é permitido transferir valores que sejam menores que o saldo"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroSaldoInsuficiente (" + self.__msg +")"   

