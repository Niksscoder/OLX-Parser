import requests
from bs4 import BeautifulSoup
import csv

# all computers which price more then 8000zl
url = 'https://www.olx.pl/elektronika/komputery/laptopy/?search%5Bfilter_float_price%3Afrom%5D=8000&search%5Bfilter_enum_state%5D%5B0%5D=new'


def write_csv(result):
    """
    Write all parsed materials in csv file
    """
    with open ('parsed.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['set=,'])
        for i in result:
            writer. writerow((i['name'],
                              i['price'],
                              i['address'],
                              i['url']))


def clean():
    """
    Replace all "\n" and "\t" to " "
    """
    pass


def get_data():
    """
    With bs4 get materials from url page
    """
    pass

def main(url):
    print("I'm working, but not yet completely (")


if __name__ == '__main__':
    main(url)

