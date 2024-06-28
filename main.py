import requests
from bs4 import BeautifulSoup
from operator import itemgetter

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

movies = []

titles = soup.find_all(name="h3", class_="title")

for title in titles:
    movie = title.getText()
    movies.append(movie)


sorted_list = []
for movie_name in movies:
    try:
        movie_tups = movie_name.split(")")[1].strip()
    except IndexError:
        movie_tups = movie_name.split(":")[1].strip()
    sorted_list.append(movie_tups)
    print(movie_tups)

print(sorted_list)


# for movie in sorted_movies:
#     with open("movies.txt", mode="w") as file:
#         file.write(f"{movie}\n")

# print(sorted_movies)
# item = sorted_movies[0].split(")")
# print(item)
# print(final_list)
