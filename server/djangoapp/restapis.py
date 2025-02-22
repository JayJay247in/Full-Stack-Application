# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    """
    Makes a GET request to the specified endpoint of the backend API.

    Args:
        endpoint (str): The API endpoint to request (e.g., '/reviews').
        **kwargs: Keyword arguments that will be converted to URL parameters.

    Returns:
        dict: The JSON response from the API, or None if an error occurred.
    """
    backend_url = settings.BACKEND_URL  # Get backend URL from settings
    if not backend_url:
        print("Error: BACKEND_URL is not set in settings.py")
        return None

    params = ""
    if kwargs:
        params = '&'.join([f"{key}={value}" for key, value in kwargs.items()])  # More efficient

    request_url = f"{backend_url}{endpoint}?{params}"  # Use f-strings
    print(f"GET from {request_url}")  # Use f-strings

    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")  # Include the exception in the message
        return None
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        return None

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
