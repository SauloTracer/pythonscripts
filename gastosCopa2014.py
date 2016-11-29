import urllib.request
url = 'http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento'
resp = urllib.request.urlopen(url).read().decode('utf-8')
total = 0
j = 0
while j != -1:
    abre = '<valorTotalPrevisto>'
    fecha = '</'
    j = resp.find(abre,j)
    if j == -1:
        break
    k = resp.find(fecha,j)
    v = resp[j+len(abre):k]
    print(v)
    total += float(v)
    j = k + len(fecha)
print ("R$ {:.2f}".format(total))
