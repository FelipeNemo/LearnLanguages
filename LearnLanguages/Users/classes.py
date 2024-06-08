"""Classes para manipulação e gerenciamento de Users dentro de LearnLanguages"""

# Imports.
from .erros import *
from . import constantes as const

# 9) Implementar a classe abstrata Usuario: -----------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod # Classe de base abstrata.

class Usuario(metaclass=ABCMeta):
    
# a) Atributos:
    
# Não precisamos verificar se os atributos de usuários são instâncias de usuário pois classes de base abstrata não criam objetos.
    
    def __init__(self, nome, email, paisOrigem, paisAtual, carteira, idiomas =[], horarios= []):
        self.nome = nome
        self.email = email
        self.paisOrigem = paisOrigem
        self.paisAtual = paisAtual
        self.idiomas = idiomas
        self.horarios = horarios
        self.carteira = carteira
        
    @property   # Máximo 50 caracteres.
    def nome(self):
        return self._nome
    
    @nome.setter  
    def nome(self, nome):
        if len(nome) > const.MAX_NOME:
            raise ErroNomeInvalido(f"O nome deve ter no máximo {const.MAX_NOME} caracteres")
        else:
             self._nome = nome

    @property  # Máximo 50 caracteres.
    def email(self):
        return self._email
    
    @email.setter  
    def email(self, email):
        if len(email) > const.MAX_EMAIL:
             raise ErroEmailInvalido(f"O e-mail deve ter no máximo {const.MAX_EMAIL} caracteres")
        else:
             self._email = email


    @property  # Máximo 10 caracteres.
    def paisOrigem(self):
        return self._paisOrigem
    
    @paisOrigem.setter 
    def paisOrigem(self, paisOrigem):
        if len(paisOrigem) > const.MAX_PAISORIGEM:
             raise ErroPaisDeOrigemInvalido(f"O país de origem deve ter no máximo {const.MAX_PAISORIGEM} caracteres")
        else:
             self._paisOrigem = paisOrigem


    @property  # Máximo 10 caracteres.
    def paisAtual(self):
        return self._paisAtual
    
    @paisAtual.setter 
    def paisAtual(self, paisAtual):
        if len(paisAtual) > const.MAX_PAISATUAL:
             raise ErroPaisAtualInvalido(f"O país de atual deve ter no máximo {const.MAX_PAISATUAL} caracteres")
        else:
            self._paisAtual = paisAtual

    @property
    def idiomas(self):
        return self._idiomas.copy()

    @idiomas.setter
    def idiomas(self, i_list):
        if all(isinstance(i, Idioma) for i in i_list):
            self._idiomas = i_list
        else:
            raise ErroIdiomaInvalido(f"O nome do idioma não pode exceder {const.MAX_IDIOMA} caracteres.")

    def adicionar_idioma(self, idioma):
        if isinstance(idioma, Idioma):
            self._idiomas.append(idioma)
        else:
            raise ErroIdiomaInvalido(f"O nome do idioma não pode exceder {const.MAX_IDIOMA} caracteres.")

        
    @property  # Uma Lista [] de objetos horario que mostra os horários do usuário.
    def horarios(self):
         return self._horarios
    
    @horarios.setter
    def horarios(self, h_list):
        if all(isinstance(h, Horario) for h in h_list):
            self._horarios = h_list


    @property  # Objeto do tipo carteira necessário para efetuar ou receber pagamentos das aulas.
    def carteira(self):
         return self._carteira

    @carteira.setter 
    def carteira(self, carteira):
        self._carteira = carteira

# b) Métodos: 
        
# i) imprimirRelatorio: Método abstrato que deve ser implementado pelas classes que herdam a classe Usuario.
# imprimir um relatório completo sobre as atividades do usuário.
        
    @abstractmethod
    def imprimirRelatorio(self):
        """ Método abstrato que deve ser implementado nas subclasses """
        pass
       
# 10) Implemente a classe Estudante como uma subclasse de Usuario:
     
# a) Atributos:
    
class Estudante(Usuario):
    def __init__(self,nome, email, paisOrigem, paisAtual,carteira, idiomas_aprender=None, historico_professores=None):
        super().__init__(nome, email, paisOrigem, paisAtual,carteira)
        self.idiomas_aprender = idiomas_aprender if idiomas_aprender is not None else []
        self.historico_professores = historico_professores if historico_professores is not None else []
        self.aulas_concluidas = [] # add: confirmação de aulas concluidas

# b) Métodos:
        
# i) imprimirRelatorio:
    def imprimirRelatorio(self):
        relatorio = {
            "Idiomas que sabe falar": self.idiomas_ja_sabe_falar(),
            "Idiomas que deseja aprender": self.idiomas_deseja_aprender(),
            "Horários do estudante": self.listar_horarios(),
            "Professores do estudante": self.lista_professores(),
            "Aulas concluídas": self.obter_aulas_concluidas,
            "Professor favorito": self.exibir_professor_favorito(),
            "Idioma favorito": self.exibir_idioma_favorito(),
            "Saldo da carteira": self.saldo_carteira()
        }
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")
            

#(1) Listar Idiomas que o estudante sabe falar;
    def idiomas_ja_sabe_falar(self):
         return [f"{idioma.idioma} (Nível {idioma.nivel})" for idioma in self.idiomas]
    
#(2) Listar Idiomas que o estudante deseja aprender;
    def idiomas_deseja_aprender(self):
        return [f"{idioma.idioma} (Nível {idioma.nivel})" for idioma in self.idiomas_aprender]
    
#(3) Listar horários do estudante;
    def listar_horarios(self):
        return self.horarios
    
#(4) Listar professores do estudante;
    def lista_professores(self):
        return [str(professor) for professor in self.historico_professores]
    
#(5) Listar aulas concluídas pelo estudante;
    def obter_aulas_concluidas(self):
        return self.aulas_concluidas
    
#(6) Exibir dados do professor favorito do estudante (com qual professor o estudante teve mais aulas, e quantas foram);
    def exibir_professor_favorito(self):
        if not self.historico_professores:
             return "Não há histórico de professores até o momento"
        
        professor_favorito = max(set(self.historico_professores), key=self.historico_professores.count)
        qtd_aulas_professor_favorito = self.historico_professores.count(professor_favorito)
        return f"Professor favorito: {professor_favorito}, com {qtd_aulas_professor_favorito} aulas."
    
#(7) Exibir idioma favorito do estudante (com qual idioma o estudante tevemais aulas, e quantas foram);
    def exibir_idioma_favorito(self):
        if not self.aulas_concluidas:
            return "Não há aulas concluídas ainda."
        
        idiomas_concluidos = [aula.idioma for aula in self.aulas_concluidas]
        idioma_favorito = max(set(idiomas_concluidos), key=idiomas_concluidos.count)
        qtd_aulas_idioma_favorito = idiomas_concluidos.count(idioma_favorito)
        return f"Idioma favorito: {idioma_favorito}, com {qtd_aulas_idioma_favorito} aulas."
    
#(8) Exibir saldo da carteira do estudante.
    def saldo_carteira(self):
        return self.carteira.saldo
          
# i) agendarAula:
    
    def agendar_aula(self, aula):
        self.horarios.append(aula.horario)
        self.idiomas.append(aula.idioma)
        
          
# iii) confirmarQueAulaFoiConcluida:
     
    def confirmar_aula_concluida(self, aula, carteira_sistema):
        if aula.horario in self.horarios:
            self.horarios.remove(aula.horario)
            self.aulas_concluidas.append(aula)
            
            # Transferir o valor da aula do estudante para o professor e sistema
            valor_sistema = aula.preco * 0.1
            valor_professor = aula.preco * 0.9

            self.carteira.transferir(aula.preco, aula.professor.carteira)
            aula.professor.carteira.transferir(valor_sistema, carteira_sistema)
            
        else:
            raise ErroAulaInvalida("Aula não encontrada nos horários do estudante")
        
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Email: {self.email}\n"
            f"País de Origem: {self.paisOrigem}\n"
            f"País Atual: {self.paisAtual}\n"
            f"Idiomas que sabe falar: {', '.join(self.idiomas_ja_sabe_falar())}\n"
            f"Idiomas que deseja aprender: {', '.join(self.idiomas_deseja_aprender())}\n"
            f"Horários do estudante: {', '.join(self.listar_horarios())}\n"
            f"Professores do estudante: {', '.join(self.lista_professores())}\n"
            f"Aulas concluídas: {', '.join(self.obter_aulas_concluidas())}\n"
            f"Professor favorito: {self.exibir_professor_favorito()}\n"
            f"Idioma favorito: {self.exibir_idioma_favorito()}\n"
            f"Saldo da carteira: {self.saldo_carteira()}"
        )

      
# 11) Implementar a classe Professor como uma subclasse de Usuario:


     
# a) Atributos:
     
class Professor(Usuario):
    def __init__(self,nome, email, paisOrigem, paisAtual,carteira, idiomas_ensina=None, historico_estudantes=None):
        super().__init__(nome, email, paisOrigem, paisAtual,carteira)
        self.idiomas_ensina =  idiomas_ensina if idiomas_ensina is not None else []
        self.historico_estudantes = historico_estudantes if historico_estudantes is not None else []
        self.aulas_concluidas = [] 

# b) Métodos:
          
# i) imprimirRelatorio do professor:
        
        # i) imprimirRelatorio:
    def imprimirRelatorio(self):
        relatorio = {
            "Idiomas que o professor sabe falar": self.idiomas_ja_sabe_falar(),
            "Idiomas que o professor ensina": self.idiomas_deseja_ensinar(),
            "Horários do professor": self.listar_horarios(),
            "Estudantes do professor": self.lista_estudantes(),
            "Aulas concluídas": self.obter_aulas_concluidas,
            "Saldo da carteira": self.saldo_carteira()
        }
        for chave, valor in relatorio.items():
            print(f"{chave}: {valor}")
     
#(1) Listar Idiomas que o professor sabe falar;
    def idiomas_ja_sabe_falar(self):
         return  [f"{idioma.idioma} (Nível {idioma.nivel})" for idioma in self.idiomas]
    
#(2) Listar Idiomas que o professor ensina;
    def idiomas_deseja_ensinar(self):
        return [f"{idioma.idioma} (Nível {idioma.nivel})" for idioma in self.idiomas_ensina]
    
#(3) Listar horários do professor;
    def listar_horarios(self):
        return self.horarios
    
#(4) Listar de estudantes do professor;
    def lista_estudantes(self):
        return self.historico_estudantes
    
#(5) Listar aulas concluídas pelo professor;
    def obter_aulas_concluidas(self):
        return self.aulas_concluidas

    
#(6) Exibir saldo da carteira do professor.
    def saldo_carteira(self):
        return self.carteira.saldo
          
# ii) aceitarPedidoDeAgendamento do professor:
    def Agendamento_Professor(self, aula): # (1) Se o professor está com horario indisponivel. 
        if aula.hora_inicio in self.horarios or aula.hora_fim in self.horarios: 
             return "Horário indisponível para o professor."  
    
    
        for estudante in self.historico_estudantes: 
            if aula.hora_inicio in estudante.horarios or aula.hora_fim in estudante.horarios: # Verificar se o horário do estudante está disponível
                 return f"Horário indisponível para o estudante {estudante.nome}." 
        self.aulas_concluidas.append(aula)# # (2) Horário do professor e do estudante devem ser marcados como não disponíveis. 
        for estudante in self.historico_estudantes:
          if estudante.nome == aula.estudante:
            estudante.aulas_concluidas.append(aula) 
            break
    
    
        self.horarios.append(aula.hora_inicio)
        self.horarios.append(aula.hora_fim)
        for estudante in self.historico_estudantes:
            if estudante.nome == aula.estudante: # (3) Usuários não podem ter duas aulas marcadas no mesmo horário.
                 estudante.horarios.append(aula.hora_inicio)
                 estudante.horarios.append(aula.hora_fim)
                 break
    
        return "Aula agendada com sucesso."  
    

# 12) Fornecer um método para imprimir o relatório do sistema, o qual deve informar a quantidade
#de estudantes e professores cadastrados, bem como o saldo da carteira do sistema. O método
#também deve imprimir o relatório de cada usuário cadastrado no sistema.

# imprimirRelatorioSistema:
def imprimirRelatorioSistema(estudantes, professores, carteira_sistema):
    print(f"----- Relatório do Professor -----\n")
    print(f"Quantidade de estudantes cadastrados: {len(estudantes)}") # (1) Informar quantidade de estudantes e professores cadastrados
    print(f"Quantidade de professores cadastrados: {len(professores)}") # (2) Atribuir os 10% das aulas na carteira do sistema.
    print(f"Saldo da carteira do sistema: {carteira_sistema.saldo}")

    for estudante in estudantes: # (3) Imprimir o relatório de cada usuário(alunos).
            print(estudante)

    for professor in professores: # (3) Imprimir o relatório de cada usuário(professores).
            print(professor)


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
         return f"Idioma: {self.idioma} - Nível: {self.nivel}!"


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
        return f"Tipo de aula: {self.idioma} - Preço: {self.preco} - ID {self.identificador}"

# 7) Implementar a classe Aula. Uma aula reúne informações como professor, estudante, horário, e
#tipo da aula.
# Herda de class TipoDeAula(idioma e obj TipoDeAula)
# Herda de class Horario horario
      
class Aula(Horario, TipoDeAula):
    def __init__(self, professor, estudante, idioma, nivel, preco, identificador, hora_inicio, hora_fim, dia_semana):
        TipoDeAula.__init__(self, idioma, nivel, preco, identificador)
        Horario.__init__(self, hora_inicio, hora_fim, dia_semana)
        self.horario = Horario(hora_inicio, hora_fim, dia_semana)
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
        return (f"Aula: {self.idioma} - Professor: {self.professor} - Estudante: {self.estudante}, "
                f"Preço: {self.preco} - ID : {self.identificador}, "
                f"Horário: {self.hora_inicio} - {self.hora_fim}, {self.dia_semana}")
           
            


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
    def saldo(self, saldo):
        if saldo >= 0:
                 self.__saldo = saldo
        else:
            raise ErroSaldoInvalido("Saldo deve ser positivo ou 0 !")
      
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            raise ErroDepositoInvalido("Só é permitido depositar um valor maior ou igual a 0 !")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo: # Especificação de erro.
            self.__saldo -= valor
        else:
            raise ErroSaqueIndisponivel("Esse valor excede o saldo disponível para saque !")
        
 # transferencias são feitas apenas na instancia Carteira
 # pra transferir:
 # (1)  Sacamos valor>0 da conta que transfere  
 # (2)  Depositamos valor na conta destino
        
    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Carteira): 
            raise ErroContaInvalida("Essa carteira não existente no sistema !")
        if 0 < valor <= self.__saldo: # Especificação de erro.
            self.sacar(valor)
            conta_destino.depositar(valor)   
        else:
            raise ErroSaldoInsuficiente("Transferências só podem ser feitas com valores menores ou iguaisque o saldo total disponível !") 
          
               




