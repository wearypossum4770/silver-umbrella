from re import findall
months = dict(
    [
          (1, "A"),
  (2, "B"),
  (3, "C"),
  (4, "D"),
  (5, "E"),
  (6, "H"),
  (7, "L"),
  (8, "M"),
  (9, "P"),
  (10, "R"),
  (11, "S"),
  (12, "T"),
    ]
)
def fiscal_code(person):
    name, surname, gender, dob = person.items()
    consonants,vowels  = (r'[^aeiou]+',r"[aeiou]",)
    third = dob[1][::-3]
    return third
    return "".join(findall(consonants,person['name']))
    ...


print(fiscal_code({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961" }))