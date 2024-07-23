import json
import re
import nltk
from nltk.corpus import wordnet
from random_responses import random_string

# Ensure you have the NLTK data downloaded
nltk.download('wordnet')


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


response_data = load_json("bot.json")


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    exact_matches = []
    best_response = None
    highest_score = 0

    for response in response_data:
        response_score = 0
        required_words = response["required_words"]
        user_input = response["user_input"]

        # Exact match score
        if any(word in user_input for word in split_message):
            exact_matches.append(response)

        # Check for required words
        if required_words:
            required_words_set = set(required_words)
            split_message_set = set(split_message)
            if required_words_set.issubset(split_message_set):
                # Score based on required words match
                response_score = len(required_words)

                # Score based on user input match
                user_input_set = set(user_input)
                response_score += len(user_input_set.intersection(split_message_set))

                if response_score > highest_score:
                    highest_score = response_score
                    best_response = response

    # Prefer exact matches if available
    if exact_matches:
        best_response = max(exact_matches, key=lambda x: len(set(x["user_input"]).intersection(split_message)))

    # Return the best response or a random response
    if best_response:
        return best_response["bot_response"]

    # Handle empty input
    if input_string.strip() == "":
        return "Please type something so we can chat :("

    return random_string()


while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))
