---
course: llm-zoomcamp
id: bf0403d21b
question: 'OpenAI: Why does my token count differ from what OpenAI reports?'
section: 'Module 1: Introduction'
sort_order: 320
---

When using tiktoken.encode() to count tokens in your prompt, you might get a number like 320, while OpenAI’s API response reports something like 327. This is expected and due to internal tokens added by OpenAI’s chat formatting.

Here’s what happens under the hood:

Each message in a chat.completions.create() call (e.g., {role: "user", content: "..."}) adds 4 structural tokens (role, content, separators).

The API also adds 2 tokens globally to mark the start of assistant response generation.

Any extra newlines, whitespace, or uncommon Unicode characters in your content may slightly increase the token count.

So even if your visible text is 320 tokens, OpenAI may count 327 due to these internal additions.

Added by José Luis Martínez (Maxkaizo)

