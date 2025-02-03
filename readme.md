# Number Classification API

A Flask-based API to classify numbers with properties such as prime, perfect, Armstrong, even/odd, and more. It also fetches fun mathematical facts about the provided number.

## 🚀 Features
- **Prime Check**: Determines if a number is prime.
- **Perfect Number Check**: Identifies perfect numbers.
- **Digit Sum**: Calculates the sum of all digits.
- **Property Classification**: Classifies numbers as Armstrong, even, or odd.
- **Fun Facts**: Retrieves interesting mathematical facts via the [Numbers API](http://numbersapi.com/).

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

2. **Set up a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install flask flask-cors requests
```

4. **Run the application:**
```bash
python app.py
```

## 🧪 API Usage

### **Endpoint:** `/api/classify-number`
**Method:** `GET`

### **Query Parameter:**
- `number` (required): The number you want to classify.

### **Example Request:**
```bash
http://localhost:5000/api/classify-number?number=28
```

### **Sample Response:**
```json
{
  "number": "28",
  "is_prime": false,
  "is_perfect": true,
  "digit_sum": 10,
  "properties": ["Even"],
  "fun_fact": "28 is the second perfect number."
}
```

### **Error Responses:**
- **For Negative Numbers:**
```json
{
  "number": "-5",
  "error": true,
  "message": "Negative numbers are not supported"
}
```
- **For Invalid Inputs:**
```json
{
  "number": "alphabet",
  "error": true
}
```

## ⚙️ Technologies Used
- **Python**
- **Flask**
- **Flask-CORS**
- **Requests**

---

**Note:** Ensure you have an active internet connection for the fun fact feature to work correctly.

