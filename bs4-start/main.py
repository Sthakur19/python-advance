from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

# print(response.text)

soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = soup.find_all(name='a', rel='noreferrer')

article_links = []
article_texts = []

for article in article_tag:
    article_text = article.getText()
    article_link = article.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)
    

# article_tag_link = article_tag.get('href')
article_tag_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(article_texts)
# print(article_links)
article_index = article_tag_upvote.index(max(article_tag_upvote))
print(max(article_tag_upvote), article_index)
print(article_links[article_index])
print(article_texts[article_index])

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)

# anchor_tag = soup.find_all(name='a')
# print(anchor_tag)

# for tag in anchor_tag:
#     # print(tag.getText())
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading)
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# company_url = soup.select_one(selector='p a')
# print(company_url)

# headings = soup.select('.heading')
# print(headings)