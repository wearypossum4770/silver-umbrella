import asyncio
import json

# from django.conf import settings
import aiohttp
import requests

request_object = {}

base_url = "http://127.0.0.1:8000"
# def genryusai_shigekuni_yamamoto_data():
#     with open(f"{settings.BASE_DIR}/users/fixtures/new_registrant.json") as _d:
#         __data__ = json.load(_d)
#     return __data__
reqs = [
    {
        # "data": genryusai_shigekuni_yamamoto_data(),
        "url": f"{base_url}/register/",
    },
]
secondary = []
cookies = {
    "csrftoken": "V2XHDDoshpRD05CY0WZXqaAntYjZNGUAmip406tIKhpL2ykNiwsKP27E0Sg4VGz5; expires=Wed, 08 Jun 2022 14:53:53 GMT; Max-Age=31449600; Path=/; SameSite=Lax"
}


async def main():
    jar = aiohttp.CookieJar(unsafe=True)
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
                _cookie = {
                    "csrftoken": primaryPost.headers.get("Set-Cookie").split(
                        "csrftoken="
                    )[-1]
                }
                request.update(cookies=_cookie)
                request_object[request.get("url")] = primaryPost.status

        for url in urls:
            async with session.get(f"{base_url}{url}") as useFetch:
                request_object[url] = useFetch.status


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


def requests():
    request_object.update(secondary=secondary)
    return request_object


print(request_object)
