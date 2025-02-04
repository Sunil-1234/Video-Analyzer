# 🎥 AI-Powered YouTube Video Summarizer

An AI-driven web application that extracts and summarizes YouTube video transcripts using **Gemini 2.0 Flash Exp**. It provides quick insights and key takeaways from videos, making content consumption more efficient.

## 🚀 Features
- Extracts **YouTube video transcripts**
- Summarizes content using **Gemini 2.0 Flash Exp**
- Answers **user-specific queries** about the video
- Simple **Streamlit UI** for easy interaction
- Supports **auto-generated Hindi transcripts** if English is unavailable

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (Frontend UI)
- **YouTube Transcript API** (Transcript extraction)
- **Google Gemini API** (AI-powered summarization)
- **DuckDuckGo Search API** (For additional insights)
- **dotenv** (Environment variable management)

## 📌 Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Sunil-1234/Video-Analyzer.git
   cd Video_summarizer
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up API Keys:**
   - Create a `.env` file in the project root and add:
     ```ini
     GOOGLE_API_KEY=your-google-api-key
     ```
   - Replace `your-google-api-key` with your actual API key.

## 🎯 Usage

1. **Run the Streamlit App:**
   ```sh
   streamlit run app.py
   ```

2. **Enter a YouTube Video URL** and click **"Summarize Video"** to get key takeaways.
3. **Ask specific questions** about the video and click **"Get Insights"**.

## 🔧 Troubleshooting
- If you get an error like `No transcripts found`, the video might only have **auto-generated Hindi transcripts**. The app will try fetching them automatically.
- Ensure your **Google API key** is valid and has access to the Gemini model.

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue if you find bugs or have feature suggestions.



---
Developed by **Sunil Kumar Modi** 🚀

