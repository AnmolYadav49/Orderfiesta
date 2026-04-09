import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orderista_core.settings')
django.setup()

from canteen.models import MenuItem
from accounts.models import CustomUser

# Create a canteen user if none exists
canteen_user, _ = CustomUser.objects.get_or_create(username='canteen_admin', defaults={'role': 2})

foods = [
    # North Indian
    ("Butter Chicken", "Rich and creamy tomato gravy with tender chicken.", 12.99, "North Indian"),
    ("Paneer Tikka Masala", "Cottage cheese cubes in a spicy curry.", 10.99, "North Indian"),
    ("Dal Makhani", "Slow-cooked black lentils with butter and cream.", 9.49, "North Indian"),
    ("Garlic Naan", "Soft flatbread topped with garlic and cilantro.", 3.99, "North Indian"),
    ("Chole Bhature", "Spicy chickpea curry with fried bread.", 8.99, "North Indian"),
    ("Rogan Josh", "Classic Kashmiri lamb curry.", 14.99, "North Indian"),
    ("Palak Paneer", "Fresh spinach curry with cottage cheese.", 10.49, "North Indian"),
    # South Indian
    ("Masala Dosa", "Crispy rice crepe filled with spiced potatoes.", 8.99, "South Indian"),
    ("Idli Sambar", "Steamed rice cakes served with lentil soup.", 6.99, "South Indian"),
    ("Medu Vada", "Deep fried lentil donuts.", 5.99, "South Indian"),
    ("Uttapam", "Thick savory pancake with onions and tomatoes.", 7.49, "South Indian"),
    ("Chicken Chettinad", "Fiery and aromatic South Indian chicken curry.", 13.49, "South Indian"),
    ("Lemon Rice", "Tangy and flavorful rice tempered with spices.", 6.49, "South Indian"),
    # Chinese
    ("Hakka Noodles", "Wok-tossed noodles with fresh vegetables.", 9.99, "Chinese"),
    ("Manchurian Dry", "Crispy veggie balls in a dark soy garlic sauce.", 10.49, "Chinese"),
    ("Chilli Chicken", "Spicy Indo-Chinese chicken appetizer.", 11.99, "Chinese"),
    ("Fried Rice", "Classic vegetable fried rice.", 8.99, "Chinese"),
    ("Spring Rolls", "Crispy rolls stuffed with mixed vegetables.", 6.49, "Chinese"),
    ("Sweet Corn Soup", "Comforting classic Chinese soup.", 5.49, "Chinese"),
    # Beverages
    ("Mango Lassi", "Sweet and creamy yogurt-based mango drink.", 4.99, "Beverages"),
    ("Masala Chai", "Indian spiced tea with milk.", 2.99, "Beverages"),
    ("Cold Coffee", "Chilled coffee blended with ice and cream.", 5.49, "Beverages"),
    ("Mojito Virgin", "Refreshing mint and lime mocktail.", 6.99, "Beverages"),
    ("Fresh Lime Soda", "Sweet and salted lime drink.", 3.99, "Beverages"),
    ("Iced Tea", "Classic lemon iced tea.", 4.49, "Beverages"),
]

MenuItem.objects.all().delete() # clear old

for name, desc, price, cuisine in foods:
    MenuItem.objects.create(
        name=name, description=desc, price=price, cuisine=cuisine, canteen=canteen_user, customizable=True
    )
print("Seeding complete! Added", len(foods), "items.")
