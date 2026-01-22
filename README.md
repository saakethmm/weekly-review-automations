# Weekly Review Automation


## Project Overview

Automate the grunt work of weekly reflections on PACTs (Purposeful, Actionable, Continuous, Trackable) -- borrowed from Tiny Experiments. Reflect naturally in Apple Notes, then let Claude propagate your changes across Notion, TickTick, and Google Sheets through conversational AI powered by MCP (Model Context Protocol).

Focus on meaningful reflection - Claude handles the cross-platform sync.

## The Problem

Weekly reviews involve:
1. **Meaningful work** (~1 hour): Reflecting on the week in Apple Notes, deciding what's working, adjusting PACTs
2. **Grunt work** (frustrating, time-consuming): Manually propagating those changes across:
   - Notion PACT database (structured records)
   - TickTick task descriptions (daily interface)
   - Google Sheets tracking columns (completion data)

Cross-checking consistency across three platforms is tedious and error-prone.

This project eliminates the grunt work through natural language AI interpretation.

## The Solution

**Natural Reflection → AI-Powered Sync**

Write your weekly reflection and PACT adjustments in Apple Notes (where you already think), then paste into Claude Desktop. MCP servers handle the rest:

1. **Reflect in Apple Notes** - Write freely about what's working, what needs to change
2. **Paste into Claude Desktop** - Share your reflection notes
3. **Claude interprets and syncs** via MCP:
   - Parses your natural language updates
   - Updates Notion database (PACT records)
   - Modifies TickTick tasks (preserving structure)
   - Adjusts Google Sheets columns
4. **Review and iterate** - Claude shows what changed, you can refine
5. **Done** - All three platforms in sync from one reflection

## System Architecture

### MCP-Based Data Flow

```
┌─────────────────────────────────────┐
│        Apple Notes                   │
│  (Weekly reflection + PACT updates)  │
│                                      │
│  "Application Writing PACT:          │
│   - Change to ≥1 response per day    │
│   - Duration: 2 weeks                │
│   - Add: turn internet off"          │
└─────────────────────────────────────┘
        │
        │ (Copy/Paste)
        ▼
┌─────────────────────────────────────┐
│      Claude Desktop                  │
│  (Conversational AI + MCP)           │
│                                      │
│  Parses natural language             │
│  Reasons about changes               │
│  Orchestrates updates                │
└─────────────────────────────────────┘
        │
        ├───────────────┬──────────────┬──────────────┐
        ▼               ▼              ▼              ▼
┌─────────────┐ ┌─────────────┐ ┌────────────┐ ┌────────────┐
│   Notion    │ │  TickTick   │ │  Sheets    │ │  Examples  │
│ MCP Server  │ │ MCP Server  │ │ MCP Server │ │(Templates) │
└─────────────┘ └─────────────┘ └────────────┘ └────────────┘
        │               │              │
        ▼               ▼              ▼
┌─────────────┐ ┌─────────────┐ ┌────────────┐
│  Notion DB  │ │ TickTick API│ │   Sheets   │
│(PACT Data)  │ │   (Tasks)   │ │  (Tracker) │
└─────────────┘ └─────────────┘ └────────────┘
```

### How It Works

**During Your Weekly Review:**

1. **Reflect in Apple Notes**
   - Review your week
   - Note what's working, what isn't
   - Write PACT adjustments in natural language:
     ```
     Application Writing PACT:
     - Reduce scope to ≥1 response (was 2 responses + messaging)
     - 2 week trial
     - Add reminder to turn off internet

     Sleep PACT:
     - Too ambitious at daily, scale to 3x/week

     New: Morning Journaling
     - 5min after meditation, daily, 1 month trial
     ```

2. **Copy into Claude Desktop**
   - Paste your reflection notes
   - Say: "Update my PACTs based on these notes"

3. **Claude Interprets & Syncs**
   - Parses your natural language
   - Identifies which PACTs changed and how
   - Uses MCP to:
     - Read current state from Notion/TickTick
     - Calculate what needs updating
     - Update Notion PACT database
     - Modify TickTick task descriptions (preserving your structure)
     - Adjust Google Sheets columns (rename, hide/unhide)

4. **Real-Time Feedback**
   ```
   Claude: I've processed your updates:

   ✓ Application Writing PACT:
     - Notion: Updated name, action, duration (2 weeks), revisit (Jan 25)
     - TickTick: Task renamed, description updated, messaging content removed
     - Sheets: Column renamed to "Application Writing Task"

   ✓ Sleep PACT:
     - Notion: Frequency changed to "3x/week"
     - TickTick: Recurrence updated to 3x per week
     - Sheets: No change needed

   ✓ Morning Journaling (NEW):
     - Notion: New PACT created
     - TickTick: New daily task created
     - Sheets: New column added

   Want to see any of the updated task descriptions?
   ```

5. **Iterate Naturally**
   - "Actually, make Sleep PACT 4x/week instead"
   - "Show me the TickTick description for Application Writing"
   - Claude adjusts in real-time

**Result**: One reflection in Apple Notes propagates everywhere automatically.

## PACT Structure

### Notion Fields

**Note**: Notion is updated via MCP based on your Apple Notes reflections - you don't manually edit it. It serves as the structured database that syncs with TickTick and Sheets.

Fields in the Notion PACT database:
- **name**: PACT identifier (e.g., "Application Writing Task")
- **action**: What to do (e.g., "Write out ≥1 written responses")
- **frequency**: How often (e.g., "daily (workdays)", "weekly", "3x/week")
- **description**: Additional context, reminders, guidelines
- **duration**: How long to trial this version (e.g., "2 weeks", "1 month")
- **next_revisit_date**: When to review this PACT again (calculated: prior_sunday + duration)
- **status**: "Active" or "Inactive" (determines if PACT is currently being tracked)

### TickTick Task Format
```
Task Name: [PACT Name] ([Action])

Description:
## Tasks:
- [ ] [Specific task items]
- [ ] [Additional checkboxes as needed]

[Any specific reminders or notes]

---
## Guidelines
[Instructions for completing the task]
[Motivational reminders]
[Time/energy management notes]
```

### Google Sheets Structure
- **Columns**: One per PACT (named by PACT name)
- **Rows**: Dates
- **Values**:
  - `1` = completed
  - `0` = not done
  - `-1` = not applicable (e.g., rest day)

## Update Types

### Modifying Existing PACTs
- Change PACT name → Update TickTick task name, Sheets column name
- Change frequency → Update TickTick recurrence
- Change duration → Update Notion revisit date
- Change description → Update relevant parts of TickTick description (preserve structure)

**Key Principle**: Preserve as much of the existing TickTick content as possible. Only modify what changed in Notion.

### Adding New PACTs
- Create new TickTick task based on Notion fields
- Use example tasks as templates (match similar PACT types)
- Add new column in Sheets

### Pausing PACTs
When a PACT's status is changed to "Inactive" in Notion:
- **TickTick**: Clear the task's due date/recurrence (task remains but is not scheduled)
- **Sheets**: Hide the column (data is preserved, not deleted)
- **Notion**: Status field = "Inactive"

When reactivating (status changed back to "Active"):
- **TickTick**: Restore recurrence based on frequency field
- **Sheets**: Unhide the column
- **Notion**: Status field = "Active"

## AI Reasoning: From Natural Language to Structured Updates

Claude Desktop handles the complex interpretive work that was previously ambiguous:

### 1. Natural Language Parsing
**Your Apple Notes:**
```
Application Writing PACT:
- Reduce to ≥1 response per day (was doing 2 responses + messaging)
- This is just for writing, networking separate
- 2 week trial
- Turn internet off during block
```

**Claude extracts:**
- PACT name: "Application Writing"
- Change type: Scope reduction + separation
- New action: "Write ≥1 response per day"
- Duration: 2 weeks
- Additional note: Internet blocking reminder
- Platforms to update: All three (Notion, TickTick, Sheets)

### 2. Context Understanding via MCP

**Fetches current state:**
- Notion: Current "Networking Task" PACT details
- TickTick: Existing task with 2 responses + 1 message checkboxes
- Sheets: "Networking Task" column

**Identifies changes:**
- Name change: "Networking Task" → "Application Writing Task"
- Action simplified: Remove messaging component
- Checkboxes: Remove response 2 and message checkboxes
- Guidelines: Update quantity from "2 responses + 1 message" to "≥1 response"
- New reminder: Add internet blocking note

### 3. Preserves Structure

**In TickTick:**
- Keeps `## Tasks` and `## Guidelines` sections
- Preserves motivational text ("broader health", "P habit", etc.)
- Maintains checkbox format
- Only modifies what changed

**Example transformation:**
```diff
- Networking Task (Write out 2 written responses and 1 Message)
+ Application Writing Task (Write out ≥1 written responses)

  ## Tasks:
  - [ ] Response 1: [specific prompt]
- - [ ] Response 2: [specific prompt]
- - [ ] 1 message: [contact info]
+
+ Turn Internet off in this block if possible.

  ## Guidelines
- Write 2 responses and send one email/message...
+ Write ≥1 response for an interesting opportunity...

  [Motivational text preserved exactly]
```

### 4. Three-Way Sync

**Updates all platforms consistently:**
- **Notion**: Database record with structured fields
- **TickTick**: Task name, description, recurrence
- **Sheets**: Column names, visibility (hide/unhide for inactive PACTs)

### 5. Handles Edge Cases

- **New PACTs**: Uses example templates to generate appropriate TickTick format
- **Paused PACTs**: Clears TickTick recurrence, hides Sheets column, sets Notion status
- **Ambiguity**: Asks clarifying questions ("Did you mean 3x per week or every 3 weeks?")
- **Conflicts**: Reports if manual edits exist in TickTick that differ from Notion

**Key Innovation**: The interpretive work that was previously the hardest part (extracting structured updates from natural language reflections) now happens conversationally through Claude's reasoning + MCP's direct platform access.

## Tech Stack & Configuration

### Core Components

**Claude Desktop**
- Your conversational interface for managing PACTs
- Connects to all platforms via MCP servers

**MCP Servers (Model Context Protocol)**
Three custom MCP servers provide Claude with access to your platforms:

1. **Notion MCP Server**
   - Reads/writes PACT database
   - Queries old vs new state
   - Env: `NOTION_TOKEN`, `NOTION_DATABASE_ID`

2. **TickTick MCP Server**
   - Fetches existing tasks
   - Updates task names, descriptions, recurrence
   - Env: TickTick OAuth2 credentials

3. **Google Sheets MCP Server**
   - Reads/writes tracking columns
   - Hides/unhides columns based on PACT status
   - Env: Google service account credentials

### Configuration Files

**`claude_desktop_config.json`**
Configure MCP servers in Claude Desktop:
```json
{
  "mcpServers": {
    "notion": {
      "command": "node",
      "args": ["path/to/notion-mcp-server/build/index.js"],
      "env": {
        "NOTION_TOKEN": "secret_xxx",
        "NOTION_DATABASE_ID": "xxx"
      }
    },
    "ticktick": {
      "command": "node",
      "args": ["path/to/ticktick-mcp-server/build/index.js"],
      "env": {
        "TICKTICK_CLIENT_ID": "xxx",
        "TICKTICK_CLIENT_SECRET": "xxx"
      }
    },
    "sheets": {
      "command": "node",
      "args": ["path/to/sheets-mcp-server/build/index.js"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "path/to/credentials.json",
        "SPREADSHEET_ID": "xxx"
      }
    }
  }
}
```

**Example TickTick Tasks**
- Store 3-5 representative PACT formats in `examples/ticktick_task_examples.md`
- Claude references these when creating new PACTs or understanding structure
- Ensures consistency with your preferred formatting

**Frequency Mappings**
- Define how Notion frequencies map to TickTick recurrence in `config/frequency_mappings.json`
- Examples: "daily (workdays)" → TickTick weekday recurrence

**Credentials**
- Store in `.env` files (never commit to git)
- Each MCP server loads from environment variables

## Usage

### Typical Weekly Review Workflow

**1. Reflect in Apple Notes:**

```
Week of Jan 12, 2026 - Weekly Review

What worked:
- Application writing felt better when focused (no networking mixed in)
- Sleep routine too rigid, missing days made me feel bad

What to change:

Application Writing PACT:
- Separate from networking (different mental modes)
- Reduce to ≥1 response per day (1 is sustainable, 2 was burnout)
- 2 week trial starting today
- Need reminder: turn internet off during writing block

Sleep PACT:
- Scale back from daily to 3x/week
- Remove pressure language from task description
- Keep 1 month duration

New experiment:

Morning Journaling PACT:
- 5 min reflection after meditation
- Daily (including weekends)
- Simple prompt: "What matters today?"
- 1 month trial
```

**2. Paste into Claude Desktop:**

```
You: Here's my weekly review with PACT updates:

[paste Apple Notes content above]

Can you update Notion, TickTick, and Sheets to reflect these changes?

Claude: I'll process your reflection and sync across all platforms.

[Reading current state via MCP...]

I see three changes:

1. Application Writing PACT (modified from "Networking Task")
   - Separating writing from networking
   - Scope: ≥1 response per day
   - Duration: 2 weeks (revisit: Jan 25)
   - Add: Internet blocking reminder

2. Sleep PACT (frequency adjustment)
   - Change from daily → 3x/week
   - Duration stays at 1 month

3. Morning Journaling PACT (new)
   - Daily practice
   - 5 min journaling
   - 1 month trial

Proceeding with updates...

[Updating Notion via MCP...]
✓ Application Writing: PACT updated (name, action, duration, revisit date)
✓ Sleep: Frequency changed to "3x/week"
✓ Morning Journaling: New PACT created

[Updating TickTick via MCP...]
✓ Application Writing: Task renamed, description updated, messaging content removed, internet reminder added
✓ Sleep: Recurrence changed to 3x/week
✓ Morning Journaling: New daily task created with journaling prompt

[Updating Sheets via MCP...]
✓ "Networking Task" column → "Application Writing Task"
✓ Sleep column: No change needed
✓ "Morning Journaling" column added

All platforms synced! Want to see any of the updated task descriptions?

You: Show me the Application Writing task description

Claude: Here's the updated TickTick task:

---
Application Writing Task (Write out ≥1 written responses)

## Tasks:
- [ ] Response 1: [your current prompt]

Turn Internet off in this block if possible.

(adapt order/tasks needed based on time/energy)

---
## Guidelines
Write ≥1 response for an interesting opportunity! Set time and extend
intentionally if needed (keeping in mind other PACTs/highlight).

Think of this is for my ~*broader health*~, ~*something that will help
with my P habit*~, ~*for my self-confidence*~, ~*for financial and
social reasons*~...

[rest of your motivational text preserved]
---

You: Perfect! That's exactly what I wanted.
```

### Common Commands

**After pasting your Apple Notes reflection:**
- "Update all platforms based on these notes"
- "What changes did you identify?"
- "Show me what the TickTick task looks like before updating"
- "Actually, make that 3 weeks instead of 2"
- "What PACTs are currently active in Notion?"
- "Pause the [PACT name] PACT for now"

## Design Principles

1. **Reflect naturally, sync automatically**: Write your thoughts in Apple Notes where you already reflect. Paste once, Claude handles propagating changes across all platforms through conversational AI.
2. **Preserve > Generate**: Keep existing content, only change what's needed. TickTick task structure and motivational text stays intact.
3. **Natural language → Structured data**: Claude interprets your free-form reflections and translates them into structured updates across Notion (database), TickTick (tasks), and Sheets (tracking). No manual data entry.
4. **Safety first**: Claude shows what it's changing before applying. You can iterate and refine in real-time.
5. **Minimal effort**: Weekly reviews should be ≤1 hour of meaningful reflection, not frustrating cross-platform data entry.

## Future Enhancements

- **Apple Notes direct integration**: MCP server that watches Apple Notes for changes (no manual paste)
- **Voice reflection**: Speak your weekly review, Claude transcribes and updates everything
- **Smart suggestions from tracking data**: "You've missed Sleep PACT 4/7 days - want to adjust frequency?"
- **Completion analytics**: "Show me my PACT completion trends over the last month"
- **Automated weekly prompts**: Claude asks reflection questions based on your PACTs
- **Multi-user support**: Share PACT templates and sync patterns with others
- **Rollback capability**: "Undo my last weekly review changes"
- **Conflict detection**: Warn if manual TickTick edits differ from Notion state
