# AI Engineer Technical Assessment  
## Authentication Component Detector

### Overview
This project is a lightweight web application that dynamically scrapes and analyzes
website HTML to detect authentication components such as login forms.

The application accepts any website URL as input, fetches its markup, and attempts
to locate username/password authentication sections using DOM analysis heuristics.
If found, it returns the relevant HTML snippet; otherwise, it reports that no
authentication component was detected.

---

## Features
- Scrapes live website HTML content
- Detects authentication/login forms using HTML heuristics
- Dynamic URL input support
- Returns raw HTML snippet of the detected authentication component
- Interactive API testing via FastAPI Swagger UI
- Fully runnable locally

---

## Tech Stack
- **Backend:** Python, FastAPI
- **Web Scraping:** Requests, BeautifulSoup
- **Frontend (Optional UI):** HTML, JavaScript
- **API Documentation:** FastAPI Swagger UI

---

## Project Structure

auth-component-detector/
│
├── backend/
│ ├── main.py # FastAPI application
│ └── scraper.py # Web scraping & authentication detection logic
│
├── frontend/
│ └── index.html # Simple UI for dynamic URL input
│
├── requirements.txt
└── README.md

---

## Setup Instructions (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/JoshnaMedisetty/auth-component-detector.git
cd auth-component-detector 

```

### 2. Create and Activate Virtual Environment
macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Backend Server
```bash
cd backend
uvicorn main:app --reload
```
The backend will start at: http://127.0.0.1:8000

## How to Use the Application

### Option 1: Using FastAPI Interactive Docs (Recommended)

* Open the following URL in your browser: http://127.0.0.1:8000/docs
* Locate the GET /analyze endpoint.
* Click the "Try it out" button.
* Enter any website URL in the url field.
* Click Execute.
* View the JSON response containing:
- Whether an authentication component was found
- The extracted HTML snippet (if available)

This interface allows you to easily test multiple websites dynamically.

### Option 2: Using the Simple Frontend UI

* Open the file: frontend/index.html
* Enter a website URL in the input field.
* Click Analyze.
* The detected authentication component (or result message) will be displayed.

## Example Test URLs

The application has been tested with the following types of websites:

* https://github.com/login (SaaS)
* https://www.facebook.com/login (Social Media)
* https://www.amazon.com (E-commerce)
* https://medium.com (Blog)
* https://www.reddit.com (Community Platform)

## Detection Logic

The detection algorithm uses the following heuristics:

* Searches for <form> elements containing <input type="password">
* Falls back to locating standalone password inputs if no form is found
* Extracts and returns the closest parent HTML block as the authentication component

## Notes

* Some websites may block scraping or require JavaScript rendering.
* The solution focuses on static HTML analysis, which covers a majority of login pages.
* The architecture is modular and easy to extend (e.g., headless browsers, ML-based detection).

## Author
Joshna Medisetty
joshnamedisetty0107@gmail.com
medisetty0107@gmail.com 
