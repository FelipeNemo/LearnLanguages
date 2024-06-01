"""Classes para manipulação e gerenciamento de Users dentro de LearnLanguages"""

# Imports.
from .erros import *
from . import constantes as const

# 9) Implementar a classe abstrata Usuario: -----------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Usuario(ABC):
    
# a) Atributos:
    
    def __init__(self, nome, email, paisOrigem, paisAtual, idiomas, horarios, carteira):
        self.__nome = nome
        self.__email = email
        self.__paisOrigem = paisOrigem
        self.__paisAtual = paisAtual
        self.__idiomas = idiomas
        self.__horarios = horarios
        self.__carteira = carteira


    @property   # Máximo 50 caracteres.
    def nome(self):
        return self.__nome
    
    @nome.setter  
    def nome(self, nome):
        self.__nome = nome


    @property  # Máximo 50 caracteres.
    def email(self):
        return self.__email
    
    @email.setter  
    def email(self, email):
        self.__email = email


    @property  # Máximo 10 caracteres.
    def paisOrigem(self):
        return self.__paisOrigem
    
    @paisOrigem.setter 
    def paisOrigem(self, paisOrigem):
        self.paisOrigem = paisOrigem


    @property  # Máximo 10 caracteres.
    def paisAtual(self):
        return self.__paisAtual
    
    @paisAtual.setter 
    def paisAtual(self, paisAtual):
        self.paisAtual = paisAtual


    @property   # Uma Lista [] de objetos idioma que o usuário sabe falar(Já implementado na classe Idioma).
    def idiomas(self):
        return self.__idiomas

    @idiomas.setter 
    def idiomas(self, idiomas):
        self.__idiomas = idiomas

    
    @property  # Uma Lista [] de objetos horario que o usuário sabe falar(Já implementado na classe Horario).
    def horarios(self):
         return self.__horarios
    
    @horarios.setter 
    def carteira(self, horarios):
        self.__horarios = horarios


    @property  # Uma Lista [] de objetos carteira que o usuário sabe falar(Já implementado na classe Carteira).
    def carteira(self):
         return self.__carteira

    @carteira.setter 
    def carteira(self, carteira):
        self.__carteira = carteira

# b) Métodos: 
        
# i) imprimirRelatorio: Método abstrato que deve ser implementado pelas classes que herdam a classe Usuario.
# imprimir um relatório completo sobre as atividades do usuário.
        
    @abstractmethod
    def imprimir_relatorio(self):
         pass
       
# 10) Implemente a classe Estudante como uma subclasse de Usuario:

class Estudante(Usuario):
     
# a) Atributos:
     
     def __init__(self, idiomas, professores):
          self.idiomas = idiomas
          self.professores = professores

# b) Métodos:

#(1) Listar Idiomas que o estudante sabe falar;
#(2) Listar Idiomas que o estudante deseja aprender;
#(3) Listar horários do estudante;
#(4) Listar professores do estudante;
#(5) Listar aulas concluídas pelo estudante;
#(6) Exibir dados do professor favorito do estudante (com qual professor o estudante teve mais aulas, e quantas foram);
#(7) Exibir idioma favorito do estudante (com qual idioma o estudante tevemais aulas, e quantas foram);
#(8) Exibir saldo da carteira do estudante.
          
# i) Lista de idiomas que o estudante deseja aprender.
    
     def idiomas_aprender(self):
          pass
          
# ii) Lista de professores do estudante ja teve.
     
     def historico_professores(self):
          pass

      
# 11) Implementar a classe Professor como uma subclasse de Usuario:
class Professor(Usuario):

     
# a) Atributos:
     
     def __init__(self, idiomas, estudantes):
          self.idiomas = idiomas
          self.estudantes = estudantes

# b) Métodos:
          
# i) imprimirRelatorio do professor:
     def idiomas_professor(self):
          pass
     
#(1) Listar Idiomas que o professor sabe falar;
#(2) Listar Idiomas que o professor ensina;
#(3) Listar horários do professor;
#(4) Listar de estudantes do professor;
#(5) Listar aulas concluídas pelo professor;
#(6) Exibir saldo da carteira do professor.
          
# ii) aceitarPedidoDeAgendamento do professor:
     def Agendamento_Professor():
          pass
# (1) Se o professor aceitar um pedido de agendamento.     
# (2) Horário do professor e do estudante devem ser marcados como não disponíveis.    
# (3) Usuários não podem ter duas aulas marcadas no mesmo horário.
     
# 12) Fornecer um método para imprimir o relatório do sistema, o qual deve informar a quantidade
#de estudantes e professores cadastrados, bem como o saldo da carteira do sistema. O método
#também deve imprimir o relatório de cada usuário cadastrado no sistema.
     
# OBS: Classe Sistema faz registra operações de marcação de aulas, saidas e entradas na carteira do aluno e do professor e sistema.


class Sistema(Usuario):
      pass

# (1) Informar quantidade de estudantes e professores cadastrados
# (2) Atribuir os 10% das aulas na carteira do sistema.
# (3) Imprimir o relatório de cada usuário(professores e alunos) cadastrado no sistema




#---------------------------------------------------------------------------------------------------------------------------------------------

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
      
class Carteira():
     
      def __init__(self,saldo):
          self.__saldo = saldo

      @property
      def saldo(self):
          return self.__saldo
      
      @saldo.setter
      def saldo(self, valor):
            if valor > 0:
                 self.__saldo += valor
            else:
                 raise ValueError("Valor precisa ser maior que 0 !") # Criar em erros.py

      def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError("Esse valor excede o saldo disponível para saque !")
        
 # transferencias são feitas apenas na instancia Carteira
 # pra transferir:
 # (1)  Sacamos valor>0 da conta que transfere  
 # (2)  Depositamos valor na conta destino
        
      def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Carteira): 
            raise TypeError("A transferência deve ser feita para outra instância de Carteira.")
        if 0 < valor <= self.__saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)   
        else:
            raise ValueError("A quantia para transferência deve ser positiva e menor ou igual ao saldo disponível.") # Criar em erros.py
          
               




