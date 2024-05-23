import os
from googleapiclient.discovery import build
reacted1 = "'AIzaSyA47JPNTVMFf2nIoP2IYD0svgV0AJF7_sA'"
reacted = "d3998bd1571bb41d9"

API_KEY = reacted1
CSE_ID = reacted

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
query = "memory leaks"
results = google_search(query, API_KEY, CSE_ID)

for result in results:
    print(result['title'])
    print(result['snippet'])
    print(result['link'])
    print()
