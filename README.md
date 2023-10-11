# ZoteroToKumu
A simple program that extracts document information from a Zotero library and generates a Kumu import file in JSON format.

Installation:<br />
Clone/copy the github code to a folder<br />
Open a console and navigate to the folder<br />
(Optional) If you use virtual environments, create one and activate it.<br />
Run:  pip (or pip3) install -r requirements.txt<br />
<br />
Create file called .env with information from your Zotero account:<br />
LIBRARY_TYPE=group    (for accessing a group library)<br />
or LIBRARY_TYPE=user    (for accessing a user library)<br />

LIBRARY_ID: Your personal library ID is [available here](https://www.zotero.org/settings/keys), in the section "Your userID for use in API calls"<br />
For group libraries, the ID can be found by opening the group’s page: https://www.zotero.org/groups/groupname, and hovering over the group settings link. The ID is the integer after /groups/<br />

ZOTERO_API_KEY=[create your api key here](https://www.zotero.org/settings/keys)<br />
Save the .env file<br />

Here's my .env file (for reference)<br />
![image](https://github.com/zenskunkworx/ZoteroToKumu/assets/145480414/98cccea0-5570-4cad-bdd2-4c2a5b9ab06b)<br />

Run: python app.py    (or python3 app.py)<br />

Here's a sample View setup in Kumu:<br />
![image](https://github.com/zenskunkworx/ZoteroToKumu/assets/145480414/abac7ec5-03a3-4be7-9ee5-d0babe0b1f4d)<br />




