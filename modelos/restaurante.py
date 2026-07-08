from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # self == this (java)
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False # ._ atributo privado
        self._avaliacao = []

        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} - {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'inativo'
    
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = soma_notas / quantidade_notas
        return round(media, 1)