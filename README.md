# CloudConnect — Python Mobile Cloud App

A mobile-friendly Streamlit learning project demonstrating REST API requests, JSON parsing, Firebase Authentication and Cloud Firestore.

## Features
- REST API GET request to JSONPlaceholder
- HTTP status/error handling and JSON response parsing
- Firebase email/password registration and login
- Cloud Firestore task creation and reading
- User-owned task data model
- Firebase setup guide and suggested Firestore security rules

## Requirements
- Python 3.9+
- Firebase project
- Email/Password sign-in enabled in Firebase Authentication
- Cloud Firestore database created

## Run on Windows
1. Extract this ZIP.
2. Open the extracted `Mobile_Cloud_Firebase_App` folder.
3. Create a folder named `.streamlit`.
4. Inside it, create `secrets.toml` using the template in `config/secrets.example.toml`.
5. Replace the placeholders with your Firebase Web API key and Project ID.
6. Open CMD in the project folder and run:

   ```bash
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

7. Open the local URL shown in the terminal.

## Firebase setup
1. Open https://console.firebase.google.com/ and create a project.
2. In Project settings, register a Web app and copy its Web API key.
3. In Authentication > Sign-in method, enable Email/Password.
4. Create a Cloud Firestore database.
5. Open Firestore > Rules and publish the recommended rules in `docs/firestore.rules`.
6. Put the Web API key and project ID in `.streamlit/secrets.toml`.

## Security notes
- Do not commit `.streamlit/secrets.toml` to GitHub.
- Firebase Web API keys identify a Firebase project; access must be protected by Firebase Authentication and Firestore Security Rules.
- Do not store passwords in the app or database.
- The demo stores the Firebase ID token in Streamlit session state. For production, implement token refresh, logout/revocation strategy, HTTPS hosting and stronger session controls.
- Review and test Firestore rules before using real user data.

## Project structure
```text
Mobile_Cloud_Firebase_App/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── config/
│   └── secrets.example.toml
└── docs/
    ├── data_model.md
    ├── firestore.rules
    └── test_plan.md
```

## Important
This is a Python web app with a mobile-friendly interface, not a native Android APK or iOS IPA. Firebase credentials are not included; you must add your own project configuration.
