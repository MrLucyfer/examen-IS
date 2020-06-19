import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='RSA problems')
parser.add_argument('-p', help="Factorize primes")
parser.add_arguments('-s', help="Sign message")
args = parser.parse_args()

def factorize(num):
    req = requests.get('http://factordb.com/index.php?query={}'.format(num))
    soup = BeautifulSoup(req.text, 'lxml')
    all_a = soup.find_all('font')
    all_a = all_a[:-1]

    p = int(all_a[0].text)
    n = int(all_a[1].text)

    phi = (p-1) * (n - 1)

    print('{} factorized -> N: {} P: {}'.format(num, n, p))

if args.p:
    factorize(args.p)


