import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da coleção da Steam (substitua pelo link da sua coleção, se necessário)
url_colecao = "https://steamcommunity.com/sharedfiles/filedetails?id=3474671993"

# Fazer a requisição à página da coleção com cabeçalhos para simular um navegador
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url_colecao, headers=headers)

# Verificar se a página foi acessada com sucesso
if response.status_code != 200:
    print(f"Erro ao acessar a página da coleção: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar os itens dos mods na página da coleção
# Ajuste o seletor após inspecionar a página (exemplo: 'div.collectionItem')
mod_items = soup.find_all('div', class_='collectionItem')

# Verificar se os itens foram encontrados
print(f"Número de mods encontrados: {len(mod_items)}")
if len(mod_items) == 0:
    print("Nenhum mod encontrado. Verifique o seletor para os itens dos mods.")
    exit()

# Lista para armazenar os dados dos mods
dados_mods = []

# Extrair nome e descrição diretamente da página da coleção
for item in mod_items:
    # Extrair o nome do mod (ajuste o seletor)
    nome = item.find('div', class_='workshopItemTitle')
    nome = nome.text.strip() if nome else "Nome não encontrado"
    autor = item.find('span', class_="workshopItemAuthorName")
    autor = autor.text.strip()
    link = item.find('div', class_='workshopItem')
    link = link.find('a')
    link = link.get('href')
    # Extrair a descrição (não há descrição completa na página da coleção, apenas títulos)
    # Para descrições completas, seria necessário acessar cada página individual, mas como você quer simplificar,
    # vamos assumir que a descrição inicial não está disponível diretamente na coleção
    imagem = item.find('img', class_='workshopItemPreviewImage')
    imagem = imagem.get('src')
    descricao = item.find('div', class_='workshopItemShortDesc')
    descricao = descricao.text.strip()
    avaliacao = item.find('img', class_='fileRating')
    avaliacao = avaliacao.get('src')

    # Adicionar os dados à lista
    if nome:
        print(f"Mod encontrado: {nome},{imagem}")
        dados_mods.append({
            'Nome': nome,
            'Imagem': imagem,
            'Descrição': descricao,
            'Avaliação': avaliacao,
            'Autor': autor,
            'Link': link
        })

# Criar uma tabela com pandas
if dados_mods:
    df = pd.DataFrame(dados_mods)
    # Salvar a tabela em um arquivo CSV
    df.to_csv('mods.csv', index=False, encoding='utf-8', sep=';')
    print("Tabela gerada com sucesso! Veja o arquivo 'mods.csv'.")
else:
    print("Nenhum dado foi extraído. Verifique os seletores.")