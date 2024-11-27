from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Define a constant for the expected API key
EXPECTED_API_KEY = "apikey"  # Replace with your actual key if it's different

@app.route('/', methods=['GET'])
def fetch_data():
    # Check for the apikey in the query parameters
    apikey = request.args.get("apikey")
    print(apikey)
    if apikey != EXPECTED_API_KEY:
        print(apikey)
        return jsonify({"error": "Invalid or missing API key"}), 403

    # Proceed to fetch data from the external URL if the key is valid
    try:
        response = requests.get("http://localhost:8000/hello/", params={"apikey": EXPECTED_API_KEY})
        response.raise_for_status()  # Check for HTTP request errors

        data = json.loads(response.text)  # Parse the data as JSON
        country = "India"  # Specify the country for filtering

        # Filter movies by the specified country, ensuring 'country' is a string
        movies = [movie for movie in data if isinstance(movie.get("country"), str) and country in movie["country"]]

    except requests.RequestException as e:
        # In case of an error, return an error message in JSON format
        return jsonify({"error": str(e)}), 500

    # Return the filtered movies as a JSON response
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
