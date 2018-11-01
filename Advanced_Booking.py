import requests
import re
from bs4 import BeautifulSoup as BS


def Connection(city):                                            #Function to check is the city exists on the WebPage
    url = 'https://in.bookmyshow.com/{}/movies'.format(city)
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    try:
        response.status_code != 200
    except:
        ArithmeticError("The site is not parseable")


def Parse(city):                                                 #Function to ask the movie and parse the info from the Webpage
    print("Enter a word of the movie you want to be informed")
    movie_name = input()
    while (True):
        url = 'https://in.bookmyshow.com/{}/movies'.format(city)
        response = requests.get(url)
        soup = BS(response.text, 'lxml')
        movie_titles = []
        movies = soup.select('a.__movie-name')

        for movie in movies:                                     #A for loop to check all the movies in the webpage and save it in a list
            movie_titles.append(movie.get('title'))
        # print(movie_titles)

        pattern = re.compile(movie_name)                         #Making a pattern object of our given moive name
        for movie in movie_titles:
            matches = pattern.finditer(movie)                   #A for loop to find the pattern of the given movie name in the movie list
            if matches != None:
                for match in matches:
                    Movie_found = movie + "\nThe Advanced booking for this movie is out"

                    return Movie_found


def main():
    print("Enter your city")
    city_name = input()
    Connection(city_name)
    Movie_found = Parse(city_name)
    print(Movie_found)


main()
