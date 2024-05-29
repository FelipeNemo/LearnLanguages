"""Classes para manipulação e gerenciamento de Users dentro de LearnLanguages"""
# Imports
from .erros import *
from . import constantes as const


# 2) Todos os atributos das classes precisam ter seu acesso gerenciado por setters e getters.

# 3) Caso existam valores inválidos, o programa deve lançar exceções, as quais devem ser
#tratadas para que o programa não pare de funcionar na aplicação (app.py).

# 4) Implementar a classe Idioma, a qual armazena o nome do idioma (50 caracteres no máximo) e
#nível de proficiência (A1, A2, B1, B2, C1, C2, ou Nativo).

class Idioma:
    def __init__(self, idioma, nivel):
        self.idioma = idioma
        self.nivel = nivel

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, n):
        if isinstance(n, str) and len(n) <= const.MAX_IDIOMA:
            self.__idioma = n
        else:
            raise ErroIdiomaInvalido(f"O nome do idioma não pode exceder {const.MAX_IDIOMA} caracteres.")

    @idioma.deleter
    def idioma(self):
        del self.__idioma

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, i):
        if isinstance(i, str) and i in const.NIVEL_PROFICIENCIA:
            self.__nivel = i
        else:
             raise ErroNivelInvalido(f"Nível de proficiência inválido. Escolha entre {const.NIVEL_PROFICIENCIA}.")

    @nivel.deleter
    def nivel(self):
        del self.__nivel

    # Print objeto Idioma(nome, nivel)
    def __str__(self):
        return f"{self.idioma} e tem nível {self.nivel}!"


# 5) Implementar a classe Horario para representar os horários em que o professor está disponível
#para lecionar as aulas de idiomas. O pacote datetime pode ser utilizado para representar a
#data. Métodos são opcionais.
class Horario():
      def __init__(self, hora_inicio, hora_fim, dia_semana):
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.dia_semana = dia_semana

      @property    
      def hora_inicio (self):
            return self.__hora_inicio 
      @hora_inicio.setter
      def hora_inicio(self, hora_inicio):
                        self.__hora_inicio = hora_inicio

      @property    
      def hora_fim (self):
            return self.__hora_fim 
      @hora_fim.setter
      def hora_fim(self, hora_fim):
            self.__hora_fim = hora_fim

      @property    
      def dia_semana(self):
            return self.__dia_semana
      @dia_semana.setter
      def dia_semana(self, dia_semana):
            self.__dia_semana = dia_semana

      def __str__(self):
            return f"Horário: {self.hora_inicio} - {self.hora_fim}, {self.dia_semana}"




# 6) Implementar a classe TipoDeAula para identificar os diferentes tipos de aulas oferecidos pelos
#professores. Cada tipo de aula possui informações tais como idioma, preço, e identificador.

class TipoDeAula(Idioma):
      def __init__(self, idioma, nivel, preco, identificador):
        super().__init__(idioma, nivel)  # Chama o construtor da classe pai para definir idioma e nivel
        self.preco = preco
        self.identificador = identificador

      @property    
      def preco (self):
            return self.__preco 
      @preco.setter
      def preco(self, preco):
            self.__preco = preco

      @property    
      def identificador (self):
            return self.__identificador
      @identificador.setter
      def identificador(self, identificador):
            self.__identificador = identificador

      def __str__(self):
           return f"Tipo de aula: {self.idioma}, preço {self.preco}, identificador {self.identificador}"

# 7) Implementar a classe Aula. Uma aula reúne informações como professor, estudante, horário, e
#tipo da aula.
# Herda de class TipoDeAula(idioma e obj TipoDeAula)
# Herda de class Horario horario
      
class Aula(Horario, TipoDeAula):
      def __init__(self, professor, estudante, idioma, nivel, preco, identificador, hora_inicio, hora_fim, dia_semana):
           TipoDeAula.__init__(self, idioma, nivel, preco, identificador)
           Horario.__init__(self, hora_inicio, hora_fim, dia_semana)
           self.professor = professor
           self.estudante = estudante

      @property
      def professor (self):
            return self.__professor
      @professor.setter
      def professor(self, professor):
            self.__professor = professor

      @property
      def estudante(self):
            return self.__estudante
      @estudante.setter
      def estudante(self, estudante):
            self.__estudante = estudante

      def __str__(self):
           return (f"Aula de {self.idioma} com {self.professor}, estudante: {self.estudante}, "
                   f"preço: {self.preco}, identificador: {self.identificador}, "
                   f"horário: {self.hora_inicio} - {self.hora_fim}, {self.dia_semana}")
           
            


# 8) Implementar a classe Carteira, a qual serve para permitir ao estudante pagar o preço das
#aulas aos professores. A classe Carteira deve permitir depositar, sacar, e fazer transferências
#de dinheiro entre carteiras.
      
class Carteira(Aula):
     def __init__(self,depositar,sacar,transferir):
          super().__init__(Aula)
          self.depositar = depositar
          self.sacar = sacar
          self.sacar = transferir

          #def transferir(self):
               



     


# 9) Implementar a classe abstrata Usuario:
# inicio do código em funções.py
       
# 10) Implemente a classe Estudante como uma subclasse de Usuario:
class Estudante:
      pass
# 11) Implementar a classe Professor como uma subclasse de Usuario:
class Professor:
      pass
# OBS: Classe Sistema faz as operações de marcação de aulas, saidas e entradas na carteira do aluno e do professor ...
class Sistema:
      pass

# 12) Fornecer um método para imprimir o relatório do sistema, o qual deve informar a quantidade
#de estudantes e professores cadastrados, bem como o saldo da carteira do sistema. O método
#também deve imprimir o relatório de cada usuário cadastrado no sistema.


