from app.mock.data import businesses


def create_business(owner_id: str, data: dict):
    business = {
        "id": str(len(businesses) + 1),
        "name": data["name"],
        "category": data["category"],
        "lat": data["lat"],
        "lng": data["lng"],
        "rating": 0,
        "ownerId": owner_id,
        "claimed": True,
    }
    businesses.append(business)
    return business


def claim_business(business_id: str, owner_id: str):
    b = next((x for x in businesses if x["id"] == business_id), None)
    if not b:
        return None, "not_found"
    if b.get("ownerId") and b["ownerId"] != owner_id:
        return None, "already_claimed"
    b["ownerId"] = owner_id
    b["claimed"] = True
    return b, None


def update_business(business_id: str, owner_id: str, fields: dict):
    b = next((x for x in businesses if x["id"] == business_id), None)
    if not b:
        return None, "not_found"
    if b.get("ownerId") != owner_id:
        return None, "forbidden"
    for key, value in fields.items():
        b[key] = value
    return b, None


def get_owned_businesses(owner_id: str):
    return [b for b in businesses if b.get("ownerId") == owner_id]