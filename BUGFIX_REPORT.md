# Bugfix Report

This document explains the issues found in the original script and how they were resolved.

---

## Bug 1 — Incorrect variable name

### Problem

The function `calculate_average()` used the variable:

len(number)

However, the correct variable name is `numbers`.

### Error

NameError: name 'number' is not defined

### Fix

Changed:

len(number)

to:

len(numbers)

---

## Bug 2 — Undefined variable

### Problem

The script attempted to categorize the score using:

categorize_score(average_score)

But the variable `average_score` was never defined.

### Error

NameError: name 'average_score' is not defined

### Fix

Replaced with the correct variable:

categorize_score(average)

---

## Bug 3 — Code cleanup

The conditional logic was simplified by removing the unnecessary `else` block in the final return.

Before:

else:
    return "Fail"

After:

return "Fail"

---

## Result

After applying the fixes, the script runs successfully and produces the expected output:

Student scores: [88, 92, 76, 81, 95]  
Average score: 86.4  
Category: Good

---

## Skills Demonstrated

- Python debugging
- Runtime error diagnosis
- Code correction
- Logic cleanup
- Troubleshooting workflow
