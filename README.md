# AI Blog-to-Video Generator – Convert Articles into Stunning Videos

A Python-powered AI tool that generates text on a specific topic and converts it into an engaging video using OpenAI, GTTS (Google Text-to-Speech), and MoviePy.

## 🚀 Features
- Generate AI-written content on any topic using OpenAI's API
- Convert the generated text into speech using GTTS
- Create a video with text, speech, and visuals using MoviePy
- Automate the entire process for content creators

## 📌 Prerequisites
Make sure you have the following installed before running the script:
- [Python](https://www.python.org/downloads/) (Latest Version)
- [Visual Studio Code](https://code.visualstudio.com/download) (or any other code editor)

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rohit7008/AI-Content-Generator-Suitable-for-blog-article-generation.git
cd AI-Content-Generator-Suitable-for-blog-article-generation
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install openai gtts moviepy
```

### 4️⃣ Set Up Your OpenAI API Key
#### Using Environment Variables
Create a `.env` file in the project root and add:
```env
OPENAI_API_KEY=your-openai-api-key-here
```
Modify your Python script to load the key:
```python
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## 🎮 How to Use
### 1️⃣ Generate AI Text
Run the script to generate text:
```bash
python text_generator.py
```
Enter a topic when prompted, and the script will generate a well-structured article.

### 2️⃣ Convert Text to Video
Run the video generator script:
```bash
python video_generator.py
```
This will:
- Convert the AI-generated text into speech
- Generate a video with visuals, text, and narration

## 🎥 Demo & Tutorial
Watch the full tutorial video here:
[YouTube Tutorial](https://youtu.be/AVgBTwbwOkg)

## 🐝 Contributing
Feel free to submit pull requests or open issues for improvements!

## 📚 License
This project is open-source and available under the MIT License.

---

Enjoy automating your content creation! 🚀🎥 If you like this project, give it a ⭐ on GitHub!

