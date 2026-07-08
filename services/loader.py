import json
import os

def load_stories_from_file(filepath="data/stories.json"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Fajl {filepath} ne postoji.")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_story_by_index(index=0, filepath="data/stories.json"):
    stories = load_stories_from_file(filepath)
    if index >= len(stories):
        raise IndexError("Ne postoji story sa tim indeksom.")
    return stories[index]


def get_manual_story():
    print("Unesi user story (Enter dva puta da završiš unos):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)