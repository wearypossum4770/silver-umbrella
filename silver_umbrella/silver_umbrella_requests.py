import asyncio
import json

import aiohttp


def json_reader(request_content):
    return json.loads(request_content)


request_object = {}
base_url = "http://127.0.0.1:8000"
reqs = [
    {
        "url": f"{base_url}/register/",
    },
]
secondary = []


async def main():
    jar = aiohttp.CookieJar(unsafe=True)
    posts = [
        "/api/announcements/",
    ]
    urls = [
        "/",
        "/about/",
        "/register/",
        "/password-reset/",
        "/appointments/",
        "/appointments/1/",
    ]
    async with aiohttp.ClientSession(cookies=jar) as session:
        for request in reqs:
            async with session.get(**request) as primaryPost:
                request_object[request.get("url")] = primaryPost.status
        for url in urls:
            async with session.get(f"{base_url}{url}") as useFetch:
                request_object[url] = useFetch.status
        for url in posts:
            async with session.get(f"{base_url}{url}") as getJSON:
                json_body = await getJSON.json()
                request_object[url] = json_body
        # async with session.get(
        #     "https://silver-umbrella-2019.herokuapp.com/"
        # ) as herokuapp:
        #     request_object["herokuapp"] = herokuapp.headers


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


def requests():
    request_object.update(secondary=secondary)
    return request_object


# print(requests())
