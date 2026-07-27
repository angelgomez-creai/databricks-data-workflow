# Databricks IA Environment

## Configuration

### Databricks AI Dev Kit

A toolkit for coding agents (Claude Code, Codex, Cursor, and others) provided by Databricks Field Engineering, giving them Databricks-specific knowledge, skills, MCP tools, and the Databricks Builder App to build reliable workflows, pipelines, and dashboards faster. See the [Databricks AI Dev Kit GitHub repository](https://github.com/databricks-solutions/ai-dev-kit) for installation instructions.

### GitHub MCP

Connect to the GitHub remote MCP server using the Claude CLI:

```
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer <YOUR_TOKEN>"
```

To authenticate, generate a **fine-grained personal access token** in GitHub with the minimum permissions needed:

- **Repository access**: limit it to only the repository/repositories that are necessary — never grant access to all repositories.
- **Permissions**: grant only what's needed for now — `Contents` (commits), `Issues`, and `Pull requests` (read/write as applicable).

### Databricks MCP

```
claude mcp add databricks-sql-mcp --transport http "https://<your-workspace-hostname>/api/2.0/sql" --header "Authorization: Bearer <YOUR_TOKEN>"
```

Replace `<your-workspace-hostname>` with your Databricks workspace URL and `<YOUR_TOKEN>` with a Databricks personal access token.
