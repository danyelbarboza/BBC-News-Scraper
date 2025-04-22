import requests
from bs4 import BeautifulSoup

def get_bbc_news():
    res = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(res.text, "html.parser")
    
    articles = soup.find_all("div", attrs={"data-testid": "dundee-card"})
    
    all_articles = []
    
    for article in articles:
        link_tag = article.find("a", href=True)
        title_tag = article.find("h2", attrs={"data-testid": "card-headline"})
        time_tag = article.find("span", attrs={"data-testid": "card-metadata-lastupdated"})

        if link_tag and title_tag:
            title = title_tag.text.strip()
            link = link_tag['href']
            if link.startswith("/"):
                link = "https://www.bbc.com" + link
            time_text = time_tag.text.strip() if time_tag else "Horário não encontrado"

        
            all_articles.append({
            'title': title,
            'link': link,
            'time': time_text
        })
    
    return all_articles



for item in get_bbc_news():
    print(f"- Título: {item['title']}\n- Link: {item['link']}\n- Horário: {item['time']}\n\n")