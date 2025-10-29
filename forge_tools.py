from superagi.tools.base_tool import BaseTool

class ForgeBuilder(BaseTool):
    name = "ForgeBuilder"
    description = "Builds Forge project components."

    def _execute(self, **kwargs):
        # your logic here
        return "Forge build complete."

class ForgeAnalyzer(BaseTool):
    name = "ForgeAnalyzer"
    description = "Analyzes Forge data."

    def _execute(self, **kwargs):
        return "Forge analysis complete."


class ForgeFileTool(BaseTool):
    name = "Forge File"
    description = "Read or write files in the Forge directory."

    def _execute(self, path: str, content: str = None, mode: str = "read"):
        base = "/app/forge/"
        abs_path = os.path.join(base, path)
        if mode == "write":
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, "w") as f:
                f.write(content or "")
            return f"Wrote file {path}"
        with open(abs_path, "r") as f:
            return f.read()


class ForgeShellTool(BaseTool):
    name = "Forge Shell"
    description = "Run shell commands safely in the Forge workspace."

    def _execute(self, command: str) -> str:
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd="/app/forge/workspace"
            )
            return f"Exit {result.returncode}\\nSTDOUT:\\n{result.stdout}\\nSTDERR:\\n{result.stderr}"
        except Exception as e:
            return f"Shell execution failed: {e}"
