from app.mock.data import batches, products


def get_product(product_id: str):
    return next((p for p in products if p["id"] == product_id), None)


def create_product(owner_id: str, data: dict):
    if any(p["barcode"] == data["barcode"] for p in products):
        return None, "duplicate_barcode"

    product = {
        "id": str(len(products) + 1),
        "barcode": data["barcode"],
        "name": data["name"],
        "brand": data.get("brand"),
        "ingredients": data.get("ingredients"),
        "allergens": data.get("allergens") or [],
        "ownerId": owner_id,
    }
    products.append(product)
    return product, None


def list_batches(product_id: str):
    if not get_product(product_id):
        return None
    return [b for b in batches if b["productId"] == product_id]