# AGENTS.md

## Project

Mail-Lab is a command-line tool for one newsletter: PROCARMA Club.
It reads the subscribers, checks an issue, and sends it to a practice mail server.

## Rules

- Use uv for everything: creating the project, adding packages, running code and tests.
- Never use a real person's email address. Use `@example.com` addresses, and `@resend.dev` for practice sends.
- Commit and push after every step.

## Behaviors first

- I give the expected answers.
- You write them as checks (`assert` lines in `checks.py` that call my functions).
- You show me the checks failing.
- Then you write the code that makes them pass.

## How I learn

- I have completed up to 13.9 of https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/ and I update this number as I learn.
- Write only with what I have learned. If something new would really help, stop and tell me its name in one line. I decide.
- When the code uses something new, show me that piece first and ask me to predict what it does. Stay quiet while I guess. Then run it, and explain a line only when I ask.
