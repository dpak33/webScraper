import requests
from bs4 import BeautifulSoup
import json
import time


def scrape_jobs(query, location=None, max_pages=5):
    base_url = f"https://remoteok.com/remote-{query}-jobs"
    if location:
        base_url += f"?location={location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    jobs_list = []
    for page in range(1, max_pages + 1):
        url = f"{base_url}&page={page}"

        max_retries = 5
        delay = 2  # Initial delay in seconds

        for attempt in range(max_retries):
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                break
            elif response.status_code == 429:
                print(f"Rate limited. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print(f"Failed to retrieve jobs: {response.status_code}")
                return []

        if response.status_code != 200:
            print(f"Failed to retrieve jobs after {max_retries} attempts: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"HTML fetched and parsed successfully for page {page}.")

        for job_card in soup.find_all('tr', class_='job'):
            title = job_card.find('h2', itemprop='title').text.strip()
            company = job_card.find('h3', itemprop='name').text.strip()
            location = job_card.find_all('div', class_='location')[0].text.strip() if job_card.find_all('div',
                                                                                                        class_='location') else "Remote"

            # Extract the job summary from the JSON data embedded in the <script> tag
            script_tag = job_card.find('script', type='application/ld+json')
            if script_tag:
                job_data = json.loads(script_tag.string)
                summary = job_data.get('description', 'No description available')
                summary = BeautifulSoup(summary, 'html.parser').text.strip()  # Clean HTML tags from the summary
                salary_min = job_data.get('baseSalary', {}).get('value', {}).get('minValue', 'N/A')
                salary_max = job_data.get('baseSalary', {}).get('value', {}).get('maxValue', 'N/A')
                salary = f"${salary_min} - ${salary_max}" if salary_min != 'N/A' and salary_max != 'N/A' else "N/A"
            else:
                summary = "No description available"
                salary = "N/A"

            jobs_list.append({
                'title': title,
                'company': company,
                'location': location,
                'summary': summary,
                'salary': salary
            })

        print(f"Jobs found on page {page}: {len(jobs_list)}")

    print(f"Total jobs found: {len(jobs_list)}")
    return jobs_list