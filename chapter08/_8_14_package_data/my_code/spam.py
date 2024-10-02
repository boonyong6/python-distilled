import pkgutil
import json

def func():
    if __package__ is None:
        print(f'"{__name__}" module is not in a package.')
        return
    
    raw_data = pkgutil.get_data(__package__, "resources/data.json")

    if raw_data is None:
        print(f"No data.")
        return
    
    text_data = raw_data.decode("utf-8")
    data = json.loads(text_data)
    print(data)
