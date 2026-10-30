# Pocket Tasks — Mobile To-Do App (Python)

A responsive, browser-based To-Do application built with Python and Streamlit.

## Features
- Mobile-friendly UI with buttons, form inputs, cards and list views
- Multiple screens: Tasks, Add Task and Summary
- Add tasks with category and due date
- Input validation (required title; maximum 80 characters)
- Mark tasks complete/incomplete
- Delete tasks
- Filter tasks by category
- Progress summary

## Run on Windows
1. Download and extract `Mobile_Todo_App.zip`.
2. Open the extracted `Mobile_Todo_App` folder.
3. Click the File Explorer address bar, type `cmd`, and press Enter.
4. Run:

   ```bash
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

5. The app opens in your browser at the local address shown in Command Prompt.

## Project structure
```text
Mobile_Todo_App/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   └── README.txt
└── tests/
    └── test_plan.md
```

## Test checklist
See `tests/test_plan.md` for manual test cases.

## Screenshots
Run the app and capture screenshots of:
- Tasks screen
- Add Task screen
- Summary screen

On Chrome, press `F12` and toggle the device toolbar to preview a phone-sized layout.

## Important
This is a Python web app with a mobile-friendly design. It is not a native Android APK or iOS IPA. Tasks are kept in Streamlit session memory; they are not saved permanently to a database.
