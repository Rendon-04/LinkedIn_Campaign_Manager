# Job Search Agent

An AI-powered LinkedIn-style job search assistant that helps job seekers discover job opportunities, generate custom outreach messages, and track progress — all from a centralized dashboard.

<img width="1728" alt="Screenshot 2025-06-18 at 11 22 34 AM" src="https://github.com/user-attachments/assets/d54df6d6-3ecc-40ba-b45f-5e17b4a04c57" />
<img width="1728" alt="Screenshot 2025-06-18 at 11 16 41 AM" src="https://github.com/user-attachments/assets/1d6fab5d-f94a-4144-83f6-eeb36697db83" />

## Features

- **Suggested Jobs** — Browse job suggestions based on target roles and industries.
- **AI Message Generator** — Compose personalized outreach messages using OpenAI GPT-4.
- **Message Flow Suggestions** — See tailored suggestions based on your skills and the job selected.
- **Weekly Strategy** — Stay focused with high-level goals tied to your target field.
- **Next Steps** — Follow actionable steps based on your recent activities.
- **Campaign Insights** — Visualize engagement metrics like message logs.
- **Database-Driven Demo** — Fully functional backend with PostgreSQL.

MVP version — no login required.

---

## Tech Stack

| Frontend            | Backend            | AI & Tools        |
|---------------------|--------------------|-------------------|
| React (Webpack)     | FastAPI (Python)   | OpenAI GPT-4      |
| SCSS                | SQLAlchemy         | Axios             |
| React Context API   | Pydantic           | PostgreSQL        |

---

## How It Works

1. Select a job from the list of suggested jobs.
2. View dynamic strategy suggestions for your job search.
3. Generate a personalized outreach message with AI.
4. Log your actions and see updated recommendations.
5. Everything is stored in a PostgreSQL database.

---

## ⚙Getting Started

### Prerequisites

✅ Node.js (v18+) and npm  
✅ Python 3.10+  
✅ PostgreSQL running locally (or via Docker)  
✅ [OpenAI API key](https://platform.openai.com/account/api-keys)

---

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/job-search-agent.git
cd job-search-agent
````

---

### 2. Create and Configure the Database

> You can use either:
>
> * **Local Postgres install**, or
> * **Docker Postgres** for convenience.

#### Option A - Local Postgres

Start Postgres locally and create a DB:

```sql
CREATE DATABASE linkedin_agent;
```

#### Option B - Docker

```bash
docker run -d \
  --name linkedin-agent-db \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=linkedin_agent \
  -p 5432:5432 \
  postgres:14
```

---

### 3. Set Up the Backend

From the root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/linkedin_agent
```

#### Create DB Tables

```bash
python create_tables.py
```

#### Load Mock Data

```bash
python -m app.utils.mock_loader
```

#### Run FastAPI

```bash
uvicorn app.main:app --reload
```
---

### 4. Set Up the Frontend

From the root:

```bash
cd frontend
npm install
npm run start
```
---

**Once the app is running:**

Visit:

```
http://localhost:3000
```

Click:

* **Suggested Jobs** → see jobs from your Postgres DB
* **Compose Message** → triggers a real AI-generated message
* **Log an Action** → logs new entries into your Postgres DB

✅ Check backend logs:

* You’ll see FastAPI handle real requests like:

```
GET /jobsearch/jobs
POST /agent/generate_message
GET /agent/next_steps/1
```

✅ Check your database:

```sql
SELECT * FROM users;
SELECT * FROM jobs;
SELECT * FROM actions;
```

…and confirm real data exists.

---

## Example Mock User

This user is inserted via the backend on startup:

```json
{
  "id": 1,
  "name": "Ivan Rendon",
  "job_goal": "Software Engineer",
  "industry": "Technology",
  "skills": ["Python", "React", "SQL", "FastAPI"]
}
```

---

## API Routes to Test

* `GET /jobsearch/jobs`
* `GET /jobsearch/user/1`
* `POST /agent/generate_message`
* `GET /agent/next_steps/1`
* `POST /agent/actions`

---

## Environment Variables

| Variable         | Description                |
| ---------------- | -------------------------- |
| `OPENAI_API_KEY` | Your OpenAI GPT-4 API Key  |
| `DATABASE_URL`   | Postgres connection string |

---

## Author

Built by [Ivan Rendon](https://www.linkedin.com/in/ivanrendon91/)
Inspired by LinkedIn.

