#  Fawry Rise Journey – E-commerce System

A console-based E-commerce simulation system, developed for the **Fawry Rise / Quantum Full Stack Development Internship Challenge**.

---

##  Features
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

##  Project Structure

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

##  Getting Started

1. Make sure **Python 3.8+** is installed.
2. Clone or download the repository.
3. Run the entry script:

   ```bash
   python main.py
   ```

---

##  Sample Scenario (`main.py`)

```python
cart.add_item(cheese, 2)
cart.add_item(tv, 1)
cart.add_item(scratch_card, 1)
cart.add_item(biscuits, 1)
checkout(customer, cart)
```

### 🖨 Example Console Output

```
Added 2x Cheese to cart.
Added 1x TV to cart.
Added 1x Scratch Card to cart.
Added 1x Biscuits to cart.

--- Starting Checkout ---

bassant paid 700 EGP. Remaining balance: 300 EGP.
Shipment notice :
2x Cheese 400g
1x TV 5kg
1x Biscuits 700g
Total package weight 6.1kg

Checkout receipt :
2x Cheese 200
1x TV 300
1x Scratch Card 50
1x Biscuits 150
----------------------
Subtotal 700
Shipping 40
Amount 740

Checkout complete. Thanks for shopping!
```

---

##  Edge Cases Handled

* ✅ Expired products are not added to the cart
* ✅ Cannot add more than available quantity
* ✅ Checkout fails if cart is empty
* ✅ Checkout fails if customer balance is insufficient
* ✅ Shipping fee only applies to shippable items

---

##  Notes

* Follows clean **Object-Oriented Design** practices
* Uses **duck typing** for shippable items (`get_name()` and `get_weight()`)
* Console output format fully matches challenge requirements

---

## Developer

**Bassant Hossam**
*Fawry Full Stack Internship Challenge – 2025*

---
