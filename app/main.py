import json
import sys

def add_note(text):
    with open("data/notes.json", "r", encoding="utf-8") as f:
        notes = json.load(f)

        notes.append({"text": text})

        with open("data/notes.json", "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)

def main():

    with open("data/notes.json", "r", encoding="utf-8") as f:
        notes = json.load(f)
    
    text = "".join(sys.argv[1:])
    
    if text == "list":
        for i, note in enumerate(notes,1):
            print(f"{i}. {note.get('text', '')}")
            
    else:
        add_note(text)

if __name__ == "__main__":
    main()
