# 🧠 OCR Image Text Extractor (Flask-based Tool)
[![🌐 ntxm.org](https://img.shields.io/badge/Website-ntxm.org-blue?style=flat-square)](https://ntxm.org)
[![🏢 GitHub Org](https://img.shields.io/badge/GitHub-ntxmofficial-blue?style=flat-square)](https://github.com/ntxmofficial)
[![👨‍💻 Author](https://img.shields.io/badge/Author-nitiksh-green?style=flat-square)](https://github.com/nitiksh)
Preview on Youtube, Click on Image ♨️
[![Watch on YouTube](https://img.youtube.com/vi/33mYqmLr2Ac/0.jpg)](https://www.youtube.com/watch?v=33mYqmLr2Ac)

This is a powerful image-to-text extraction tool built using Flask and Tesseract OCR. Whether you're processing receipts, scanned documents, handwritten notes, or screenshots — this tool extracts text with high accuracy in just a few clicks.

> ✅ Created by [Nitiksh](https://github.com/nitiksh)  
> 🔗 Website: [ntxm.org](https://ntxm.org)

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

## 🛡️ License & Usage Terms

**Tool developed by:** [www.github.com/nitiksh](https://github.com/nitiksh)  
**Website:** [ntxm.org](https://ntxm.org)
**Buy From:** [payhip.com](https://payhip.com/b/ka09N)

- ✅ You are allowed to use this tool for both **development** and **production** if purchased legally from an authorized source.
- ❌ Unauthorized use, reverse engineering, or redistribution without permission is strictly prohibited.

---

## 💬 Support

Have issues or feature requests?  
DM via GitHub: [@nitiksh](https://github.com/nitiksh)

---

## 🙏 Credits

- Python & Flask
- Tesseract OCR (by Google)
- PIL (Python Imaging Library)

---

### 🔐 Legal Notice

This tool is protected under copyright and license terms.  
By using this software, you agree to the terms and conditions listed above.

---

**Created by:** [ntxm.org](https://ntxm.org) <br/>
**GitHub Organization:** [https://github.com/ntxmofficial](https://github.com/ntxmofficial) <br/>
**Author:** [https://github.com/nitiksh](https://github.com/nitiksh) <br/>
