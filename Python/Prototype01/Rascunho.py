import json
dict1 = {'um':1, 'dois':2, 'três':3}
dict2 = {'quatro':4, 'cinco':5, 'seis':6}

ref_arquivo = open("Python/Prototype01/informacoes.txt","r", encoding='utf-8')

novo_dict = ref_arquivo.read().replace('-', '').replace('\n', '').split(':')
del novo_dict[0]

lista_tags = novo_dict[5].split(',')
for i in range(len(lista_tags)): lista_tags[i] = lista_tags[i].strip()
print(lista_tags)
for i in lista_tags: print(i)



ref_arquivo.close()