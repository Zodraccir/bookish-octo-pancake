"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys
import requests
from bs4 import BeautifulSoup

URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2013,2013"

def get_top_grossing_movie_links(url):
    """Return a list of tuples containing the top grossing movies of 2013 and link to their IMDB
    page."""
    response = requests.get(url)
    movies_list = []
    for each_url in BeautifulSoup(response.text).select('a[href*="/title/"]'):
        movie_title = each_url.text 
        if movie_title != 'X' and len(movie_title)>1:
            movies_list.append(movie_title)
    return movies_list



def main():
    """Main entry point for the script."""
    movies = get_top_grossing_movie_links(URL)
    with open('output.csv', 'w') as output:
        row="start"
        for title in movies:
            row=row+";"+title
        output.write(row)

if __name__ == '__main__':
    sys.exit(main())