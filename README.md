# AI Research Daily Bot

A simple Python bot that fetches recent AI-related papers from arXiv, summarizes them with Groq, and sends a daily digest email.

## What it does

The bot:
- fetches recent papers from arXiv in selected AI-related categories
- summarizes each paper using the Groq API
- formats the results into a readable email digest
- avoids sending the same paper twice by storing sent paper IDs in `sent_papers.json`

## Features

- fetches recent arXiv papers from categories such as `cs.AI`, `cs.CL`, `cs.LG`, `cs.CV`, `cs.RO`, and `cs.NE`
- generates concise summaries with key contributions, why it matters, and real-world applications
- sends the digest via Gmail SMTP
- keeps track of already-sent papers so you do not receive duplicates

## Requirements

- Python 3.11 or newer
- A Groq API key
- A Gmail account with an app password

## Setup

1. Clone the repository and open it in your terminal.

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   On macOS/Linux, use:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following values:

   ```env
   GROQ_API_KEY=your_groq_api_key
   SENDER_EMAIL=your_gmail_address@gmail.com
   SENDER_APP_PASSWORD=your_gmail_app_password
   RECIPIENT_EMAIL=destination_email@example.com
   ```

5. Make sure your Gmail account allows app passwords. If you are using Gmail, generate an app password from your Google account settings and use that instead of your normal password.

## Running the bot

Run the script from the project root:

```bash
python main.py
```

If new papers are found, the bot will summarize them and send an email. If no new papers are available, it exits gracefully.

## Configuration

The default behavior is defined in `src/config.py`. You can adjust:
- the arXiv categories
- the number of papers to include
- the summary length
- the email subject/message format
- retry and timeout settings

## Project structure

```text
main.py
src/
  config.py
  dedup.py
  email_sender.py
  fetch_papers.py
  formatter.py
  logger.py
  summarize.py
```

## Notes

- The bot stores sent paper IDs in `sent_papers.json` in the project root.
- If the Groq API fails or rate limits, it will retry and fall back to a simple summary.
- The bot uses the arXiv API directly, so internet access is required.

## Troubleshooting

- If you get a missing environment variable error, confirm that your `.env` file exists and contains all required keys.
- If Gmail authentication fails, verify that you used a valid Gmail app password.
- If no papers are found, check your internet connection or try again later.
