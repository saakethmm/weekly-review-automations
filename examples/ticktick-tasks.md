# TickTick Task Examples

These examples show how PACT tasks are structured in TickTick.

---

## Example 1: Daily Reading PACT

**Task Name:** Reading (≥20 pages)

```
## Tasks
- [ ] Pick up book
- [ ] Read ≥20 pages
- [ ] Note any highlights

Start small if low energy - even 5 pages counts.

(adapt order/tasks needed based on time/energy)

---
## Guidelines
Reading compounds over time. 20 pages/day = 30+ books/year.
Pick fiction or non-fiction based on mood.
```

**Recurrence:** `RRULE:FREQ=DAILY`

---

## Example 2: Weekly Review PACT

**Task Name:** Weekly Review (reflect + plan)

```
## Tasks
- [ ] Review completed tasks from past week
- [ ] Check PACT tracker completion rates
- [ ] Identify what worked and what didn't
- [ ] Plan focus areas for upcoming week
- [ ] Update any PACTs that need adjustment

(adapt order/tasks needed based on time/energy)

---
## Guidelines
Block 30-60 min on Sunday. Be honest about what's working.
This is where compounding happens - small adjustments weekly.
```

**Recurrence:** `RRULE:FREQ=WEEKLY;BYDAY=SU`

---

## Example 3: Workday Exercise PACT

**Task Name:** Movement (≥15 min activity)

```
## Tasks
- [ ] Choose activity (walk, gym, yoga, etc.)
- [ ] Complete ≥15 min of movement
- [ ] Log activity if tracking

Any movement counts. Walking is underrated.

(adapt order/tasks needed based on time/energy)

---
## Guidelines
Movement before deep work improves focus.
Low energy? A 15-min walk still counts.
```

**Recurrence:** `RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR`

---

## Example 4: Biweekly Deep Clean PACT

**Task Name:** Deep Clean (one zone)

```
## Tasks
- [ ] Pick one zone (kitchen, bathroom, desk, etc.)
- [ ] Declutter surfaces
- [ ] Wipe down / scrub as needed
- [ ] Take out trash/recycling

(adapt order/tasks needed based on time/energy)

---
## Guidelines
Rotate zones each session. Don't try to do everything.
15-30 min focused cleaning > 2 hrs of scattered effort.
```

**Recurrence:** `RRULE:FREQ=WEEKLY;INTERVAL=2`

---

## Task Structure Reference

```
Task Name: [PACT Name] ([Action summary])

## Tasks
- [ ] [Specific actionable item]
- [ ] [Additional items as needed]

[Any reminders or notes]

(adapt order/tasks needed based on time/energy)

---
## Guidelines
(optional) [Instructions for completing the task]
(optional) [Motivational context]
```
