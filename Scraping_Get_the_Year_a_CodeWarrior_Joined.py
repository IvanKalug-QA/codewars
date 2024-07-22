# #Task: Write a function get_member_since which accepts a username from someone at Codewars and returns an string containing the month and year separated by a space that they joined CodeWars.
#
# ###If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though because the server may time out.
#
# #Example:
#
# >>> get_member_since('dpleshkov')
# Jul 2016
# >>> get_member_since('jhoffner')
# Oct 2012
# #Libraries/Recommendations:
#
# ##Python:
#
# urllib.request.urlopen: Opens up a webpage.
# re: The RegEx library for Python.
# bs4(BeautifulSoup): A tool for scraping HTML and XML.
# Python 2 is not working for this kata. :(
# #Notes:
#
# Time out / server errors often happen with the test cases depending on the status of the codewars website. Try submitting your code a few times or at different hours of the day if needed.
# Feel free to voice your comments and concerns in the discourse area.

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
def get_member_since(username):
    url = urljoin('https://www.codewars.com/users/', username)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stat = soup.find('div', attrs={'class': 'w-full px-0'}).find_all('div', attrs={'class': 'stat-box mt-1 mb-1 md:mb-0'})[1].find_all('div', attrs={'class': 'stat'})
    return stat[0].text.split(':')[-1]