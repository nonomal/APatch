import json
import os
import sys
import urllib.parse


url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}'
url += f'/sendMediaGroup?chat_id={urllib.parse.quote(sys.argv[1])}&media='

# https://core.telegram.org/bots/api#markdownv2-style
msg = os.environ["COMMIT_MESSAGE"]
for c in ['\\', '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']:
    msg = msg.replace(c, f'\\{c}')
commit_url = os.environ["COMMIT_URL"]
commit_id = os.environ["COMMIT_ID"][:7]

caption = f"[{commit_id}]({commit_url})\n{msg}"[:1024]

data = json.dumps([
    {"type": "document", "media": "attach://Release","caption": caption,"parse_mode":"MarkdownV2"}
    ])

url += urllib.parse.quote(data)
print(url)