import datetime
import json
import requests
import urllib.parse
from bsqt.utils.beatsaver.enums import BeatSaverLatestSort

base_url: str = "https://api.beatsaver.com"


def get_map_by_id(id):
    try:
        req = requests.get(f"{base_url}/maps/id/{id}")
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    return map_info


def get_maps_by_ids(ids):
    maps = []
    s = ","
    try:
        req = requests.get(f"{base_url}/maps/ids/{s.join(str(n) for n in ids)}")
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    for k, v in map_info.items():
        if k == "error":
            continue
        maps.append(v)
    return maps


def get_map_by_hash(hashes):
    maps = []
    s = ","
    try:
        req = requests.get(f"{base_url}/maps/hash/{s.join(str(n) for n in hashes)}")
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    for k, v in map_info.items():
        if k == "error":
            continue
        maps.append(v)
    return maps


def get_maps_by_uploader(id, page=0):
    try:
        req = requests.get(f"{base_url}/maps/uploader/{id}/{page}")
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    try:
        maps = map_info["docs"]
    except KeyError:
        print("Invalid mapper id")
        return None
    if len(maps) == 0:
        return None
    return maps


def get_maps_by_collab(id, before=None, page_size=20):
    try:
        url = f"{base_url}/maps/collaborations/{id}?pageSize={page_size}"
        if before is not None:
            url += f"&before={before}"
        req = requests.get(url)
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    try:
        maps = map_info["docs"]
    except KeyError:
        print("Invalid mapper id")
        return None
    if len(maps) == 0:
        return None
    return maps


def get_latest_maps(
    after="1970-01-01T00:00:00+00:00",
    before=None,
    automapper=False,
    page_size=20,
    sort=1,
    verified=None,  # False: no verified, True: All verified, None: both
):
    if before is None:
        now = datetime.datetime.now(datetime.timezone.utc)
        before = now.strftime("%Y-%m-%dT%H:%M:%S") + "+00:00"
    try:
        url = f"{base_url}/maps/latest"
        url += f"?after={urllib.parse.quote(after)}"
        if automapper is True:
            url += "&automapper=true"
        else:
            url += "&automapper=false"
        if before is not None:
            url += urllib.parse.quote(f"&before={urllib.parse.quote(before)}")
        url += f"&pageSize={page_size}"
        url += f"&sort={BeatSaverLatestSort(sort).name}"
        if verified is not None:
            if verified is True:
                url += "&verified=true"
            else:
                url += "&verified=false"
        print(url)
        req = requests.get(url)
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    print(req)
    map_info = json.loads(req.content)
    return map_info


def get_maps_by_plays(page):
    try:
        req = requests.get(f"{base_url}/maps/plays/{page}")
    except ConnectionError:
        print("Beat Saver connection error")
        return None
    map_info = json.loads(req.content)
    return map_info


if __name__ == "__main__":
    """"""
    # print(get_maps_by_ids([1, 2, 3]))
    # print(get_map_by_hash(["fda568fc27c20d21f8dc6f3709b49b5cc96723be"]))
    # print(get_maps_by_uploader(48853))
    # print(get_maps_by_collab(48853))
    # print(get_latest_maps(verified=True))
    # print(get_maps_by_plays(0))
