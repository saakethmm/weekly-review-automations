# Weekly Review Automation

## Project Overview

Automate the grunt work of weekly reflections on PACTs (Purposeful, Actionable, Continuous, Trackable) -- borrowed from Tiny Experiments -- updates across multiple platforms. Focus on meaningful reflection while AI handles syncing changes to TickTick, Google Sheets, and Notion.

## The Problem

Weekly reviews involve:
1. **Meaningful work** (1 hour): Reflecting on the week, deciding what's working, adjusting PACTs
2. **Grunt work** (frustrating to cross-check and manually adjust): Manually updating the same changes across TickTick task descriptions, Google Sheets tracking columns, and Notion PACT database

This project eliminates the grunt work.

## The Solution

**Single Source of Truth: Notion**

1. Reflect in Apple Notes (for personal thinking)
2. Make PACT changes directly in Notion (edit existing PACTs, add new ones)
3. Run automation script
4. Review proposed changes
5. Confirm and sync to TickTick + Sheets

## System Architecture

### Data Flow

```
┌─────────────────┐
│  Apple Notes    │  (Reflection - for your thinking)
│  (Manual)       │
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  Notion Table   │  ◄── SOURCE OF TRUTH
│  (Manual Edit)  │      (PACT database)
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  Automation     │
│  Script         │
│  (Python + AI)  │
└─────────────────┘
        │
        ├──────────────┬──────────────┐
        ▼              ▼              ▼
┌─────────────┐  ┌──────────┐  ┌─────────────┐
│  TickTick   │  │  Sheets  │  │  State      │
│  (Tasks)    │  │ (Tracker)│  │  Snapshot   │
└─────────────┘  └──────────┘  └─────────────┘
```

### Pipeline Steps

1. **Fetch Old State**: Load previous Notion snapshot (from last sync)
2. **Fetch New State**: Get current Notion table
3. **Diff Changes**: Identify what PACTs were modified/added
4. **Fetch Current TickTick**: Get existing task content
5. **AI Reasoning**: Claude determines how to update TickTick while preserving structure
6. **Update Sheets**: Sync column names if PACT names changed
7. **Preview**: Show all proposed changes
8. **Confirm & Apply**: User approves, then sync to all platforms
9. **Save Snapshot**: Store current Notion state for next run

## PACT Structure

### Notion Fields
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

## AI Agent Reasoning

The agent uses Claude API to:
1. **Understand context**: Compare old vs new Notion state
2. **Preserve structure**: Keep TickTick task format (Tasks/Guidelines sections, checkboxes, motivational text)
3. **Make targeted changes**: Update only what's necessary based on Notion diff
4. **Generate new tasks**: For new PACTs, use example templates and adapt to new PACT's specifics
5. **Handle edge cases**: Decide how to represent complex changes while maintaining readability

## Configuration & References

The project includes:
- **Example TickTick tasks**: 3-5 representative PACT task formats for the AI to reference
- **API credentials**: Stored securely (not in git)
- **State snapshot**: Local JSON file tracking last Notion sync
- **Transformation rules**: Frequency mappings (e.g., "daily (workdays)" → TickTick "every weekday")

## Tech Stack

- **Python 3.x**: Main scripting language
- **Anthropic Claude API**: AI reasoning for updates
- **Notion API** (`notion-client`): Read PACT database
- **Google Sheets API** (`gspread`): Update tracking columns
- **TickTick API** (`ticktick-py` or `requests`): Update task descriptions

## Usage

```bash
# Run the sync
python sync_pacts.py

# Preview changes without applying
python sync_pacts.py --dry-run

# Verbose output for debugging
python sync_pacts.py --verbose
```

## Design Principles

1. **Manual reflection, automated sync**: Human-centered approach, augmented by AI to assist with semantic parsing and updating across tools
2. **Preserve > Generate**: Keep existing content, only change what's needed
3. **Notion as source of truth**: One place to make changes consistently (though might change this in the future)
4. **Safety first**: Preview before applying, easy rollback
5. **Minimal effort**: Weekly reviews should be ≤1 hour of your time and worthwhile to do, not frustrating

## Future Enhancements

- Automatic backup before applying changes
- Rollback command to undo last sync
- Natural language input parser (Apple Notes → Notion updates)
