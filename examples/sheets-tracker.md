# Google Sheets PACT Tracker Example

This shows how daily PACT completion is tracked in Google Sheets.

## Tracker Format

| Date | Reading | Movement | Weekly Review | Deep Clean | Application Writing |
|------|---------|----------|---------------|------------|---------------------|
| 2024-01-15 | 1 | 1 | 0 | 0 | 1 |
| 2024-01-16 | 1 | 1 | 0 | 0 | 1 |
| 2024-01-17 | 0 | 1 | 0 | 0 | 0 |
| 2024-01-18 | 1 | 0 | 0 | 0 | 1 |
| 2024-01-19 | 1 | -1 | 0 | 0 | -1 |
| 2024-01-20 | 0 | -1 | 0 | 1 | -1 |
| 2024-01-21 | 1 | -1 | 1 | 0 | -1 |
| 2024-01-22 | 1 | 1 | 0 | 0 | 1 |
| 2024-01-23 | 1 | 1 | 0 | 0 | 0 |

## Value Legend

| Value | Meaning |
|-------|---------|
| `1` | Completed |
| `0` | Not completed |
| `-1` | N/A (not applicable for that day) |

## Structure Notes

- **Column A**: Dates (never modified by automation)
- **Columns B+**: One column per active PACT
- **Row 1**: PACT names as headers
- **Row 2+**: Daily tracking entries

## Operations

| Action | What Happens |
|--------|--------------|
| **New PACT** | New column added after last PACT column |
| **Pause PACT** | Column hidden (data preserved) |
| **Reactivate PACT** | Column unhidden |
| **Pivot PACT** | Old column hidden + new column added |

## Example Insights

From the sample data above:
- **Reading**: 7/9 days (78%) - strong consistency
- **Movement**: 5/7 workdays (71%) - good but room to improve
- **Weekly Review**: 1/1 Sundays (100%) - on track
- **Application Writing**: 4/7 workdays (57%) - may need scope adjustment
