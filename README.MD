# 🧠 Smart Text Analysis & Named Entity Recognition

A Natural Language Processing (NLP) web application built with **Python, SpaCy, TextBlob, and Streamlit**.

The application allows users to enter text or upload documents and performs multiple NLP tasks such as **tokenization, Part-of-Speech (POS) tagging, lemmatization, Named Entity Recognition (NER), sentiment analysis, word-frequency analysis, and visualization**.

---

## 🚀 Features

### 📝 Text Analysis
Enter text directly into the application and analyze it using NLP techniques.

- Tokenization
- Stop-word identification
- Part-of-Speech (POS) tagging
- Lemmatization
- Word frequency analysis
- Named Entity Recognition
- Sentiment analysis

### 📂 File-Based NLP Analysis

Upload documents and analyze their content.

Supported formats:

- `.txt`
- `.pdf`
- `.docx`

The application extracts the text from the uploaded document and performs the same NLP analysis.

### 🏷️ Named Entity Recognition (NER)

The application identifies important entities from text using **SpaCy**.

Examples include:

- 👤 PERSON
- 🏢 ORGANIZATION
- 📍 LOCATION / GPE
- 📅 DATE
- 💰 MONEY
- 📊 Other supported entities

Example:

```text
Apple was founded by Steve Jobs in California.
