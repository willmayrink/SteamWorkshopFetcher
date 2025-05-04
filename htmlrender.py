import pandas as pd

# Ler o arquivo CSV
csv_file = 'mods.csv'
df = pd.read_csv(csv_file, sep=';')  # Ajuste o delimitador conforme usado no CSV

# Verificar se o DataFrame contém dados
if df.empty:
    print("O arquivo CSV está vazio. Verifique o arquivo 'mods.csv'.")
    exit()

# Função para limitar o número de caracteres
def limitar_texto(texto, max_chars=100):
    if len(texto) > max_chars:
        return texto[:max_chars].rsplit(' ', 1)[0] + '...'  # Corta na última palavra completa
    return texto

# Iniciar o código HTML com um template básico usando Bootstrap
html_content = """
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mods da Steam</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .mod-container {
            margin-bottom: 20px;
        }
        .mod-image {
            max-width: 100%;
            height: auto;
            object-fit: cover; /* Garante que a imagem preencha o espaço */
        }
        .card-text {
            display: -webkit-box;
            -webkit-line-clamp: 2; /* Limita a 3 linhas */
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
        }
    </style>
</head>
<body>
    <div class="container mt-5" style="width: 90%; margin:auto">
        <h1>Lista de Mods</h1>
        <div class="row d-flex justify-content-center g-0 gap-3">
"""

# Adicionar cada mod ao HTML
for index, row in df.iterrows():
    nome = row['Nome']
    imagem = row['Imagem']
    descricao = row['Descrição']
    avaliacao = row['Avaliação']
    autor = row['Autor']
    link = row['Link']

    # Limitar a descrição a 100 caracteres
    descricao_limitada = limitar_texto(descricao, max_chars=100)

    # Criar um bloco HTML para cada mod
    mod_html = f"""
        <div class="card mb-3 shadow-lg rounded-4 ms-2 me-2" style="max-width: 440px; max-height: 148px;">
        <div class="row g-0">
          <div class="col-md-4 col">
            <img src="{imagem}" class="img rounded-start-4 mod-image" alt="'82 Porsche 911">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <a href="{link}" class="text-decoration-none link-light" target="_blank"><span class="card-title fw-bold">{nome}</span><img src="{avaliacao}" class="pb-1 m-2"><span class="badge rounded-pill bg-indigo position-relative">{autor}</span>
              <p class="card-text text-body-secondary"><small>{descricao}</small></p></a>
            </div>
          </div>
        </div>
      </div>
    """
    html_content += mod_html

# Fechar o HTML
html_content += """
    </div>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Salvar o HTML em um arquivo
with open('mods.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Arquivo 'mods.html' gerado com sucesso! Abra-o em um navegador para visualizar.")