from bs4 import BeautifulSoup

def truncate_and_add_read_more(paragraph, max_length=400):
    paragraph_text = paragraph.get_text()

    if len(paragraph_text) > max_length:
        truncated_text = paragraph_text[:max_length] + '...Read More'
        paragraph.string = truncated_text

with open('scienceandmathwebsite\Homepage\\templates\homepage.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

paragraph = soup.find('p', {'id': 'article1text'})

if paragraph:
    truncate_and_add_read_more(paragraph)

    with open('scienceandmathwebsite\Homepage\\templates\homepage.html', 'w') as file:
        file.write(str(soup))
else:
    print("Paragraph with id 'article1text' not found in the HTML content.")

