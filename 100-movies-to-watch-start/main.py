import requests
# import pandas
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

respone = requests.get(URL)

empireon_web_page = respone.text

soup = BeautifulSoup(empireon_web_page, 'html.parser')

section_heading = [ tilte.getText() for tilte in soup.find_all(name = 'h3', class_='title')]
movies = section_heading[::-1]
# print(section_heading)

# data = pandas.DataFrame(section_heading[::-1])
# data.to_csv('movies_list.csv', index=False)

with open('movie.text', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
    
