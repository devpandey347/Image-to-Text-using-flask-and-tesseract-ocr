# 🧠 OCR Image Text Extractor (Flask-based Tool)
[![🌐 ntxm.org](https://img.shields.io/badge/Website-ntxm.org-blue?style=flat-square)](https://ntxm.org)
[![🏢 GitHub Org](https://img.shields.io/badge/GitHub-ntxmofficial-blue?style=flat-square)](https://github.com/ntxmofficial)
[![👨‍💻 Author](https://img.shields.io/badge/Author-nitiksh-green?style=flat-square)](https://github.com/nitiksh) <br/>

This is a powerful image-to-text extraction tool built using Flask and Tesseract OCR. Whether you're processing receipts, scanned documents, handwritten notes, or screenshots — this tool extracts text with high accuracy in just a few clicks.

> ✅ Created by [Nitiksh](https://github.com/nitiksh)  

---

## 🚀 Features

- 🔍 Extract text from any image (JPEG, PNG, etc.)
- 🧠 Built using Python Flask + Tesseract OCR
- ⚡ Fast image upload and processing
- 🖼️ Save uploaded images to local server
- 🌐 CORS Enabled (ready for frontend integration)
- 🎯 Ready for both development and production use

---

## 📦 Installation

> 📝 **Requirements**:
- Python 3.7+
- Tesseract-OCR installed on your machine
- pip (Python package installer)


### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Make Sure Tesseract is Installed  
Download and install from: https://github.com/tesseract-ocr/tesseract  
Then update the path in `app.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. Run the App
```bash
python app.py
```

Visit: `http://localhost:5000`

---

## 🧪 Usage

1. Open the web interface.
2. Upload an image (e.g. screenshot, scanned doc).
3. Click "Extract" to view extracted text.
4. Download or copy the text as needed.

---

## 🙏 Credits

- Python & Flask
- Tesseract OCR (by Google)
- PIL (Python Imaging Library)

---

**Created by:** [ntxm.org](https://ntxm.org) <br/>
**GitHub Organization:** [https://github.com/ntxmofficial](https://github.com/ntxmofficial) <br/>
**Author:** [https://github.com/nitiksh](https://github.com/nitiksh) <br/>
