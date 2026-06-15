# AI Usage Documentation

## 1. Which AI Tool(s) I Used
- **ChatGPT/Claude** – used as a coding mentor throughout the assignment.

## 2. How I Used the AI
I followed a step-by-step approach with the AI, asking for guidance and code snippets for each feature. However, I never copied any code blindly. I treated every piece of AI output as a starting point, then **tested, debugged, and improved** it significantly. The final codebase reflects my own understanding and decisions.

## 3. What I Accepted vs. What I Modified
In each step, I accepted the general structure (model fields, view logic, template layout) but made substantial changes:

- **Models:** The AI provided the field definitions. I changed the `cost` field from `FloatField` to `DecimalField`, added `help_text` to every field, and refined the `save()` override to auto-calculate `total_weight`.
- **Admin:** I used the AI’s suggested `@admin.register` decorator, then independently added `search_fields`, `list_filter`, `readonly_fields`, and cross-relation search.
- **Box selection logic:** The AI suggested the ORM pattern (`filter(__gte)`, `order_by('cost').first()`). I designed the complete algorithm, wrote the custom exception, and crafted detailed error messages on my own.
- **API endpoint:** The AI pointed me to `get_object_or_404` and `JsonResponse`. I implemented the entire view, including method restriction, robust input validation, JSON structure, and the Decimal serialisation fix.
- **UI form:** I used the AI’s form class and template skeleton as a reference, but then styled with Bootstrap, added inline error display, and fixed the missing URL import completely by myself.
- **Tests:** I used the `setUpTestData` pattern the AI mentioned, but wrote all test scenarios, corrected data access bugs, added docstrings, and added an extra test case.
- **Documentation:** I followed a README outline from the AI, but all content, including this AI_USAGE, was written by me based on my actual work.

## 4. Mistakes the AI Made (and I Fixed)
- Used `FloatField` for monetary `cost` → I switched to `DecimalField`.
- Omitted `readonly_fields` for `total_weight` in admin → I added it.
- Forgot to import `order_ui_view` in `urls.py` → I caught the `NameError` and fixed it.
- Didn't mention that `Decimal` is not JSON‑serialisable → I discovered and fixed that error.
- Test `setUpTestData` incorrectly used `self` instead of `cls` for shared data → I corrected it.

## 5. How I Verified the Final Code
- **Manual testing:** Admin CRUD, UI form (happy path + error cases), API via browser and curl.
- **Automated tests:** `python manage.py test boxes` – all 5 tests pass.
- **Edge cases covered:** Negative quantity, missing params, product not found, exact weight/dimension limits.
- **Code review:** Re‑read every file for clean naming, comments, and consistency.

## 6. Core Logic Statement (As Per Assignment)
The **box recommendation algorithm** is my own work. I defined the rules (dimension check, weight check, cheapest selection) and wrote the final function with custom exception handling. The AI helped only with the specific ORM syntax (`__gte` lookups, ordering), which I then applied and tested independently.
