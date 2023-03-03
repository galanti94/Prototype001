import matplotlib.pyplot as plt
from Aluno import Aluno
from Questao import Questao


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