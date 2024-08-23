from modelos.avaliacao import Avaliacao

class Restaurante:
    # Lista que armazena todos os restaurantes cadastrados
    restaurante = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        # Retoma uma representação textual do restaurante, mostrando nome e categoria
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        # Exibi a lista de todos os restaurantes cadastrados
        print("")
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nomeljust(25)} | {restaurante._categorialjust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        # Retorn um símbolo visual representando se o restaurante está ativo ou inativo
        return '⌧' if self._ativo else '☐'
    
    def receber_estado(self):
        # Alterna o estado do restaurante entre ativo e inativo
        self._ = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        # Adiciona uma nova avaliação ao restaurante, desde que a nota esteja entre 0 a 10
        if 0 <= nota <=10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print("A nota deve estar entre 0 a 10")

        @property
        def media_avaliacoes(self):
            # Calcula e retorna a média das avalições do restaurante
            if not self._avaliacao:
                return'-'
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas / quantidade_de_notas, 1)
            return media