from bs4 import BeautifulSoup
import requests
import re

def scrape(link):
    page = requests.get('https://en.wikipedia.org' + link['href'])
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1').text.strip()
    f = open(title + '.txt', 'w', encoding='utf-8')
    output = title + '\n'
    for header in soup(['h2', 'h3']):
        targets = {'signs', 'symptoms', 'treatment', 'diagnosis'}
        if any(target in header.text.lower() for target in targets):
            output += '\n' + header.text.strip() + '\n'
            for section in header.next_siblings:
                if section.name == 'h2':
                    break
                elif section.name == 'p' or section.name == 'h3':
                    output += section.text.strip() + '\n'
    f.write(re.sub('[\[].*?[\]]', '', output.strip()))

def scrape_list(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1').text
    f = open(title + '.txt', 'w', encoding='utf-8')
    output = ''
    i = 0
    for element in soup('div', class_='div-col'):
        output += element.text
        links = element('a', href=True)
        for link in links:
            print(i)
            i += 1
            if link:
                scrape(link)
    f.write(re.sub('[\[].*?[\]]', '', output.strip()))

if __name__ == '__main__':
    scrape_list('https://en.wikipedia.org/wiki/List_of_feline_diseases')