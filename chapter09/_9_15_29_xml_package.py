# `xml.etree` is a subpackage.
from xml.etree.ElementTree import ElementTree

# Example: 
#   To extract specific elements from an XML.
doc = ElementTree(file="recipe.xml")
title_elt = doc.find("title")

if title_elt is not None:
    print(title_elt.text)

# Alternative (just get element text).
print(doc.findtext("description"))

# Iterate over multiple elements.
for item in doc.findall("ingredients/item"):
    num = item.get("num")
    units = item.get("units", "")
    text = (item.text or "").strip()
    print(f"{num}, {units}, {text}")
