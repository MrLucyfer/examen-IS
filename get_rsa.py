import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='RSA problems')
parser.add_argument('-p', help="Factorize primes")

args = parser.parse_args()

def factorize(num):
    req = requests.get('http://factordb.com/index.php?query={}'.format(num))
    soup = BeautifulSoup(req.text, 'lxml')
    all_a = soup.find_all('font')
    all_a = all_a[:-1]

    p = all_a[0].text
    n = all_a[1].text

    print('{} factorized -> N: {} P: {}'.format(num, n, p))

factorize(args.p)


