# 🌦 Weather API - Flask + OpenWeatherMap

Este é um projeto simples de API em Python utilizando o framework Flask. A API consome dados da OpenWeatherMap para exibir informações climáticas de uma cidade fornecida pelo usuário.

---

## 🚀 Como funciona?

A rota principal é:
GET /weather/<cidade>

🔎 Exemplo:
GET /weather/Tokyo

### 🔁 Resposta JSON:
json
{
  "cidade": "Tokyo",
  "temperatura": 23.5,
  "descricao": "céu limpo"
}
Caso a cidade não exista:
{
  "erro": "Cidade não encontrada"
}

⚙️ Como rodar o projeto localmente
1. Clone o repositório
git clone https://github.com/mathorita/weather-Flask.git
cd weather-Flask

3. Crie um ambiente virtual
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

Se não tiver o arquivo requirements.txt, basta instalar:
pip install flask requests

4. Adicione sua chave da API do OpenWeatherMap
Edite o arquivo city.py e substitua:
API_KEY = "SUA_CHAVE_AQUI"
com sua chave da OpenWeatherMap.

5. Rode a aplicação
python app.py
Acesse em:

arduino
http://127.0.0.1:5000/weather/Sao Paulo
🧠 Tecnologias utilizadas
Python 3

Flask

Requests

OpenWeatherMap API

