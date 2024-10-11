import unicodedata

d = {}

key_c = "Jalape\xf1o"       # ñ = \xf1
key_d = "Jalapen\u0303o"    # ñ = n + \u0303

# Fully composed
print(unicodedata.normalize("NFC", key_c).encode("utf-8"))
print(unicodedata.normalize("NFC", key_d).encode("utf-8"))
# Fully decomposed
print(unicodedata.normalize("NFD", key_c).encode("utf-8"))
print(unicodedata.normalize("NFD", key_d).encode("utf-8"))

d[key_c] = "spicy"
d[key_d] = "mild"
print(d)  # {'Jalapeño': 'spicy', 'Jalapeño': 'mild'}

# To get the general character properties. 
#   More info in https://www.unicode.org/reports/tr44/#General_Category_Values
print(unicodedata.category("A"))