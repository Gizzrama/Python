country_code = {
    "India": 91,
    "Australia": 61,
    "United Kingdom": 44,
    "America": 1
}

choice = input("Enter the country name: ").strip()

print(country_code)

try:
    print(country_code[choice])

except:
    print("Country not in dictionary")







