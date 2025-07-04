class ShippingService:
    def __init__(self, products):
        self.products = products  # List of shippable items

    def generate_shipping_notice(self):
        print(" --- Shipment notice : ---")

        summary = {}
        total_weight = 0.0

        for item in self.products:
            name = item.get_name()
            weight = item.get_weight()
            total_weight += weight

            if name not in summary:
                summary[name] = {
                    "count": 1,
                    "unit_weight": weight
                }
            else:
                summary[name]["count"] += 1

        # Print summary for each product type
        for name, info in summary.items():
            weight_str = f"{info['unit_weight']}kg" if info['unit_weight'] < 1 else f"{info['unit_weight']:.0f}kg"
            print(f"{info['count']}x {name} {weight_str}")

        print(f"Total package weight {total_weight:.1f}kg")
        return total_weight