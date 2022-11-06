import json, os
from menu import menu

cName = "config.json" # Configuration file name

def text(*text: str):
    # Shows a text on the question
    print(*text)

def label(question: str, *args):
    return input(question + "\n")

def choice(question: str, *options):
    r = menu(question, *options)
    return options[r - 1]

cvTable = {
    "text": text,
    "choice": choice,
    "label": label
}

def run(form: dict, length: int = 40):
    responses = []
    for i, k in enumerate(form["func"]):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Question {i + 1}")
        print("=" * length)

        responses.append(cvTable[k](*form["args"][i]))
        print("=" * length)

        input("Press Enter to go to the next question...")

    return responses

def main():
    if os.path.exists(cName):
        # load file
        with open(cName, "r") as f:
            c = json.loads(f.read())

        r = run(c)
        print(r)

    else:
        # create file
        with open(cName, "w") as f:
            f.write(json.dumps({}))

        print("file created")

if __name__ == "__main__":
    main()