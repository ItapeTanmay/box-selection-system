from django.core.exceptions import ObjectDoesNotExist
from .models import Box


class NoSuitableBoxError(Exception):
    """Custom exception raised when no box can fit the given product and quantity."""
    pass


def find_best_box(product, quantity):
    """
    Given a Product instance and a quantity, return the single most suitable Box
    (lowest cost that fits all dimensions and total weight).
    Raises NoSuitableBoxError if no box fits.
    """
    total_weight = product.weight * quantity

    # 1. Filter boxes that can hold the product dimensions and total weight
    fitting_boxes = Box.objects.filter(
        internal_length__gte=product.length,
        internal_width__gte=product.width,
        internal_height__gte=product.height,
        max_weight__gte=total_weight,
    ).order_by('cost')  # 2. Cheapest box first

    # 3. Return the best match or raise an error
    best_box = fitting_boxes.first()
    if best_box is None:
        raise NoSuitableBoxError(
            f"No box can fit '{product.name}' x{quantity}. "
            f"Product dimensions: {product.length}x{product.width}x{product.height} cm, "
            f"total weight: {total_weight} kg."
        )

    return best_box