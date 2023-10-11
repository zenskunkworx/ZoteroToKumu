'''Creates a Kumu Import file from a Zotero Library'''
import json
import os
from pyzotero import zotero
from dotenv import load_dotenv
load_dotenv()

library_id: str = os.getenv("LIBRARY_ID")
library_type: str = os.getenv("LIBRARY_TYPE")
api_key: str = os.getenv("ZOTERO_API_KEY")

zot: zotero.Zotero = zotero.Zotero(library_id=library_id,
                                   library_type=library_type,
                                   api_key=api_key)
items: dict = zot.top(limit=5000)
json_data: dict[str,list] = {'elements':[], 'connections':[]}
item_count: int = 1
total_items: int = len(items)

# Iterate across items in the Zotero Library
for item in items:
    # Create variables to store attributes of the item
    label: str = str(item['data']['title'])
    url: str = str(item['data'].get('url', ""))
    href: str = item['links']['self'].get('alternate', "")
    desc: str = str(item['data'].get('abstractNote', ""))
    item_type: str = str(item['data'].get('itemType', ""))
    pdate: str = str(item['data'].get('date', ""))
    publication: str = str(item['data'].get('publicationTitle', ""))

    # Create a kumu node for the item
    json_data['elements'].append({'label':label,
                                  'type':item_type,
                                  'Zotero Link':href,
                                  'Original Link':url,
                                  'Description':desc,
                                  'Publication':publication,
                                  'Date':pdate,
                                  })

    if 'creators' in item['data']:
        # Add authors of the item as Elements and connect them to the item with an Edge
        for creator in item['data']['creators']:
            author_name = creator.get('firstName',"---") + " " + creator.get('lastName',"---")
            json_data['elements'].append({'label':author_name, 'type':'Person'})
            json_data['connections'].append({'from':author_name, 'to':label, 'type':'Author'})

    print(str(item_count) + "/" + str(total_items) + " - ", item['data']['title'])
    item_count += 1

# Write the JSON data to a file
with open('zotero.json', 'w',encoding='utf-8') as outfile:
    json.dump(json_data, outfile, indent=4)
