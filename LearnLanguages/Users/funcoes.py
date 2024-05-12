# Movi a classe abstrata para ir implementando ela enquanto faço as outras classes
class Usuario:
        
        def __init__(self, nome, email):
             self.__nome = nome
             self.__email = email
        
        
        @property # pega o nome
        def nome(self):
              return self.__nome
        
        @property # pega o email
        def email(self):
              return self.__email

        @nome.setter # altera o nome
        def nome(self,nome):
              self.__nome = nome

        @nome.setter # altera o email
        def email(self,email):
              self.__email = email