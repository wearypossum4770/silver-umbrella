from django.contrib.auth import get_user_model

user = get_user_model().objects.get(username="theon.greyjoy")


def handle_save_address(_user, **kwargs):
    address = _user.profile.addresses.all().filter(
        idempotent_key=kwargs.get("idempotent_key")
    )[0]
    address.address_type = kwargs.get("address_type")
    address.street1 = kwargs.get("street1")
    address.street2 = kwargs.get("street2")
    address.state = kwargs.get("state")
    address.city = kwargs.get("city")
    address.zipcode = kwargs.get("zipcode")
    address.save()


def changeable_address(addresses, idempotent_key=None):
    if idempotent_key:
        address_info = filter(
            lambda addr: addr.idempotent_key == idempotent_key, addresses
        )
    return address_info

    return {
        "idempotent_key": "ckqib0rxk0000hsveixloydmx",
        "zipcode": "92688-2014",
    }


obj = {
    # "idempotent_key":"ckpfzqd7l0000nbve3vq1hfgl",
    "idempotent_key": "ckqib0rxk0000hsveixloydmx",
    "street1": "STE K",
    "street2": "29851 AVENTURA",
    "city": "RANCHO SANTA MARGARITA",
    "state": "CA",
    "zipcode": "92688",
    "address_type": "RESD",
}
# address = handle_save_address()
print(user)
