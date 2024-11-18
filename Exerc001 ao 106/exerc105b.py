def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['média'] = sum(n) / len(n)    
    if sit:
        if r['média'] >= 7:
            r['sit'] = 'Aprovado'
        elif r['média'] >= 5:
            r['sit'] = 'Razoavel'
        else:   
            r['sit'] = 'Reprovado'
    return r

resposta = notas(7,8,9,10,4, sit=True)
print(resposta)
