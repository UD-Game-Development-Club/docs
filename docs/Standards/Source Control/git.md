# Git Standards

## Commits

Git commits should be short and focused, in the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format. Here is a quick primer:

- `fix: <message>` - A bug fix
- `feat: <message>` - A new feature
- `docs: <message>` - Documentation changes
- `style: <message>` - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor: <message>` - A code change that neither fixes a bug nor adds a feature
- `perf: <message>` - A code change that improves performance
- `test: <message>` - Adding missing tests or correcting existing tests
- `chore: <message>` - Changes to the build process or auxiliary tools and libraries such as documentation generation
- `ci: <message>` - Changes to our CI configuration files and scripts

## Branching

Branches should be created per-feature, be named using [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case), with a leading grouping token. These branch names should be kept extremely brief (like 4-5 non-token words MAX). Here are some examples, which show each grouping token:

- `feat/awesome-new-feature` - This branch adds a new feature
- `bug/fix-broken-thing` - This branch fixes a bug
- `wip/working-on-something` - This branch is a work-in-progress, with no anticipation of when it will be ready
- `junk/just-testing-something` - This is a throwaway branch for testing something, and will be deleted after the test is complete

## Reviewing & Merging

The GDC requires at least one repo admin approval for merging into the `main` branch, to ensure the codebase remains clean and consistent. In times of dire need, admins have the capability to force merge, but should abstain unless necessary.
