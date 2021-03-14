import requests
from bs4 import BeautifulSoup
import csv

# url for parser
url = 'https://www.olx.ua/uk/elektronika/noutbuki-i-aksesuary/'


def write_csv(result):
    """
    Write all parsed data from web page in csv file
    """
    with open ('parsed.csv', 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['set=,'])
        for i in result:
            # tags
            writer. writerow((i['name'],
                              i['price'],
                              i['address'],
                              i['url']
                              ))


def clean(text):
    """
    Replace all "\n" and "\t" to " "
    """
    return text.replace('\t', '').replace('\n', '').strip()
    


def get_data(url):
    """
    With bs4 get materials from url page
    """
    # features="html.parser"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    table = soup.find('table', {'id': 'offers_table'})
    rows = table.find_all('tr', {'class': 'wrap'})
    result = []
    for row in rows: 
        name = clean(row.find('h3').text)
        url = row.find('h3').find('a').get('href') # <a href=" "/>
        price = clean(row.find('p', {'class': 'price'}).text) # find p with hte class price
        bottom = row.find('td', {'valign': 'bottom'})
        address = clean(bottom.find('small', {'class': 'breadcrumb x-normal'}).text)
        item = {'name': name, 'price': price, 'address': address, 'url': url}
        result.append(item)
    return result
    
# main func
def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    result = []
    for i in range(1, 5+1):
        print(f'Parsing page# {str(i)} of {str(5)}')
        page_url = url + '?page=' + str(i)
        result += get_data(page_url)
    write_csv(result)

if __name__ == '__main__':
    main(url)

