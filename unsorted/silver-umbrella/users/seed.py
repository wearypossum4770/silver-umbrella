import json

from django.conf import settings

location = f"{settings.BASE_DIR}/manga.json"
episode = {}
episode_list = []

with open(location) as _manga:
    manga = json.load(_manga)
for key, value in manga:
    episode_list.append(
        {
            "model": "blog.blog",
            "pk": key,
            "fields": {
                "owner": "",
                "title": value,
                "content": "",
                "date_expired": "",
                "author": "",
            },
        },
    )
print(manga)
# eposide.update(
#     owner =
# title=
# content=
# date_posted=
# date_modified=
# date_expired=
# author=
# )


unohana = get_user_model().objects.get(username="retsu_unohana")
Blog.objects.create(
    is_public=False,
    owner=unohana,
    publication_type="CONCMNT",
    title="The First Kempachi",
    content="I found... A way to heal myself, so that I could enjoy fighting forever.",
    author=unohana,
)
