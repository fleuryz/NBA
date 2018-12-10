import requests

#Função para criar url de busca de um jogo específico
def buscar_url_PlayByPlay(data, idJogo):
	return 'http://data.nba.net/json/cms/noseason/game/' + data + '/' + str(idJogo) + '/pbp_all.json'

#Função para cruar url de busca de IDs de todos os jogos em um ano
def buscar_url_IDsJogos(ano):
	return 'http://data.nba.net/json/cms/' + str(ano) + '/league/nba_games.json'

#Função para retornar o string de uma data
def get_data(dia, mes, ano):
	novoDia = dia
	novoMes = mes
	if dia<=9:
		novoDia = '0' + str(dia)
	if mes<=9:
		novoMes = '0' + str(mes)
	return str(ano) + str(novoMes) + str(novoDia)

#Escrever um arquivo .CSV com todos os jogos de um ano
def buscar_jogos(ano):

	url = buscar_url_IDsJogos(ano)

	resp = requests.get(url)

    nomeArquivo = 'Jogos' + str(ano) + '.csv'
    
	file = open(nomeArquivo, "w")

	file.write("Time Casa, Time Fora, ID, Dia, Mes, Ano, Hora\n") 

	for coisa in resp.json()['sports_content']['schedule']['game']:
		data = coisa['dt'].split(' ')[0].split('-')
		hora = coisa['dt'].split(' ')[1].split('.')[0]
		linha = coisa['v_abrv'] + ',' + coisa['h_abrv'] + ',' + str(coisa['id']) + ',' + str(data[2]) + ',' + str(data[1]) + ',' + str(data[0]) + ',' + str(hora) + '\n'
		file.write(linha)

	file.close()

#Definir a jogada realizada a partir do texto de narração de jogo
def buscar_jogada(jogada):
	return False
	

file = open("JogosIDs.csv", "r")

linhas = file.readlines()

url = buscar_url_PlayByPlay(get_data(25,10,2016), '0021600001')
resp = requests.get(url)

coisas = resp.json()

for jogada in coisas['sports_content']['game']['play']:
	hora = jogada['clock']
	if not buscar_jogada(jogada['description']):
		print jogada['description'] 
		

#pular = True
#for linha in linhas:
#	if pular:
#		pular = False
#		continue
#	dados = linha.split(',')
#	
#	url = buscar_url_PlayByPlay(get_data(dados[3],dados[4], dados[5]), dados[2])
#
#	resp = requests.get(url)
#
#	coisas = resp.json()
#
#	print dados[2]
#
#	print coisas['sports_content']['sports_meta']['season_meta']['display_season']
#
#	if coisas['sports_content']['sports_meta']['season_meta']['display_season'] != "Pre Season" :
#		print coisa['game']['play']
#	else:
#		print "erro"
#		
	
