# Project-22

# Mail Merge Project

This Python project automatically generates personalized invitation letters using a template and a list of names.

## How It Works

- Reads a template letter from:
  ```bash
  Input/Letters/starting_letter.txt
  ```

- Reads a list of invited names from:
  ```bash
  Input/Names/invited_names.txt
  ```

- Replaces the placeholder:
  ```bash
  [name]
  ```
  with each person's name.

- Creates a personalized text file for each person inside:
  ```bash
  Output/ReadyToSend/
  ```

---

## Project Structure

```bash
Project/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│
└── main.py
```

---

## Example

### Template Letter

```text
Dear [name],

You are invited to my birthday party.

Hope to see you there!
```

### invited_names.txt

```text
John
Sarah
Michael
```

### Generated Files

```bash
Output/ReadyToSend/John.txt
Output/ReadyToSend/Sarah.txt
Output/ReadyToSend/Michael.txt
```

---

## Technologies Used

- Python 3
- File Handling
- String Replacement

---

## Concepts Practiced

- Reading files
- Writing files
- Using loops
- String manipulation
- Working with directories

---

## How to Run

1. Make sure Python 3 is installed.
2. Add names to:
   ```bash
   invited_names.txt
   ```
3. Edit the template letter if desired.
4. Run the script:

```bash
python main.py
```

---

## Author

Moonzy Fernema
