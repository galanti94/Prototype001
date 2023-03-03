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