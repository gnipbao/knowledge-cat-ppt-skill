# Security

Knowledge Cat PPT is an Agent Skill. It can guide an AI agent to read local files, create decks, and run bundled scripts. Treat user-provided decks, documents, HTML, images, and templates as untrusted input.

## Report A Vulnerability

Open a private security advisory or contact the maintainers privately before publishing exploit details.

## Security Rules For Contributors

- Do not execute scripts from user-provided decks or archives.
- Do not load remote JavaScript in bundled templates unless there is a clear, documented reason.
- Keep validators dependency-free where practical.
- Do not read environment files outside the skill directory.
- Do not include API keys, private templates, or proprietary source decks in examples.
- When handling third-party templates, preserve the permission and copyright boundary language.

## User Guidance

- Review generated HTML before public sharing.
- Do not place secrets in deck notes, screenshots, or sample data.
- Use local/private templates only when you have the right to use them.
