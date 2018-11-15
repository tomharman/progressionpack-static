#!/usr/bin/env python3

import json, os

goals_folder = '_goals/'

for filename in os.listdir(goals_folder):
    file_path = os.path.join(goals_folder, filename)
    if os.path.isfile(file_path) and filename != 'readme.md':
        os.unlink(file_path)

with open("_data/goals.json") as goals_json:
    data = json.load(goals_json)

for record in data["records"]:
    id = record["id"]
    name = record["fields"]["goal-description"]

    front_matter = """---
    layout: goal
    goal_id: {id}
    title: {name}
    ---
    """.format(id=id, name=name)

    front_matter = "\n".join([s.strip() for s in front_matter.splitlines()])

    level_file = open(goals_folder + id + ".md", "w+")
    level_file.write(front_matter)
    level_file.close()
    print("Creating goal/" + id + " (" + name + ")")
