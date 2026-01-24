# Notion PACT Database Example

This table shows how PACTs are structured in the Notion database.

## Active PACTs

| Name | Action | Frequency | Duration | Next Revisit | Status |
|------|--------|-----------|----------|--------------|--------|
| Reading | ≥20 pages | Daily | 1 month | 2024-02-04 | Active |
| Movement | ≥15 min activity | Daily (workdays) | 2 weeks | 2024-01-28 | Active |
| Weekly Review | Reflect + plan week | Weekly | Ongoing | 2024-02-04 | Active |
| Deep Clean | One zone deep clean | Biweekly | 1 month | 2024-02-04 | Active |
| Application Writing | ≥1 response | Daily (workdays) | 2 weeks | 2024-01-28 | Active |

## Inactive PACTs

| Name | Action | Frequency | Duration | Next Revisit | Status |
|------|--------|-----------|----------|--------------|--------|
| Meditation | ≥10 min session | Daily | - | - | Inactive |
| Journaling | Morning pages | Daily | - | - | Inactive |

## Field Descriptions

- **Name**: Unique identifier for the PACT
- **Action**: Brief description of what to do (include target if measurable)
- **Frequency**: How often - Daily, Daily (workdays), Weekly, Biweekly, 3x/week
- **Duration**: Trial period before review (e.g., "2 weeks", "1 month", "Ongoing")
- **Next Revisit**: Calculated as: last Sunday + duration
- **Status**: Active (being tracked) or Inactive (paused, not deleted)

## Notes

- Inactive PACTs preserve history - they're paused, not deleted
- Duration resets when PACT is modified during a review
- "Ongoing" duration means the habit is established and no longer experimental
