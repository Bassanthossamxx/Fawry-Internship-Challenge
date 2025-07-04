from services.shipping_service import ShippingService

def checkout(customer, cart):
    # Step 1: Validate cart
    if cart.is_empty():
        raise ValueError("Cart is empty. Please add some products before checkout.")

    subtotal = cart.get_subtotal()
    shippable_items = cart.get_shippable_items()

    # shipping = 20 EGP
    shipping_cost = 20
    total_amount = subtotal + shipping_cost

    # Step 2: Attempt to pay
    try:
        customer.pay(total_amount)
    except ValueError as e:
        raise ValueError(f"Payment failed: {e}")

    # Step 3: If shipping required, call shipping service first
    if shippable_items:
        shipping_service = ShippingService(shippable_items)
        shipping_service.generate_shipping_notice()

    # Step 4: Print receipt
    print("\n --- Checkout receipt : ---")
    for product, quantity in cart.items:
        line_total = product.price * quantity
        print(f"{quantity}x {product.name} {line_total}")
    print("----------------------")
    print(f"Subtotal {subtotal}")
    print(f"Shipping {shipping_cost}")
    print(f"Amount {total_amount}")
    print("----------------------")
    print("\n Checkout complete. Thanks for shopping!")
    return total_amount