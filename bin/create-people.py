#!/usr/bin/env python3

import json, os

team_folder = '_team/'

for filename in os.listdir(team_folder):
    file_path = os.path.join(team_folder, filename)
    if os.path.isfile(file_path) and filename != 'readme.md':
        os.unlink(file_path)

with open("_data/team.json") as team_json:
    try:
        data = json.load(team_json)
    except Exception as e:
        print("*** Failed to load team JSON:")
        print(e)
        print("***File contents:")
        print(team_json.readlines())
        raise

for record in data["records"]:
    id = record["id"]
    name = record["fields"]["name"]

    front_matter = """---
    layout: person
    person_id: {id}
    title: {name}
    ---
    """.format(id=id, name=name)

    front_matter = "\n".join([s.strip() for s in front_matter.splitlines()])

    person_file = open(team_folder + id + ".md", "w+")
    person_file.write(front_matter)
    person_file.close()
    print("Creating team/" + id + " (" + name + ")")






