#!/usr/bin/env python3

import json, os

levels_folder = '_levels/'

for filename in os.listdir(levels_folder):
    file_path = os.path.join(levels_folder, filename)
    if os.path.isfile(file_path) and filename != 'readme.md':
        os.unlink(file_path)

with open("_data/levels.json") as levels_json:
    data = json.load(levels_json)

for record in data["records"]:
    id = record["id"]
    name = record["fields"]["name"]

    front_matter = """---
    layout: level
    level_id: {id}
    title: {name}
    ---
    """.format(id=id, name=name)

    front_matter = "\n".join([s.strip() for s in front_matter.splitlines()])

    level_file = open(levels_folder + id + ".md", "w+")
    level_file.write(front_matter)
    level_file.close()
    print("Creating level/" + id + " (" + name + ")")
