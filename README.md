# BBC News Scraper

## Descrição
Ferramenta de web scraping para extrair as últimas notícias da BBC. Desenvolvido em Python, utilizando as bibliotecas `requests` e `BeautifulSoup` para processamento HTML.

## Funcionalidades Principais
### Extração de Notícias
- Extrai os títulos, links e horários de notícias
- Suporta páginas principais da BBC
- Armazenamento de dados extraídos em formato estruturado

## Requisitos Técnicos
- Python 3.x
- Bibliotecas `requests` e `beautifulsoup4`

Instalação das dependências:
```bash
pip install requests beautifulsoup4
```

## Como Utilizar
1. Execute o script no terminal:
   ```bash
   python bbc_news_scraper.py
   ```

2. O script buscará automaticamente as notícias mais recentes na página principal da BBC

3. As notícias serão exibidas no terminal com título, link e horário relativo de publicação

## Exemplo de Saída
```plaintext
- Título: Ex-US senator's wife convicted in gold bars bribery scheme
- Link: https://www.bbc.com/news/c70zlj8dpn8o
- Horário: 6 hrs ago
```

## Licença
MIT License - Disponível para uso e modificação. Consulte o arquivo LICENSE para detalhes.

--------------------------------------

# BBC News Scraper

## Description
A web scraping tool to extract the latest news from BBC. Developed in Python using the `requests` and `BeautifulSoup` libraries for HTML processing.

## Key Features
### News Extraction
- Extracts titles, links, and publication times of news articles
- Supports BBC's main page
- Stores extracted data in a structured format

## Technical Requirements
- Python 3.x
- `requests` and `beautifulsoup4` libraries

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## How to Use
1. Run the script in the terminal:
   ```bash
   python bbc_news_scraper.py
   ```

2. The script will automatically fetch the latest news from BBC's main page.

3. The news will be displayed in the terminal with the title, link, and relative publication time.

## Example Output
```plaintext
- Title: Ex-US senator's wife convicted in gold bars bribery scheme
- Link: https://www.bbc.com/news/c70zlj8dpn8o
- Time: 6 hrs ago
```

## License
MIT License - Available for use and modification. See the LICENSE file for details.
