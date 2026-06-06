import json
import os

COURSE_DIR = "generated_courses/text"

os.makedirs(COURSE_DIR, exist_ok=True)

def save_course(topic, content):
    filename = f"{COURSE_DIR}/{topic}.json"

    data = {
        "topic": topic,
        "content": content
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_course(topic):
    filename = f"{COURSE_DIR}/{topic}.json"

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def list_courses():
    files = []

    for file in os.listdir(COURSE_DIR):
        if file.endswith(".json"):
            files.append(file.replace(".json", ""))

    return sorted(files)