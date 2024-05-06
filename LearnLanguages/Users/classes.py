#Implementar a classe abstrata Usuario:
class Usuario:
        
        def __init__(self, nome, email):
             self.__nome = nome
             self.__email = email
        
        
        @property
        def nome(self):
              return self.__nome
        
        @property
        def email(self):
              return self.__email

        @nome.setter
        def nome(self,nome):
              self.__nome = nome

        @nome.setter
        def email(self,email):
              self.__email = email
       

        #Implementar getters
#Caso existam valores inválidos, o programa deve lançar exceções, as quais devem ser
#tratadas para que o programa não pare de funcionar na aplicação (app.py).

#Subclasses
class Idioma:
      pass
#Implementar a classe Idioma, a qual armazena o nome do idioma (50 caracteres no máximo) e
#nível de proficiência (A1, A2, B1, B2, C1, C2, ou Nativo).
              
class Horario:
      pass
#Implementar a classe Horario para representar os horários em que o professor está disponível
#para lecionar as aulas de idiomas. O pacote datetime pode ser utilizado para representar a
#data. Métodos são opcionais.

class TipoDeAula:
      pass
#Implementar a classe TipoDeAula para identificar os diferentes tipos de aulas oferecidos pelos
#professores. Cada tipo de aula possui informações tais como idioma, preço, e identificador.

class Aula:
      pass
#Implementar a classe Aula. Uma aula reúne informações como professor, estudante, horário, e
#tipo da aula.

class Carteira:
      pass
#Implementar a classe Carteira, a qual serve para permitir ao estudante pagar o preço das
#aulas aos professores. A classe Carteira deve permitir depositar, sacar, e fazer transferências
#de dinheiro entre carteiras.

class Estudante:
      pass
#10)Implemente a classe Estudante como uma subclasse de Usuario:
