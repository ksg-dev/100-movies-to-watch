import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.encoding = "utf-8"
content = response.text


soup = BeautifulSoup(content, "html.parser")

movies = []

titles = soup.find_all(name="h3", class_="title")

for title in titles:
    movie = title.getText()
    movies.append(movie)


title_list = []
for movie_name in movies:
    try:
        movie_tups = movie_name.split(")")[1].strip()
    except IndexError:
        movie_tups = movie_name.split(":")[1].strip()
    title_list.append(movie_tups)


sorted_list = reversed(title_list)


start = 1
with open("movies.txt", mode="w") as file:
    for title_name in sorted_list:
        formatted_title = f"{start}) {title_name}\n"
        file.write(f"{formatted_title}")
        start += 1
