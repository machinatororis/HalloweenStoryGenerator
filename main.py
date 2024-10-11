import json
import random


def load_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


data = load_data('stories_data.json')
places = data['places']
creatures = data['creatures']
actions = data['actions']
subjects = data['subjects']


def story_generator():
    place = random.choice(places)
    creature = random.choice(creatures)
    action = random.choice(actions)
    subject = random.choice(subjects)

    story = f"One night, in the {place}, a {creature} {action} a {subject}."

    return story


for _ in range(5):
    print(story_generator())
