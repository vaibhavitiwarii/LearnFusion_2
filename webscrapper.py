import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_headings(soup):
    headings = []
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headings.append(heading.text.strip())
    return headings

def main(url):
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        headings = extract_headings(soup)
        for heading in headings:
            print(heading)
    else:
        print("Failed to retrieve the web page.")


if __name__ == "__main__":
    url = "https://example.com"
    main(url)
