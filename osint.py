import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template
import concurrent.futures

app = Flask(__name__)

# Twitter Scraper (Basic public profile scraping)
def search_twitter(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('title').text.split('(')[0].strip()
        bio = soup.find('div', {'data-testid': 'UserDescription'}).text if soup.find('div', {'data-testid': 'UserDescription'}) else "No bio available"
        followers = soup.find('a', {'href': f'/{username}/followers'}).text if soup.find('a', {'href': f'/{username}/followers'}) else "0"

        return {
            'platform': 'Twitter',
            'name': name,
            'bio': bio,
            'followers_count': followers,
            'profile_url': url
        }
    else:
        return {'platform': 'Twitter', 'error': 'Profile not found or inaccessible'}

# Google Search (Web scraping with BeautifulSoup)
def search_google(username):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    url = f"https://www.google.com/search?q={username}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for g in soup.find_all('div', class_='tF2Cxc'):
            title = g.find('h3').text if g.find('h3') else "No title"
            link = g.find('a')['href'] if g.find('a') else "No link"
            snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else "No snippet"

            results.append({'title': title, 'link': link, 'snippet': snippet})

        return {'platform': 'Google', 'results': results}
    else:
        return {'platform': 'Google', 'error': 'Failed to fetch results'}

# Instagram Scraper (Simplified, based on public profile)
def search_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('title').text.split('(')[0].strip()
        bio = soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else "No bio available"

        return {
            'platform': 'Instagram',
            'name': name,
            'bio': bio,
            'profile_url': url
        }
    else:
        return {'platform': 'Instagram', 'error': 'Profile not found or inaccessible'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    platforms = request.form.getlist('platform')  # List of selected platforms

    # If 'ALL' is selected, include all platforms
    if 'all' in platforms:
        platforms = ['twitter', 'google', 'instagram']

    results = {}

    # Use ThreadPoolExecutor to run searches concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        # Add search tasks for each selected platform
        if 'twitter' in platforms:
            futures.append(executor.submit(search_twitter, username))
        if 'google' in platforms:
            futures.append(executor.submit(search_google, username))
        if 'instagram' in platforms:
            futures.append(executor.submit(search_instagram, username))

        # Collect results from all futures
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            platform = result['platform']
            results[platform] = result

    return render_template('result.html', username=username, results=results)

if __name__ == '__main__':
    app.run(debug=True)

