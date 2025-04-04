# 📝 SmartText Generator

SmartText Generator is a Streamlit web app that allows users to generate various types of written content (essays, reports, emails, blog articles) based on user-provided keywords, writing style, tone, and word count.

It uses OpenAI's GPT model (via API) to produce informative, structured, and keyword-integrated content.

---

## 🚀 Features

- 🔤 Keyword-based content generation  
- 📚 Multiple use cases: Essay, Report, Email, Blog Article  
- ✍️ Customizable writing style: Casual / Formal / Persuasive  
- 🎭 Adjustable tone: Neutral / Passionate / Objective  
- 🔢 Word count control (100–800 words)  
- 📄 Output format selection: Plain Text / Markdown / HTML  
- ✅ Word count displayed at the end of output (optional)

---

## 🛠️ Setup

### 1. Clone this repository
### 2. Install dependencies
pip install -r requirements.txt
### 3. Set your OpenAI API key
Set the environment variable OPENAI_API_KEY
### 4. Run the App
streamlit run app.py

```
smarttext-generator/
│
├── app.py                   # Main Streamlit app
├── openai_connection_api.py # OpenAIClient class for GPT interaction
├── requirements.txt         # Python dependencies
└── README.md                # You're here!
```

