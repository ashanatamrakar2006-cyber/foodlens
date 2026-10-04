import httpx

OFF_URL = "https://world.openfoodfacts.org/api/v2/product"


async def lookup_barcode(code: str):
    async with httpx.AsyncClient(timeout=8) as client:
        res = await client.get(
            f"{OFF_URL}/{code}.json",
            headers={"User-Agent": "FoodLens/1.0 (student project)"},
        )

    if res.status_code == 404:
        return None
    res.raise_for_status()

    data = res.json()
    if data.get("status") != 1 or not data.get("product"):
        return None

    p = data["product"]
    n = p.get("nutriments", {})
    return {
        "barcode": code,
        "name": p.get("product_name") or None,
        "brand": p.get("brands") or None,
        "quantity": p.get("quantity") or None,
        "imageUrl": p.get("image_front_url") or None,
        "ingredients": p.get("ingredients_text") or None,
        "allergens": p.get("allergens_tags", []),
        "additives": p.get("additives_tags", []),
        "nutrition": {
            "energyKcal100g": n.get("energy-kcal_100g"),
            "sugars100g": n.get("sugars_100g"),
            "salt100g": n.get("salt_100g"),
            "fat100g": n.get("fat_100g"),
            "saturatedFat100g": n.get("saturated-fat_100g"),
            "proteins100g": n.get("proteins_100g"),
        },
        "nutriScore": p.get("nutriscore_grade") or None,
        "source": "openfoodfacts",
        # Member 2 ki AI service yahan assessment bharegi
        "aiAssessment": None,
    }