from bs4 import BeautifulSoup

with open('articles/NYT/www.nytimes.com/2023/10/03/us/politics/trump-stolen-election.html') as article:
    page_contents = article.read()

    soup = BeautifulSoup(page_contents, 'html.parser')

    paragraphs = soup.find_all('p')

    for line in paragraphs:
        print(line.get_text())
