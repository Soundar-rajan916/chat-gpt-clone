# Django ChatGPT Clone (Powered by Groq & LangChain)

A lightweight, fast, and fully functional ChatGPT clone built with Django. It features a retro/brutalist UI design, real-time AI response streaming using **HTMX**, and is powered by the blazing fast **Groq API** (Llama 3) via **LangChain**.

## 🚀 Features

- **Real-time Streaming:** AI responses stream instantly into the chat interface just like ChatGPT, using Django's `StreamingHttpResponse` and HTMX.
- **Auto-Generated Titles:** Chat threads automatically generate a context-aware title based on your first message.
- **Thread Management:** Create new chats, view past thread history, and seamlessly switch between active conversations.
- **Markdown Support:** Renders rich markdown (code blocks, lists, headers) in real-time using Marked.js.
- **User Authentication:** Built-in account system (signup/login/logout) to keep user threads private and secure.
- **No JS Framework:** The frontend avoids heavy SPA frameworks (React/Vue) in favor of lightweight HTML, Vanilla CSS, and HTMX.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTMX, Marked.js, HTML5, CSS3 (Flexbox/Brutalist Aesthetic)
- **AI/LLM:** Groq API (`llama-3.3-70b-versatile`)
- **Orchestration:** LangChain (`langchain`, `langchain-groq`)
- **Database:** SQLite (default Django DB)

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8+ installed
- A [Groq API Key](https://console.groq.com/) for accessing the LLM.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd chatgpt
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy the example environment file and add your Groq API key:
   ```bash
   cp .env.example .env
   ```
   Open the `.env` file and update it with your actual key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   ```

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, to access the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

8. **Open the App:**
   Navigate to `http://127.0.0.1:8000` in your web browser.

## 📁 Project Structure

- `main/` - The core Django project settings and routing.
- `chat/` - The main app handling threads, messages, LLM LangChain logic, and HTMX views.
- `accounts/` - User authentication and account management.
- `templates/` - HTML templates, including the `home.html` chat interface.
- `static/` - Static assets, including the custom brutalist `style.css`.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the MIT License.
