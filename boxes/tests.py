from django.test import TestCase
from .models import Product, Box
from .box_selector import find_best_box, NoSuitableBoxError


class BoxRecommendationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create products
        cls.small_book = Product.objects.create(
            name="Small Book", length=20, width=15, height=5, weight=0.5
        )
        cls.medium_toy = Product.objects.create(
            name="Medium Toy", length=30, width=20, height=10, weight=1.2
        )
        cls.large_lamp = Product.objects.create(
            name="Large Lamp", length=50, width=40, height=30, weight=5.0
        )

        # Create boxes
        cls.tiny_box = Box.objects.create(
            name="Tiny Box",
            internal_length=25, internal_width=20, internal_height=8,
            max_weight=1.0, cost=40.00
        )
        cls.standard_box = Box.objects.create(
            name="Standard Box",
            internal_length=35, internal_width=25, internal_height=12,
            max_weight=3.0, cost=60.00
        )
        cls.large_box = Box.objects.create(
            name="Large Box",
            internal_length=55, internal_width=45, internal_height=35,
            max_weight=6.0, cost=100.00
        )
        cls.heavy_box = Box.objects.create(
            name="Heavy Box",
            internal_length=55, internal_width=45, internal_height=35,
            max_weight=10.0, cost=120.00
        )

    def test_exact_fit_cheapest_selected(self):
        """Book x2 = 1.0kg fits Tiny Box exactly; must be cheapest (₹40)."""
        box = find_best_box(self.small_book, quantity=2)
        self.assertEqual(box, self.tiny_box)

    def test_fit_with_margin_and_weight_upgrade(self):
        """Book x3 = 1.5kg exceeds Tiny's max_weight (1.0). Standard (₹60) fits."""
        box = find_best_box(self.small_book, quantity=3)
        self.assertEqual(box, self.standard_box)

    def test_multiple_boxes_cheapest_selected(self):
        """
        Medium Toy 30x20x10, 1.2kg (qty=1).
        Tiny: length 25 < 30 → fails dimensions.
        Standard (₹60) and Large (₹100) both fit; cheapest (Standard) wins.
        """
        box = find_best_box(self.medium_toy, quantity=1)
        self.assertEqual(box, self.standard_box)

    def test_no_box_fits(self):
        """Large Lamp x3 = 15kg; no box supports that weight."""
        with self.assertRaises(NoSuitableBoxError):
            find_best_box(self.large_lamp, quantity=3)

    def test_weight_margin_exact_fit(self):
        """Large Lamp x2 = 10kg fits Heavy Box exactly (max 10)."""
        box = find_best_box(self.large_lamp, quantity=2)
        self.assertEqual(box, self.heavy_box)