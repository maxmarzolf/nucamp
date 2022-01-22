# In [1]: import requests
#
# In [2]: api_key = 'gKp3AwyDhmmVK4lQsjwmdSSvQBuDIV6Cmp1EU76w'
#
# In [3]: headers = {'X-API-Key': api_key}
#
# In [4]: url = 'https://api.propublica.org/congress/v1/members/senate/PA/current.json'
#
# In [5]: response = requests.get(url, headers=headers)
#
# In [6]: response.json()
# Out[6]:
# {'status': 'OK',
#  'copyright': 'Copyright (c) 2022 Pro Publica Inc. All Rights Reserved.',
#  'results': [{'id': 'C001070',
#               'name': 'Bob Casey',
#               'first_name': 'Bob',
#               'middle_name': None,
#               'last_name': 'Casey',
#               'suffix': None,
#               'role': 'Senator, 1st Class',
#               'gender': 'M',
#               'party': 'D',
#               'times_topics_url': 'http://topics.nytimes.com/top/reference/timestopics/people/c/robert_p_jr_casey/index.html',
#               'twitter_id': 'SenBobCasey',
#               'facebook_account': 'SenatorBobCasey',
#               'youtube_id': 'SenatorBobCasey',
#               'seniority': '15',
#               'next_election': '2024',
#               'api_uri': 'https://api.propublica.org/congress/v1/members/C001070.json'},
#              {'id': 'T000461',
#               'name': 'Patrick J. Toomey',
#               'first_name': 'Patrick',
#               'middle_name': 'J.',
#               'last_name': 'Toomey',
#               'suffix': None,
#               'role': 'Senator, 3rd Class',
#               'gender': 'M',
#               'party': 'R',
#               'times_topics_url': '',
#               'twitter_id': 'SenToomey',
#               'facebook_account': 'senatortoomey',
#               'youtube_id': 'sentoomey',
#               'seniority': '11',
#               'next_election': '2022',
#               'api_uri': 'https://api.propublica.org/congress/v1/members/T000461.json'}]}




# response = requests.get('http://127.0.0.1:5000/netflix_originals/highest_rated')
# response.text
# response.json()
# x = response.json()
# x[0]['premiere']