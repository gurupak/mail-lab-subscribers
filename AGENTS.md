# AGENTS.md

## Project

Mail-Lab is a command-line tool for one newsletter: PROCARMA Club.
It reads the subscribers, checks an issue, and sends it to a practice mail server.

## Rules

- Use uv for everything: creating the project, adding packages, running code and tests.
- Never use a real person's email address. Use `@example.com` addresses, and `@resend.dev` for practice sends.
- Commit and push after every step.
- Never read today's date inside the logic. Pass the run date in. Only the command line may read today's date.
- Command-line code goes under `if __name__ == "__main__":`, so importing the file (as the tests do) never runs it.
- When we learn a new rule in a session, propose it for AGENTS.md. I decide.

## Behaviors first

- I give the expected answers.
- You write them as tests: one pytest test per behavior in `test_maillab.py`, named for the behavior it checks, with `assert` lines that call my functions.
- Run the tests with `uv run pytest`.
- You show me the tests failing.
- Then you write the code that makes them pass.
- Expected answers come from me or the data, never from running the code and copying its output. Pick answers that also test the edges.
- Every new test must fail before the code exists. A test that passes straight away proves nothing.

## Testing

- When I ask for a test, check the numbers a second way that does not use Mail-Lab's code (a shell command or another Python module).
- Put any copies outside the project and change no project files.
- When a command crashes on data, check the data before changing the code.
- Read a Python error from the bottom: the last line says what went wrong; the lowest line in our own file says where.

## How I learn

- I have completed up to 13.11 of https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/ and I update this number as I learn.
- Write only with what I have learned. If something new would really help, stop and tell me its name in one line. I decide.
- When the code uses something new, show me that piece first and ask me to predict what it does. Stay quiet while I guess. Then run it, and explain a line only when I ask.
