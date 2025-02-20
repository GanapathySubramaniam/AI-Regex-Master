# 🧠 **Regex Master: AI-Powered Regex Pattern Generator**
```
  _____                        __  __           _            
 |  __ \                      |  \/  |         | |           
 | |__) |___  __ _  _____  __ | \  / | __ _ ___| |_ ___ _ __ 
 |  _  // _ \/ _` |/ _ \ \/ / | |\/| |/ _` / __| __/ _ \ '__|
 | | \ \  __/ (_| |  __/>  <  | |  | | (_| \__ \ ||  __/ |   
 |_|  \_\___|\__, |\___/_/\_\ |_|  |_|\__,_|___/\__\___|_|   
              __/ |                                          
             |___/                                           
```
An advanced tool that leverages **Google's Gemini 1.5-Flash** model to transform natural language requirements into precise and effective **Regular Expressions (Regex)**. The application provides in-depth explanations, examples, and ready-to-use Python code snippets to simplify complex pattern matching tasks.

---

## 🚀 **Project Overview**

**Regex Master** is a powerful and interactive web application designed to assist developers, data analysts, and regex enthusiasts. By simply describing your pattern requirements in natural language, the app generates an accurate regex pattern, explains its components, and demonstrates its practical usage with Python code.

---

## 📂 **Project Structure**

```
📁 Regex-Master/
├── 📄 app.py                 # Streamlit app for user interface and interactions
├── 📄 requirements.txt       # Project dependencies
└── 📄 .env                   # (Optional) Store your API key securely
```

---

## 🧠 **Key Features**

- 📝 **Natural Language to Regex Conversion:** Converts plain language descriptions into regex patterns using **Gemini 1.5-Flash**.
- 📖 **Comprehensive Explanations:** Provides detailed breakdowns of each regex component.
- 🧪 **Example Scenarios:** Demonstrates the regex pattern with sample data.
- 💻 **Python Code Snippet Generation:** Shows how to integrate the regex in real-world Python scripts.
- 🎨 **User-Friendly Interface:** Built using **Streamlit** for a smooth and interactive experience.

---

## ⚡ **Getting Started**

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```text
streamlit
google-generativeai
```

### **2. Set Up API Key**

- Obtain your **Google Generative AI** API key.
- Configure the API key in the `app.py` file:

```python
api_key = "AI-XXXX"  # Replace with your actual API key
```

- Alternatively, store your API key in a `.env` file for security:

```plaintext
API_KEY=your_google_genai_api_key_here
```

### **3. Launch the Application**

```bash
streamlit run app.py
```

- Open the provided `localhost` link in your browser to access the **Regex Master** app.

---

## 🎯 **Usage Example**

### **Generate a Regex Pattern**

1. **Enter Sample Data:** Input data that needs pattern matching.
2. **Describe the Pattern:** Specify the type of pattern you want in natural language.
3. **Get Results:** Receive a well-structured regex pattern with explanations and code snippets.

---

## 📄 **Sample Output**

### **Example: Extracting Email Addresses**

- **Input Data:** `"Contact us at support@example.com or sales@company.org."`
- **Pattern Request:** `"Extract all email addresses from the text."`

#### **Generated Regex:**
```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

#### **Explanation:**
- `[a-zA-Z0-9._%+-]+` : Matches the local part of the email.
- `@` : Requires the "@" symbol.
- `[a-zA-Z0-9.-]+` : Matches the domain name.
- `\.[a-zA-Z]{2,}` : Matches the top-level domain.

#### **Example Python Code:**
```python
import re

text = "Contact us at support@example.com or sales@company.org."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)

print(emails)
# Output: ['support@example.com', 'sales@company.org']
```

---

## 🔮 **Future Enhancements**

- ✅ **Add Regex Validation:** Test patterns against sample data within the app.
- 📈 **Pattern Optimization Tips:** Suggest improvements for performance.
- 🌐 **Export to JSON:** Allow pattern and explanation exports for documentation.

