
Alternatively, one can use a `.env` file to store all the API information.

## TickTick
```bash
claude mcp add --scope user ticktick \
  -e TICKTICK_CLIENT_ID="insert here from api website" \
  -e TICKTICK_CLIENT_SECRET="insert here from api website" \
  -e TICKTICK_ACCESS_TOKEN="appears after authorization" \
  -e TICKTICK_USERNAME="your_email@example.com" \
  -e TICKTICK_PASSWORD="password" \
  -- ticktick-sdk
```

**some common issues**: ticktick-sdk will show as not connected unless conda environment with ticktick-sdk installed is activated

* `--scope user` is key to ensuring the mcp is always visible (other options are `project` and `local`)


## Google Sheets

```bash
claude mcp add --scope user google-sheets \
	-e SERVICE_ACCOUNT_PATH=path/to/service/account/mcp-connector.json \
	-e DRIVE_FOLDER_ID=folder-id-from-url \
	-- uvx mcp-google-sheets@latest 
```

```json
"mcpServers": {
    "google-sheets": {
      "command": "uvx",
      "args": [
        "mcp-google-sheets@latest"
      ],
      "env": {
        "SERVICE_ACCOUNT_PATH": "path/to/service/account/mcp-connector.json",
        "DRIVE_FOLDER_ID": "folder-id-from-url"
      }
    }
  }
```

**some common issues**: must be created via google cloud API, creating new project, then API key


  ## Notion
```bash
  claude mcp add --scope user notion \
  -e NOTION_TOKEN=your-notion-token-here # looks like ntn_xxx \
  -- npx @notionhq/notion-mcp-server 
```


created via integration on https://notion.so



