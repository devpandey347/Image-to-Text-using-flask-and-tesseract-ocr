"""
Tool developed by: www.github.com/nitiksh

You are permitted to use this tool in both development and production environments **only** if you have obtained it through legal and authorized means.  
If you have legally purchased or received access to this tool, feel free to use it without any restrictions.

However, if you are using this tool without proper authorization or through illegal means, you are strictly **not allowed** to use it under any circumstances.
"""

import os
import base64
import requests
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from PIL import Image
import pytesseract
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

UPLOAD_FOLDER = "images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve the homepage
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract_text", methods=["POST"])
def extract_text():
    image = None
    image_path = None

    # Handle Image Upload
    if "image" in request.files:
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400
        
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)
        image = Image.open(image_path)

    # Handle Image URL
    elif "image_url" in request.form:
        image_url = request.form["image_url"]
        if image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                image_path = os.path.join(UPLOAD_FOLDER, "downloaded_image.png")
                image.save(image_path)
            except Exception as e:
                return jsonify({"error": f"Invalid image URL: {str(e)}"}), 400

    if image is None:
        return jsonify({"error": "No image provided"}), 400

    # Get selected language
    language = request.form.get("language", "eng")

    try:
        # Extract text using Tesseract
        extracted_text = pytesseract.image_to_string(image, lang=language)

        # Convert image to base64 for preview
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return jsonify({"extracted_text": extracted_text, "image_base64": f"data:image/png;base64,{img_str}"})

    except Exception as e:
        return jsonify({"error": f"Text extraction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
