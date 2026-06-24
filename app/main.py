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
        filtered_notes = [note for note in notes if note.get('text', '').strip()]
        for i, note in enumerate(filtered_notes, 1):
            print(f"{i}. {note.get('text', '')}")
    elif text == "clear":
        notes = []
        with open("data/notes.json", "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
    elif text.strip():
        add_note(text)

if __name__ == "__main__":
    main()
