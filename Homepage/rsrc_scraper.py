# Currently this script scrapes only the noaa.gov website for science related videos
# This is an early prototype of the full thing, just as a proof of concept and to make sure their content is scrapable
# I plan to use a similar script to get other resources (legally)

# legality -> https://sos.noaa.gov/copyright/
# tldr on the above link i can use this since my website is educational
# i will make sure to give the noaa credit somewhere on the page once i get to deploying this thing

# issues -> very slow runtime at least on my machine | needs immediate fix or this thing will cause many issues

# is still functional tho


# instead of storing on a database ( due to storage concerns with mongodb my preferred backend ), i'll use a plain text 
#                                                                                                 json file and some dynamic 
#                                                                                                 html using a basic js script 
#                                                                                                 to display a random video from 
#                                                                                                 the given list


from bs4 import BeautifulSoup
import requests
import os

def main(base_url, url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    video_links = soup.find_all('a', href=lambda href: href and href.endswith('.mov'))

    download_dir = 'downloaded_videos'
    os.makedirs(download_dir, exist_ok=True)

    for link in video_links:
        video_url = base_url + link['href']
        
        video_name = os.path.basename(video_url)
        
        video_path = os.path.join(download_dir, video_name)
        
        response = requests.get(video_url)
        
        with open(video_path, 'wb') as f:
            f.write(response.content)
            
main('https://sos.noaa.gov', 'https://sos.noaa.gov/catalog/datasets/a-global-tour-of-precipitation/')