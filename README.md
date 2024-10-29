<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>API Documentation</h1>
<p>
    Bem-vindo à documentação da API para o sistema de gerenciamento de empresas. Esta API foi desenvolvida para manipular e validar informações de empresas, facilitando a integração de dados administrativos.
</p>
 
<h2>Funcionalidades</h2>
<ul>
<li>Validação e recebimento de dados empresariais: Recebe e valida informações essenciais sobre empresas, verificando campos obrigatórios e o formato dos dados.</li>
<li>Resposta detalhada em caso de erros: A API retorna mensagens claras e estruturadas, facilitando a identificação e correção de problemas.</li>
<li>Campos suportados: São validados campos como email, nome da empresa, unidade federativa, porte e natureza jurídica, além de detalhes de início de atividades.</li>
</ul>

<h2>Campos Obrigatórios</h2>
<p>Os seguintes campos devem estar presentes na requisição:</p>
<ul>
<li><strong>email:</strong> Endereço de e-mail da empresa. (Formato: string)</li>
<li><strong>nome_empresa:</strong> Nome da empresa (até 100 caracteres).</li>
<li><strong>uf:</strong> Unidade Federativa, aceitando valores específicos (ex. SP, RJ).</li>
<li><strong>porte_empresa:</strong> Porte da empresa (Micro Empresa, Empresa de Pequeno Porte, Outros).</li>
<li><strong>capital_social:</strong> Capital social em reais (formato: inteiro).</li>
<li><strong>municipios:</strong> Município de registro, sem acentos.</li>
<li><strong>cnaes:</strong> Classificação de atividades econômicas.</li>
<li><strong>natureza_juridica:</strong> Natureza jurídica da empresa.</li>
<li><strong>ano_inicio_ativ:</strong> Ano de início das atividades (inteiro).</li>
<li><strong>mes_inicio_ativ:</strong> Mês de início das atividades (1-12).</li>
<li><strong>dia_inicio_ativ:</strong> Dia de início das atividades (1-31).</li>
</ul>
 
<h2>Estrutura de Requisição</h2>

<p><strong>Endpoint:</strong> (POST) /getResponse/</p>
 
<p><strong>Exemplo de Body:</strong></p>
<pre>
{
    "email": "contato@exemplo.com",
    "nome_empresa": "Exemplo LTDA",
    "uf": "SP",
    "porte_empresa": "Micro Empresa",
    "capital_social": 50000,
    "municipios": "SAO PAULO",
    "cnaes": "Comércio varejista de artigos do vestuário e acessórios",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "ano_inicio_ativ": 2015,
    "mes_inicio_ativ": 6,
    "dia_inicio_ativ": 15
}
</pre>
 
<h2>Tratamento de Erros</h2>
 
<h3>Erro de Colunas Ausentes</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre quando a requisição enviada não contém todas as colunas obrigatórias.</li>
<li><strong>Código HTTP:</strong> 400 Bad Request</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "missing required columns",
    "missing_columns": ["nome_empresa", "capital_social"]
}
</pre>
</li>
</ul>
 
<h3>Erro de Conexão com o Banco de Dados</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre quando a API não consegue estabelecer conexão com o banco de dados.</li>
<li><strong>Código HTTP:</strong> 500 Internal Server Error</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "Database connection failed"
}
</pre>
</li>
</ul>
 
<h3>Erro de Processamento Interno</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre quando há uma exceção inesperada durante o processamento da requisição.</li>
<li><strong>Código HTTP:</strong> 500 Internal Server Error</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "An error occurred during processing"
}
</pre>
</li>
</ul>
 
<h3>Erro ao Carregar o Pipeline</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre quando há uma falha ao carregar o modelo de previsão a partir do arquivo pipeline.pkl.</li>
<li><strong>Código HTTP:</strong> 500 Internal Server Error</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "Failed to load prediction model",
    "details": "The model file 'pipeline.pkl' could not be found"
}
</pre>
</li>
</ul>
 
<h3>Erro de Execução da Previsão</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre se houver falha ao executar a previsão, como problemas com os dados fornecidos ao modelo.</li>
<li><strong>Código HTTP:</strong> 500 Internal Server Error</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "Prediction execution failed",
    "details": "The input data is not compatible with the prediction model"
}
</pre>
</li>
</ul>
 
<h3>Erro de Formato de Dados Inválido</h3>
<ul>
<li><strong>Descrição:</strong> Esse erro ocorre quando algum campo possui o formato incorreto (por exemplo, capital_social não é um inteiro).</li>
<li><strong>Código HTTP:</strong> 400 Bad Request</li>
<li><strong>Resposta JSON:</strong>
<pre>
{
    "error": "Invalid data format",
    "invalid_fields": ["capital_social", "ano_inicio_ativ"]
}
</pre>
</li>
</ul>
 
<h2>Criador</h2>
<ul>
<li><strong>Nome do Criador:</strong> Marcus Vinicius Righeto Thomazetti <a href="https://github.com/MarcusVinciusRT">GitHub</a></li>
<li><strong>Nome do Criador:</strong> Davi de Siqueira Cavalacante <a href="https://github.com/davaslindo">GitHub</a></li>
</ul>
</body>
</html>