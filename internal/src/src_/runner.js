import {user} from './User.js'

let obj =  {
    "password": "pbkdf2_sha256$260000$MZSO5Iey4KG5EZLcNvyNCG$OvuSzxovqM1JznX7ivSJG3Zw2/o8HD6DNI+zCrLroHQ=",
    "username": "tommen.baratheon",
    "first_name": "tommen",
    "email": "tommen.baratheon@game.of.thrones.com",
    "date_joined": "2021-06-01T22:04:12.440Z",
    "last_name": "baratheon",
    "is_patient": false,
    "is_clinic_staff": false,
}

let tommen = user(obj)
tommen.clean()
console.log(tommen)