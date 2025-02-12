import json

# create example dictionary and save as json
dct = {}
dct["name"] = "andy"
dct["major"] = "data analytics"

dct["favorite_song"] = "crazy frog axel f"
dct["favorite_song"] = "i barely knew you"

print(dct)

try:
    file = open("andy_info.json", "w")
    json.dump(dct, file, indent=4)
except:
    print("opening file failed")


with open("andy_info.json") as file:
    dct2 = json.load(file)



