import requests
from bs4 import BeautifulSoup
import json

url = 'https://leetcode.com/studyplan/top-interview-150/'
response = requests.get(url)

# 응답이 HTML인 경우 BeautifulSoup으로 파싱
soup = BeautifulSoup(response.text, 'html.parser')

script_tag = soup.find('script', {'id': '__NEXT_DATA__', 'type': 'application/json'})

if script_tag:
    data = json.loads(script_tag.string)

    try:
        category = data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['studyPlanV2Detail']['planSubGroups']
        for c in category:
            with open('top_interview_150.md', 'a', encoding='utf-8') as f:
                f.write(f"""< {c['name']} >\n""")
                for q in c['questions']:
                    if q['difficulty'] == 'EASY':
                        f.write(f" - [ ] {q['id']}. {q['title']} 🟡\n")
                    elif q['difficulty'] == 'MEDIUM':
                        f.write(f" - [ ] {q['id']}. {q['title']} 🟠\n")
                    elif q['difficulty'] == 'HARD':
                        f.write(f" - [ ] {q['id']}. {q['title']} 🔴\n")
                f.close()
                    

    except KeyError as e:
        print(f"KeyError: {e}")


