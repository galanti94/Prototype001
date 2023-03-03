class Questao:
    def __init__(self, 
    enunciado, alternativa_a, alternativa_b, alternativa_c, kw_a, kw_b, kw_c):
        self.nome = enunciado
        self.alternativa_a = alternativa_a
        self.alternativa_b = alternativa_b
        self.alternativa_c = alternativa_c
        self._kw_a = kw_a
        self._kw_b = kw_b
        self._kw_c = kw_c
    
    # Só tem 3 alternativas porque eu estava com preguiça =,(
    def kw_assinalada(self, alternativa):
        match alternativa:
            case 'a':
                return self._kw_a
            case 'b':
                return self._kw_b
            case 'c':
                return self._kw_c
            case _:
                print("Somente a, b ou c!")