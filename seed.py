from django.contrib.auth import authenticate, get_user_model

users = [
    [
        ("username", "testuser2"),
        ("first_name", "John"),
        ("last_name", "Doe"),
        ("email", "john.d.doe@example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "testuser3"),
        ("first_name", "Jane"),
        ("last_name", "Doe"),
        ("email", "jane.d.doe@example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Eddard.Stark"),
        ("first_name", "Eddard"),
        ("last_name", "Stark"),
        ("email", "Eddard.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Robert.Baratheon"),
        ("first_name", "Robert"),
        ("last_name", "Baratheon"),
        ("email", "Robert.Baratheon@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Jaime.Lannister"),
        ("first_name", "Jaime"),
        ("last_name", "Lannister"),
        ("email", "Jaime.Lannister@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Catelyn.Stark"),
        ("first_name", "Catelyn"),
        ("last_name", "Stark"),
        ("email", "Catelyn.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Cersei.Lannister"),
        ("first_name", "Cersei"),
        ("last_name", "Lannister"),
        ("email", "Cersei.Lannister@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Daenerys.Targaryen"),
        ("first_name", "Daenerys"),
        ("last_name", "Targaryen"),
        ("email", "Daenerys.Targaryen@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Jorah.Mormont"),
        ("first_name", "Jorah"),
        ("last_name", "Mormont"),
        ("email", "Jorah.Mormont@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Viserys.Targaryen"),
        ("first_name", "Viserys"),
        ("last_name", "Targaryen"),
        ("email", "Viserys.Targaryen@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Jon.Snow"),
        ("first_name", "Jon"),
        ("last_name", "Snow"),
        ("email", "Jon.Snow@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Robb.Stark"),
        ("first_name", "Robb"),
        ("last_name", "Stark"),
        ("email", "Robb.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Sansa.Stark"),
        ("first_name", "Sansa"),
        ("last_name", "Stark"),
        ("email", "Sansa.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Arya.Stark"),
        ("first_name", "Arya"),
        ("last_name", "Stark"),
        ("email", "Arya.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Theon.Greyjoy"),
        ("first_name", "Theon"),
        ("last_name", "Greyjoy"),
        ("email", "Theon.Greyjoy@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Brandon.Stark"),
        ("first_name", "Brandon"),
        ("last_name", "Stark"),
        ("email", "Brandon.Stark@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Joffrey.Baratheon"),
        ("first_name", "Joffrey"),
        ("last_name", "Baratheon"),
        ("email", "Joffrey.Baratheon@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Sandor.Clegane"),
        ("first_name", "Sandor"),
        ("last_name", "Clegane"),
        ("email", "Sandor.Clegane@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Tyrion.Lannister"),
        ("first_name", "Tyrion"),
        ("last_name", "Lannister"),
        ("email", "Tyrion.Lannister@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Petyr.Baelish"),
        ("first_name", "Petyr"),
        ("last_name", "Baelish"),
        ("email", "Petyr.Baelish@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Davos.Seaworth"),
        ("first_name", "Davos"),
        ("last_name", "Seaworth"),
        ("email", "Davos.Seaworth@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Samwell.Tarly"),
        ("first_name", "Samwell"),
        ("last_name", "Tarly"),
        ("email", "Samwell.Tarly@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Stannis.Baratheon"),
        ("first_name", "Stannis"),
        ("last_name", "Baratheon"),
        ("email", "Stannis.Baratheon@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Jeor.Mormont"),
        ("first_name", "Jeor"),
        ("last_name", "Mormont"),
        ("email", "Jeor.Mormont@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Margaery.Tyrell"),
        ("first_name", "Margaery"),
        ("last_name", "Tyrell"),
        ("email", "Margaery.Tyrell@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Tywin.Lannister"),
        ("first_name", "Tywin"),
        ("last_name", "Lannister"),
        ("email", "Tywin.Lannister@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Talisa.Maegyr"),
        ("first_name", "Talisa"),
        ("last_name", "Maegyr"),
        ("email", "Talisa.Maegyr@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Tormund.Giantsbane"),
        ("first_name", "Tormund"),
        ("last_name", "Giantsbane"),
        ("email", "Tormund.Giantsbane@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Brienne.DeTarth"),
        ("first_name", "Brienne"),
        ("last_name", "DeTarth"),
        ("email", "Brienne.DeTarth@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Ramsay.Bolton"),
        ("first_name", "Ramsay"),
        ("last_name", "Bolton"),
        ("email", "Ramsay.Bolton@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Daario.Naharis"),
        ("first_name", "Daario"),
        ("last_name", "Naharis"),
        ("email", "Daario.Naharis@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Ellaria.Sand"),
        ("first_name", "Ellaria"),
        ("last_name", "Sand"),
        ("email", "Ellaria.Sand@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Tommen.Baratheon"),
        ("first_name", "Tommen"),
        ("last_name", "Baratheon"),
        ("email", "Tommen.Baratheon@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Jaqen.Hghar"),
        ("first_name", "Jaqen"),
        ("last_name", "Hghar"),
        ("email", "Jaqen.Hghar@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Roose.Bolton"),
        ("first_name", "Roose"),
        ("last_name", "Bolton"),
        ("email", "Roose.Bolton@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "Grey.Worm"),
        ("first_name", "Grey"),
        ("last_name", "Worm"),
        ("email", "Grey.Worm@gameofthrones.example.com"),
        ("is_staff", 0),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "aadmin"),
        ("first_name", ""),
        ("last_name", ""),
        ("email", ""),
        ("is_staff", 1),
        (
            "is_active",
            1,
        ),
    ],
    [
        ("username", "admin2"),
        ("first_name", ""),
        ("last_name", ""),
        ("email", ""),
        ("is_staff", 1),
        (
            "is_active",
            1,
        ),
    ],
]

users = [dict(user) for user in users]
previous = list(set([user.username for user in get_user_model().objects.all()]))
additional = [user["email"].split("@")[0].lower() for user in users]
output = [username for username in additional if username not in previous]
print(output)
