import matplotlib.pyplot as plt

class Aluno:
    def __init__(self, kw):
        self._kw = kw

    def getKw(self):
        return self._kw

    # Função para adicionar novas KW de acordo com as respostas
    def addKw(self, new):
        if type(new) == list:
            for i in new:
                self._kw.append(i)
        else:
            self._kw.append(new)

    # Função para retornar um dicionário com as KW e contagem
    def diagnostico(self, kws):
        set_kws = set(kws)
        kw_count = {}
        for unique_kw in set_kws:
            count = 0
            for kw in kws:
                if unique_kw == kw: 
                    count += 1
            kw_count[f'{unique_kw}'] = count
        return dict(sorted(kw_count.items(), key=lambda x: x[1], reverse=True))

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


# Criando a prova **do jeito mais preguiçoso possível**
questao1 = Questao(enunciado='Dois meninos...', 
                  alternativa_a='5', alternativa_b='10', alternativa_c='15', 
                  kw_a=['ler', 'somar'], kw_b='somar', kw_c='multiplicar')

questao2 = Questao(enunciado='Dois meninos...', 
                  alternativa_a='5', alternativa_b='10', alternativa_c='15', 
                  kw_a=['ler', 'somar'], kw_b='somar', kw_c='multiplicar')

questao3 = Questao(enunciado='Dois meninos...', 
                  alternativa_a='5', alternativa_b='10', alternativa_c='15', 
                  kw_a=['ler', 'somar'], kw_b='somar', kw_c='multiplicar')

# Modelando o aluno
guilherme = Aluno([])
guilherme.addKw(questao1.kw_assinalada('a'))
guilherme.addKw(questao2.kw_assinalada('a'))
guilherme.addKw(questao3.kw_assinalada('a'))
guilherme.addKw(questao3.kw_assinalada('c'))

# Plotando gráficos
D = guilherme.diagnostico(guilherme.getKw())
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.show()