import os

import requests

from gdrive_to_commons import settings


def upload_files_to_commons(mw_site=None):
    s = requests.session()
    url = settings.WIKI_URL

    params_1 = {"action": "query", "meta": "tokens", "type": "login", "format": "json"}

    r = s.get(url=url, params=params_1)
    data = r.json()

    login_token = data["query"]["tokens"]["logintoken"]

    params_2 = {
        "action": "login",
        "lgname": settings.WIKI_BOT_USERNAME,
        "lgpassword": settings.WIKI_BOT_PASSWORD,
        "format": "json",
        "lgtoken": login_token,
    }

    r = s.post(url, data=params_2)

    params_3 = {"action": "query", "meta": "tokens", "format": "json"}

    r = s.get(url=url, params=params_3)
    data = r.json()

    csrf_token = data["query"]["tokens"]["csrftoken"]

    for file in os.listdir("tmp"):
        params_4 = {
            "action": "upload",
            "filename": file,
            "format": "json",
            "token": csrf_token,
            "ignorewarnings": 1,
        }

        file = os.path.join("tmp", file)
        files = {"file": (file, open(file, "rb"), "multipart/form-data")}
        r = s.post(url, files=files, data=params_4)
        data = r.json()
        print(data)
