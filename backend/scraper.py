import requests
from bs4 import BeautifulSoup

def find_auth_component(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Failed to fetch URL: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Look for forms that contain password input
    forms = soup.find_all("form")
    for form in forms:
        password_input = form.find("input", {"type": "password"})
        if password_input:
            return {
                "found": True,
                "html_snippet": str(form)
            }

    # Fallback: search for password input anywhere
    password_input = soup.find("input", {"type": "password"})
    if password_input:
        parent = password_input.find_parent()
        return {
            "found": True,
            "html_snippet": str(parent)
        }

    return {
        "found": False,
        "message": "No authentication component found."
    }
