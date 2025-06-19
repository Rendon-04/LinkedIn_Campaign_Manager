# Job Search Agent

An AI-powered LinkedIn-style job search assistant that helps job seekers discover job opportunities, generate custom outreach messages, and track progress — all from a centralized dashboard.

<img width="1728" alt="Screenshot 2025-06-18 at 11 22 34 AM" src="https://github.com/user-attachments/assets/d54df6d6-3ecc-40ba-b45f-5e17b4a04c57" />
<img width="1728" alt="Screenshot 2025-06-18 at 11 16 41 AM" src="https://github.com/user-attachments/assets/1d6fab5d-f94a-4144-83f6-eeb36697db83" />



## Features

- **Suggested Jobs** — Browse job suggestions based on target roles and industries.
- **AI Message Generator** — Compose personalized outreach messages using OpenAI GPT-4.
- **Message Flow Suggestions** — See tailored suggestions based on selected job and your skills.
- **Weekly Strategy** — Keep track of high-level job-seeking goals.
- **Next Steps** — Follow actionable steps toward your next role.
- **Campaign Insights** — Visualize engagement metrics like responses and open rates.
- MVP version with no login required.

---

## 🛠️ Tech Stack

| Frontend            | Backend            | AI & Tools        |
|---------------------|--------------------|-------------------|
| React + Vite        | FastAPI (Python)   | OpenAI GPT-4      |
| Tailwind / SCSS     | Pydantic           | Axios             |
| React Context API   | Uvicorn            |                   |

---

## 🧑‍💻 How It Works

1. Select a job from the suggested list.
2. View tailored message suggestions with keywords and flow tips.
3. Use the AI-powered generator to compose a message.
4. Track messaging progress and conversion metrics on the dashboard.

---


## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.10+
- [OpenAI API key](https://platform.openai.com/account/api-keys)

---

### Installation

#### 1. Clone the repo:

```bash
git clone https://github.com/your-username/job-search-agent.git
cd job-search-agent
````

---

#### 2. Start the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file in the backend with:

```
OPENAI_API_KEY=your-openai-key-here
```

Then run:

```bash
uvicorn app.main:app --reload
```

---

#### 3. Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:3000`
Backend runs at: `http://localhost:8000`

---

## Environment Variables

| Variable         | Description               |
| ---------------- | ------------------------- |
| `OPENAI_API_KEY` | Your OpenAI GPT-4 API Key |

---

## Example Mock User

For demo purposes, the app uses the following mock user:

```json
{
  "name": "Ivan Rendon",
  "job_goal": "Software Engineer",
  "industry": "Tech",
  "skills": ["React", "FastAPI", "PostgreSQL"]
}
```

---

## Future Enhancements

* User Authentication (OAuth or Email Login)
* Memory-based conversation tracking
* Resume/Cover Letter Upload
* Calendar integrations for interview scheduling
* Multi-channel outreach (email, LinkedIn, etc.)

---

## Build

Built by [Ivan Rendon](https://www.linkedin.com/in/ivanrendon91/)
and Inspired by LinkedIn.
