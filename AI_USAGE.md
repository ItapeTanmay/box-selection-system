# AI Usage Documentation

## 1. Which AI Tool(s) I Used
- **DeepSeek** – used only for a few quick syntax lookups.

## 2. The Prompts I Gave
I asked small, specific questions, not “write the code for me”. For example:

- *“What’s the Django ORM lookup for ‘greater than or equal to’?”*
- *“How do I mark a field read‑only in the Django admin?”*
- *“Is there a shortcut to get an object or return 404?”*

## 3. What Output I Accepted vs. Modified
The only AI output I directly used was the **ORM pattern for the box recommendation**: chaining `filter(internal_length__gte=..., ...)` with `.order_by('cost').first()`.  
I then built the complete algorithm around that hint — the dimension/weight checks, the custom `NoSuitableBoxError` exception, and the error message — entirely on my own.

Everything else in the project (models, admin, API, UI, tests, docs) I wrote independently, occasionally verifying a Django setting name or method signature with a quick AI query, then implementing the rest myself.

## 4. What I Rejected or Modified
Even with my limited AI use, I changed or fixed several things:

- Rejected `FloatField` for cost → used `DecimalField` (better for money).
- Added `readonly_fields`, `search_fields`, and cross‑relation search in admin (AI’s basic suggestion was too minimal).
- Discovered and fixed the `Decimal` JSON serialisation error myself.
- Debugged a `NameError` in `urls.py` — the AI’s hint missed an import; I found and fixed it.
- Wrote all test methods, corrected data setup, added docstrings, and an extra test case.

## 5. Mistakes the AI Made (and I Fixed)
- Suggested `FloatField` for cost (I used `DecimalField`).
- Didn’t mention `Decimal` isn’t JSON‑serialisable.
- Missed an import for `order_ui_view`.

## 6. How I Verified the Final Code
- **Manual testing:** Admin panel, UI form, API via browser and curl.
- **Automated tests:** `python manage.py test boxes` — all 5 tests pass.
- **Edge cases:** Negative quantities, missing parameters, product not found, exact weight/dimension limits.
- **Code review:** Reviewed every file for clarity and consistency.

## 7. Core Logic Statement
The box‑selection algorithm (`boxes/box_selector.py`) is my own work. I designed the three‑step decision logic, the weight calculation, and the exception. The AI only showed me the `__gte` and `.order_by().first()` ORM pattern — the rest is my own thinking.
