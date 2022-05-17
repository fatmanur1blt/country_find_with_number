import re


def find_country(phone_number):
    pattern = r"(\d{3}-\d{7}"
    x = re.search(pattern, phone_number)

    if x:
        country_code = x.groups()[0]
        print(country_code)
        if country_code.startswith("90"):
            return "Turkey"
        elif country_code.startswith("44"):
            return "England"
        elif country_code.startswith("34"):
            return "Spain"
        elif country_code.startswith("39"):
            return "Italy"
        elif country_code.startswith("81"):
            return "Japan"
        else:
            return "Invalid code"

    else:
        return "incorrect entry"

    phone_number: str = input("Hi, can you entry phone number please:")
    find_country(phone_number)
