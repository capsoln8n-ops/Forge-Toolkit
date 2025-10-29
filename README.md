# Forge Toolkit 🔩

This is a custom SuperAGI toolkit that gives agents direct file and shell access
inside a mounted `/app/forge` workspace.

## Tools

### 🧾 Forge File
Read or write files within `/app/forge`.

### ⚙️ Forge Shell
Run safe shell commands (e.g., `ls`, `pytest`, `docker compose up`) inside `/app/forge/workspace`.

## Installation
1. In SuperAGI dashboard → Tools → Add a new tool.
2. Paste this repo URL.
3. Restart backend or refresh toolkits.
4. Done — new tools will appear under "Forge Toolkit".
