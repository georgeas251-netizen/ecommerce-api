import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

#Create Categories
electronics  = Category.objects.create(name='Electronics', description='Electronic devices and gadgets')
clothing = Category.objects.create(name='Clothing', description='Fashion and apparel')
computers = Category.objects.create(name='Computer & AI', description='Computers and AI products')

# Electronics Products
electronics_products = [
    ('iPhone 15', 999.99, 50),
    ('Samsung Galaxy S24', 899.99, 40),
    ('iPad Pro', 1099.99, 30),
    ('AirPods Pro',249.99, 100),
    ('Sony Headphones', 349.99, 60),
    ('Apple Watch', 399.99, 45),
    ('Samsung TV 55"', 799.99, 20),
    ('PlayStation 5', 499.99, 15),
    ('Xbox Series X', 499.99, 15),
    ('Nintendo Switch', 299.99, 35),
    ('Canon Camera', 649.99, 25),
    ('GoPro Hero 12', 399.99, 30),
    ('JBL Speaker', 199.99, 50),
    ('Kindle Paperwhite', 139.99, 70),
    ('Drone DJI Mini', 599.99, 20),
    ('Samrt Doorbell', 149.99, 40),
    ('Fitbit Tracker', 99.99, 60),
    ('Portable Charger', 49.99, 100),
    ('USB-C Hub', 39.99, 80),
    ('Wireless Charger', 29.99, 90),
    ('Smart Bulb Pack', 34.99, 75),
    ('Ring Camera', 179.99,35),
    ('Alexa Echo', 99.99, 55),
    ('Google Nest', 129.99, 45),
    ('Electric Toothbrush', 79.99, 60),
    ('Robot Vaccum', 299.99, 25),
    ('Air Purifier', 199.99, 30),
    ('Smart Scale', 59.99, 50),
    ('Noise Cancelling Earbuds', 179.99, 40),
    ('4K Webcam', 89.99, 65),
]

#Clothing Products
clothing_products = [
    ('Nike Air Max', 129.99, 80),
    ('Adidas Hoodie', 69.99, 100),
    ('Levi Jeans', 59.99, 120),
    ('Puma T-Shirt', 29.99, 150),
    ('Under Armour Shorts', 39.99, 90),
    ('Zara Dress', 79.99, 60),
    ('H&M Jacket', 89.99, 50),
    ('Ralph Lauren Polo', 99.99, 70),
    ('Tommy Hilfiger Cap', 34.99, 110),
    ('Champion Sweatshirt', 49.99, 85),
    ('Reebok Sneakers', 89.99, 75),
    ('New Balance Shoes', 109.99, 65),
    ('Gucci Belt', 299.99, 20),
    ('Ray-Ban Sunglasses', 149.99, 40),
    ('North Face Coat', 199.99, 30),
    ('Patagonia Vest', 129.99, 35),
    ('Lululemon Leggings', 98.99, 55),
    ('Calvin Klein Underwear', 29.99, 200),
    ('Versace Shirt', 189.99, 25),
    ('Burberry Scarf', 249.99, 20),
    ('Wool Socks Pack', 19.99, 95),
    ('Leather Wallet', 44.99, 90),
    ('Swim Trunks', 24.99, 70),
    ('Yoga Mat Bag', 29.99, 110),
    ('Running Belt', 19.99, 95),
    ('Winter Gloves', 24.99, 110),
    ('Beanie Hat', 14.99, 150),
    ('Compression Socks', 17.99, 200),
    ('Gym Bag', 54.99, 65),
]

# Computers & AI Products
computer_products = [
    ('MacBook Pro M3', 1999.99, 20),
    ('Dell XPS 15', 1599.99, 15),
    ('HP Spectre x360', 1399.99, 18),
    ('Lenovo ThinkPad', 1299.99, 22),
    ('ASUS ROG Gaming Laptop', 1799.99, 12),
    ('Razer Blade 15', 2199.99, 10),
    ('Microsoft Surface Pro', 1099.99, 25),
    ('Acer Swift 3', 699.99, 30),
    ('LG gram 16', 1149.99, 18),
    ('Samsung Galaxy Book', 999.99, 20),
    ('NVIDIA RTX 4090', 1599.99, 8),
    ('AMD Ryzen 9 CPU', 499.99, 15),
    ('32GB RAM Kit', 129.99, 40),
    ('2TB NVMe SSD', 149.99, 50),
    ('4K Moniter 27"', 499.99, 25),
    ('Mechanical Keyboard', 149.99, 25),
    ('Gaming Mouse', 79.99, 60),
    ('Mouse Pad XL', 29.99, 80),
    ('Laptop Stand', 39.99, 70),
    ('External SSD 1TB', 99.99, 55),
    ('ChatGPT plus Sub', 20.00, 999),
    ('GitHub Copilot Sub', 10.00, 999),
    ('Raspberry Pi 5', 79.99, 35),
    ('Arduino Starter Kit', 49.99, 45),
    ('AI Camera Module', 89.99, 30),
    ('Python AI Course', 49.99, 999),
    ('Deep Learning Book', 59.99, 100),
    ('USB GPU Accelerator', 199.99, 20),
    ('Smart Home Hub', 129.99, 40),   
]

# Add all products
for name, price, stock in electronics_products:
    Product.objects.create(name=name, category=electronics, price=price, stock=stock, description=f'{name} -Premium quality product')

for name, price, stock in clothing_products:
    Product.objects.create(name=name, category=clothing, price=price, stock=stock, description=f'{name} - Premium quanlity product')

for name, price, stock in computer_products:
    Product.objects.create(name=name, category=computers, price=price, stock=stock, description=f'{name} - Premium quality product')

print('✅ 90 products added successfully!')
print(f'Electronics: {len(electronics_products)} products')
print(f'Clothing: {len(clothing_products)} products')
print(f'Computers & AI: {len(computer_products)} products')