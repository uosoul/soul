print("Hello python")

import requests

resp = requests.get(url="https://www.baidu.com").content.decode()
