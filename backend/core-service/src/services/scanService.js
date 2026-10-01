const OFF_URL = 'https://world.openfoodfacts.org/api/v2/product';

// Open Food Facts se product laata hai aur apne format mein badalta hai
export async function lookupBarcode(code) {
  const res = await fetch(`${OFF_URL}/${code}.json`, {
    headers: { 'User-Agent': 'FoodLens/1.0 (student project)' },
    signal: AbortSignal.timeout(8000),
  });

  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`Open Food Facts error: ${res.status}`);

  const data = await res.json();
  if (data.status !== 1 || !data.product) return null;

  const p = data.product;
  return {
    barcode: code,
    name: p.product_name || null,
    brand: p.brands || null,
    quantity: p.quantity || null,
    imageUrl: p.image_front_url || null,
    ingredients: p.ingredients_text || null,
    allergens: p.allergens_tags || [],
    additives: p.additives_tags || [],
    nutrition: {
      energyKcal100g: p.nutriments?.['energy-kcal_100g'] ?? null,
      sugars100g: p.nutriments?.sugars_100g ?? null,
      salt100g: p.nutriments?.salt_100g ?? null,
      fat100g: p.nutriments?.fat_100g ?? null,
      saturatedFat100g: p.nutriments?.['saturated-fat_100g'] ?? null,
      proteins100g: p.nutriments?.proteins_100g ?? null,
    },
    nutriScore: p.nutriscore_grade || null,
    source: 'openfoodfacts',
    // Member 2 ki AI service yahan assessment bharegi (Green/Yellow/Red)
    aiAssessment: null,
  };
}