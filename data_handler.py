import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_best_answer(question, datasets):
    keywords = question.lower().split()
    best_answer = None

    for dataset in datasets:
        for entry in dataset:
            if any(keyword in entry['question'].lower() for keyword in keywords):
                # If we find a match, we return the first found answer
                best_answer = entry['answer']
                return best_answer

    return None
