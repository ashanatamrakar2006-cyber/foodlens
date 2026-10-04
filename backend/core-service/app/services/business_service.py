from math import asin, cos, radians, sin, sqrt

from app.mock.data import businesses


def distance_km(lat1, lng1, lat2, lng2):
    r = 6371
    d_lat = radians(lat2 - lat1)
    d_lng = radians(lng2 - lng1)
    a = sin(d_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lng / 2) ** 2
    return 2 * r * asin(sqrt(a))


def search_businesses(q: str = "", category: str | None = None):
    return [
        b for b in businesses
        if q.lower() in b["name"].lower() and (not category or b["category"] == category)
    ]


def get_business(business_id: str):
    return next((b for b in businesses if b["id"] == business_id), None)


def nearby_businesses(lat: float, lng: float, radius: float):
    result = []
    for b in businesses:
        d = round(distance_km(lat, lng, b["lat"], b["lng"]), 2)
        if d <= radius:
            result.append({**b, "distanceKm": d})
    return sorted(result, key=lambda x: x["distanceKm"])