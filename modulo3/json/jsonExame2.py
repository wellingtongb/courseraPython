import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ') #solicitando a universidade para o usuario
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address}) #concatenando enderecos e passando os parametros que a API pede
    print 'Retrieving', url
    uh = urllib.urlopen(url)    #abrindo o endereco ja concatenado
    data = uh.read()            #lendo o site
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data)) #criando objeto json e carregando o json do endereco passado
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        continue

    location = js['results'][0]['place_id']     #parseando o json e buscando a id do endereco passado pelo usuario
    print location
