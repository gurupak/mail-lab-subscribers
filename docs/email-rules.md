# Rules for every newsletter issue

An issue file must:

1. Start with a line `Subject: ...` of 50 characters or fewer (as counted by Python's `len()`; an emoji like 👍🏽 counts as 2).
2. Then a line `Preview: ...` of 90 characters or fewer (counted the same way).
3. Greet the reader: the first line after the Preview (skipping blank lines) starts with `Hi {{first_name}}`.
4. Have exactly one main link, written as `[Button text](https://...)`, between the greeting and the footer. Links in the footer don't count.
5. End with a sign-off, then this two-line footer as plain text:
   - a line that starts `You're getting this because`
   - a line that contains `Unsubscribe: {{unsubscribe_url}}`
