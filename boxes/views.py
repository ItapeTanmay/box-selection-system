from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from .box_selector import find_best_box, NoSuitableBoxError
from django.shortcuts import render
from .forms import OrderRecommendationForm


def order_ui_view(request):
    form = OrderRecommendationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = OrderRecommendationForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            try:
                box = find_best_box(product, quantity)
                total_weight = product.weight * quantity

                context.update({
                    'result': {
                        'product': product.name,
                        'quantity': quantity,
                        'total_weight': total_weight,
                        'box': {
                            'name': box.name,
                            'dimensions': f"{box.internal_length}x{box.internal_width}x{box.internal_height} cm",
                            'max_weight': box.max_weight,
                            'cost': str(box.cost),
                        }
                    },
                    'success': True,
                })
            except NoSuitableBoxError as e:
                context.update({
                    'error': str(e),
                    'success': False,
                })
    return render(request, 'boxes/order.html', context)


def recommend_box_api(request):
    # Only allow GET
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET method allowed'}, status=405)

    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')

    if not product_id or not quantity:
        return JsonResponse(
            {'error': 'product_id and quantity query parameters are required'},
            status=400
        )

    # Validate quantity is a positive integer
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        return JsonResponse(
            {'error': 'quantity must be a positive integer'},
            status=400
        )

    product = get_object_or_404(Product, pk=product_id)

    try:
        box = find_best_box(product, quantity)
    except NoSuitableBoxError as e:
        return JsonResponse({'error': str(e)}, status=400)

    # Build success response
    data = {
        'product': product.name,
        'quantity': quantity,
        'total_weight': product.weight * quantity,
        'recommended_box': {
            'name': box.name,
            'dimensions': f"{box.internal_length}x{box.internal_width}x{box.internal_height} cm",
            'max_weight': box.max_weight,
            'cost': str(box.cost),   # Decimal must be converted to string for JSON
        }
    }
    return JsonResponse(data)