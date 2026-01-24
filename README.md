# Weekly Review Automation

## Project Overview

Automate the grunt work of weekly reflections on PACTs (Purposeful, Actionable, Continuous, Trackable) as seen in [Tiny Experiments](https://www.barnesandnoble.com/w/tiny-experiments-anne-laure-le-cunff/1145986849?ean=9780593715130) with some of my own personal tweaks. Reflect naturally in your own notes, then let Claude propagate your changes across Notion, TickTick, and Google Sheets through conversational AI powered by MCP (Model Context Protocol).

Focus on meaningful reflection - Claude handles the cross-platform sync.

## The Problem

Weekly reviews involve:
1. **Meaningful work** (~1 hour): Reflecting on the week in personal notes, deciding what's working, adjusting PACTs
2. **Grunt work** (frustrating, time-consuming): Manually propagating those changes across:
   - Notion PACT database (structured records)
   - TickTick task descriptions (daily interface)
   - Google Sheets tracking columns (completion data)

Cross-checking consistency across three platforms is tedious and error-prone, so this project aims to eliminate the grunt work.

## The Solution

**Natural Reflection → AI-Powered Sync**

Write your weekly reflection and main adjustments in your personal notes, then paste into Claude Code/Desktop (or interactively chat). MCP servers handle the rest.

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
│  Notion DB  │ │ TickTick API│ │ Sheets API │
│(PACT Data)  │ │   (Tasks)   │ │  (Tracker) │
└─────────────┘ └─────────────┘ └────────────┘
```

### Neat Features (via LLM integration)

- **Real-Time Feedback**
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

- **Iterate Naturally**
   - "Actually, make Sleep PACT 4x/week instead"
   - "Show me the TickTick description for Application Writing"
   - Claude adjusts in real-time


## PACT Structure

See `examples/` for examples of how each might look (with the provided CLAUDE.md file)


### Configuration Files

See `connection_instructions.md`.

## Usage

### Common Commands

**After pasting your Apple Notes reflection:**
- "Update all platforms based on these notes"
- "What changes did you identify?"
- "Show me what the TickTick task looks like before updating"
- "Actually, make that 3 weeks instead of 2"
- "What PACTs are currently active in Notion?"
- "Pause the [PACT name] PACT for now"

## Design Principles

A lot of the ideas here are based on the book, but more generally on a design philosophy of building tools that extends the human interface with technology using a more natural medium, while still allowing the core reflections to be made by the individual. See the blog post for more details.

1. **Reflect naturally, sync automatically**: Write your thoughts in Apple Notes where you already reflect. Paste once, Claude handles propagating changes across all platforms through conversational AI.
2. **Preserve > Generate**: Keep existing content, only change what's needed. TickTick task structure and motivational text stays intact.
3. **Natural language → Structured data**: Claude interprets your free-form reflections and translates them into structured updates across Notion (database), TickTick (tasks), and Sheets (tracking). No manual data entry.
4. **Safety first**: Claude shows what it's changing before applying. You can iterate and refine in real-time.
5. **Minimal effort**: Weekly reviews should be ≤1 hour of meaningful reflection, not frustrating cross-platform data entry.

## Potential Enhancements

- **Completion analytics**: "Show me my PACT completion trends over the last month"
- **Automated weekly prompts**: Claude asks reflection questions based on your PACTs
- **Rollback capability**: "Undo my last weekly review changes"
