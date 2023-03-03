kw_a = ['ler', 'somar','ler', 'somar','ler', 'somar']

set_kw_a = set(kw_a)

kw_count = {}

for unique_kw in set_kw_a:
    count = 0
    for kw in kw_a:
        if unique_kw == kw: 
            count += 1
    kw_count[f'{unique_kw}'] = count

print(type(['ler', 'somar']) == list)

sorted(kw_count.items(), key=lambda x: x[1], reverse=True)