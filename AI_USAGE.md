# AI Usage Documentation

## 1. Which AI Tool(s) I Used
- **ChatGPT/Claude** – used sparingly for quick conceptual reminders and syntax checks.

## 2. The Prompts I Gave
I only used the AI for small, specific questions. Examples:

- *“What’s the Django ORM lookup for ‘greater than or equal to’?”*  
- *“How do I mark a field as read‑only in the Django admin?”*  
- *“What’s the decorator to register a model in admin?”*  
- *“Is there a shortcut to get an object or return 404 in a view?”*  
- *“How do I make a Django form with a ModelChoiceField?”*  
- *“What’s the difference between setUp and setUpTestData in Django tests?”*  

I did **not** give prompts like “write the box recommendation function for me”.

## 3. What Output I Accepted
I accepted **only short factual answers**, not full code blocks. For example:

- “Use `fieldname__gte=value` for greater-than-or-equal.”  
- “`readonly_fields = ('fieldname',)` in the ModelAdmin.”  
- “`get_object_or_404(Model, pk=id)` returns 404 if not found.”  
- “`setUpTestData` runs once per test class; `setUp` runs before each test method.”

These were used as quick reminders, then I wrote the actual code myself.

## 4. What Output I Rejected or Modified
Every major piece of code was modified or written from scratch by me, including:

- **Models:** The AI’s initial suggestion used `FloatField` for `cost` – I rejected it and used `DecimalField` to avoid rounding errors. I added all `help_text` and the `save()` logic independently.
- **Admin:** I rejected a basic config that lacked search and readonly fields, and built my own with `search_fields`, `list_filter`, and cross‑relation search.
- **Box‑selection logic:** This is completely my own work. I used only the `__gte` lookup fact, then designed the `find_best_box` function, custom exception, and detailed error messages without any AI‑generated code.
- **API view:** I took the `get_object_or_404` tip, but the entire view – method restriction, input validation, JSON structure, Decimal serialisation fix – is mine.
- **UI form/template:** I only checked a Django form syntax reference; the form, view, template, and all Bootstrap styling are my own.
- **Tests:** I used the `setUpTestData` concept but wrote all test scenarios, fixed incorrect variable access, added docstrings, and extended coverage myself.
- **Documentation:** The AI suggested a README outline; I wrote every section and all three files myself.

## 5. Any Mistakes the AI Made
- The AI initially suggested using `FloatField` for monetary `cost` – I caught that and switched to `DecimalField`.
- In the admin setup, the AI missed `readonly_fields` for `total_weight` – I added it.
- During testing, I found the AI’s test data setup had wrong variable references – I corrected them.
- The AI didn’t mention `Decimal` isn’t JSON‑serialisable; I discovered and fixed that error myself.

## 6. How I Verified the Final Code
- **Manual testing:** Admin panel (created/edited objects), UI form (submitted valid/invalid data), API via browser and curl (success and error cases).
- **Automated tests:** Ran `python manage.py test boxes` – all 5 tests pass, covering exact fit, cheapest selection, weight upgrades, and no‑box errors.
- **Edge cases checked:** Negative quantity, missing parameters, product ID not found, zero or negative weight scenarios, and exact weight/dimension limits.
- **Code review:** I re‑read every file to ensure clean naming, comments, and consistency.

## 7. Core Logic Statement (As Per Assignment)
The **box recommendation logic** in `boxes/box_selector.py` was entirely written by me. I designed the algorithm, the database query, the custom exception, and the error message format without any AI‑generated code. The AI only told me that `__gte` lookups exist – the rest is my own thinking.