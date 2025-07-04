# Fawry Rise Journey – E-commerce System

A console E-commerce  system, developed for  **Fawry Rise Full Stack Development Internship Challenge**.

---

## Features

* **Product Management**: Define products with name, price, and quantity.
* **Expirable Products**: e.g., Cheese, Biscuits (with expiry validation).
* **Shippable Products**: Include weight (e.g., TV, Cheese).
* **Cart System**:
  * Validates available quantity before adding
  * Skips expired products
  * Calculates subtotal
* **Customer Checkout**:
  * Verifies sufficient balance
  * Generates shipping notice (if needed)
  * Prints a detailed receipt

---

## Project Structure

```
project/
│
├── models/
│   ├── product.py             # Base Product class
│   ├── expirable.py           # Expirable product logic
│   ├── shippable.py           # Shippable (mixin) logic
│   ├── customer.py            # Customer payment logic
│   └── cart.py                # Cart management and validation
│
├── services/
│   ├── shipping_service.py    # ShippingService class
│   └── checkout.py            # Checkout logic
│
└── main.py                    # Entry point and test scenario
```

---

## Getting Started

1. Make sure **Python** is installed.
2. Clone or download the repository.
3. Run the entry script:

   ```bash
   python main.py
   ```

---

## Sample Scenario (`main.py`)

```python
cart.add_item(cheese, 2)
cart.add_item(tv, 1)
cart.add_item(scratch_card, 1)
cart.add_item(biscuits, 1)
checkout(customer, cart)
```

### Example Console Output

```
--- Scenario : Success Checkout ---
Added 2x Cheese to cart.
Added 1x TV to cart.
Added 1x Scratch Card to cart.
Added 1x Biscuits to cart.

Bassant paid 720 EGP. Remaining balance: 280 EGP.

--- Shipment notice : ---
2x Cheese 0.4kg
1x TV 5kg
1x Biscuits 0.7kg
Total package weight 6.5kg

--- Checkout receipt : ---
2x Cheese 200
1x TV 300
1x Scratch Card 50
1x Biscuits 150
----------------------
Subtotal 700
Shipping 20
Amount 720
----------------------

Checkout complete. Thanks for shopping!
```

---

## Edge Cases Handled

### 1. Edge Case: Empty Cart

```
ERROR : empty cart: Cart is empty. Please add some products before checkout.
```

### 2. Edge Case: Expired Product

```
Old Biscuits is expired. Cannot add to cart.
ERROR : expired product: Cart is empty. Please add some products before checkout.
```

### 3. Edge Case: Invalid Balance

```
Added 1x TV to cart.
ERROR : invalid balance: Payment failed: bassant has invalid balance. Needed: 320, Available: 100
```

### 4. Edge Case: Quantity > Available

```
Not enough stock for Cheese. Only 3 left.
```

---

## Notes

* Follows clean **Object-Oriented Design** practices
* Uses **duck typing** for shippable items (`get_name()` and `get_weight()`)
* Console output format fully matches challenge requirements

---

**Bassant Hossam**
*Fawry Full Stack Internship Challenge – 2025*

---
