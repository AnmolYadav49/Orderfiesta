import os
import django
import urllib.request
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orderista_core.settings')
django.setup()
from django.conf import settings
from canteen.models import MenuItem

items = MenuItem.objects.all()
media_dir = os.path.join(settings.BASE_DIR, 'media', 'menu_items')
os.makedirs(media_dir, exist_ok=True)

query_map = {
    'North Indian': 'curry',
    'South Indian': 'dosa',
    'Chinese': 'noodles',
    'Beverages': 'drink'
}

print(f"Begiining to download images for {len(items)} items. This may take a moment...")
for idx, item in enumerate(items):
    # Use the item name directly for much better accuracy
    tag = item.name.replace(' ', ',')
    # Using loremflickr with a lock key to guarantee unique diverse images
    url = f"https://loremflickr.com/600/400/{tag},dish?lock={idx+300}"
    filename = f"food_image_{item.id}.jpg"
    filepath = os.path.join(media_dir, filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        item.image.name = f"menu_items/{filename}"
        item.save()
        print(f"[{idx+1}/{len(items)}] Successfully attached image for '{item.name}'")
        time.sleep(0.4) # polite throttling
    except Exception as e:
        print(f"Failed to download for '{item.name}': {e}")
print("Finished attaching all images!")
