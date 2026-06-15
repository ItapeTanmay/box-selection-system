(venv) PS D:\LinkCode\Python\Django Projects\box_selection_system> python manage.py test boxes --verbosity=2
Found 5 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, boxes, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying boxes.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_exact_fit_cheapest_selected (boxes.tests.BoxRecommendationTests.test_exact_fit_cheapest_selected)
Book x2 = 1.0kg fits Tiny Box exactly; must be cheapest (₹40). ... ok
test_fit_with_margin_and_weight_upgrade (boxes.tests.BoxRecommendationTests.test_fit_with_margin_and_weight_upgrade)
Book x3 = 1.5kg exceeds Tiny's max_weight (1.0). Standard (₹60) fits. ... ok
test_multiple_boxes_cheapest_selected (boxes.tests.BoxRecommendationTests.test_multiple_boxes_cheapest_selected)
Medium Toy 30x20x10, 1.2kg (qty=1). ... ok
test_no_box_fits (boxes.tests.BoxRecommendationTests.test_no_box_fits)
Large Lamp x3 = 15kg; no box supports that weight. ... ok
test_weight_margin_exact_fit (boxes.tests.BoxRecommendationTests.test_weight_margin_exact_fit)
Large Lamp x2 = 10kg fits Heavy Box exactly (max 10). ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.008s

OK


📋 Test Cases Summary
======================================================================
| #   | Test Name                                     | Result     |
----------------------------------------------------------------------
| 1   | test_exact_fit_cheapest_selected              | ✅ Pass     |
| 2   | test_fit_with_margin_and_weight_upgrade       | ✅ Pass     |
| 3   | test_multiple_boxes_cheapest_selected         | ✅ Pass     |
| 4   | test_no_box_fits                              | ✅ Pass     |
| 5   | test_weight_margin_exact_fit                  | ✅ Pass     |
======================================================================
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
(venv) PS D:\LinkCode\Python\Django Projects\box_selection_system> 