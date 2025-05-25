from flask import Flask, render_template
import os

app = Flask(__name__)

# Sample cosmetics data
cosmetics_data = [
    {
        'id': 1,
        'name': 'Matte Lipstick - Ruby Red',
        'price': 24.99,
        'image': 'https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400&h=400&fit=crop',
        'description': 'Long-lasting matte lipstick with intense color payoff',
        'category': 'Lips'
    },
    {
        'id': 2,
        'name': 'Foundation - Natural Glow',
        'price': 35.50,
        'image': 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400&h=400&fit=crop',
        'description': 'Full coverage liquid foundation for all skin types',
        'category': 'Face'
    },
    {
        'id': 3,
        'name': 'Eyeshadow Palette - Sunset',
        'price': 42.00,
        'image': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400&h=400&fit=crop',
        'description': '12-shade eyeshadow palette with warm sunset tones',
        'category': 'Eyes'
    },
    {
        'id': 4,
        'name': 'Mascara - Volume Boost',
        'price': 18.75,
        'image': 'https://images.unsplash.com/photo-1631729371254-42c2892f0e6e?w=400&h=400&fit=crop',
        'description': 'Waterproof mascara for dramatic volume and length',
        'category': 'Eyes'
    },
    {
        'id': 5,
        'name': 'Blush - Peachy Keen',
        'price': 22.99,
        'image': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400&h=400&fit=crop',
        'description': 'Natural-looking powder blush in a peachy pink shade',
        'category': 'Face'
    },
    {
        'id': 6,
        'name': 'Lip Gloss - Crystal Clear',
        'price': 16.50,
        'image': 'https://images.unsplash.com/photo-1583241800020-494ec2180ec4?w=400&h=400&fit=crop',
        'description': 'High-shine lip gloss with moisturizing formula',
        'category': 'Lips'
    }
] # WhatsApp configuration
WHATSAPP_NUMBER = "1234567890"  # Replace with your WhatsApp business number

def generate_whatsapp_url(product_name, price):
    message = f"Hi! I'm interested in purchasing {product_name} for ${price}. Can you help me with the order?"
    encoded_message = message.replace(' ', '%20').replace('\n', '%0A')
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"

@app.route('/')
def index():
    products_with_whatsapp = []
    for product in cosmetics_data:
        product_copy = product.copy()
        product_copy['whatsapp_url'] = generate_whatsapp_url(product['name'], product['price'])
        products_with_whatsapp.append(product_copy)
    
    return render_template('index.html', products=products_with_whatsapp)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in cosmetics_data if p['id'] == product_id), None)
    if not product:
        # For a more robust app, consider rendering a dedicated 404 page here.
        # For now, a simple text response is fine.
        return "Product not found", 404
    
    product_copy = product.copy()
    product_copy['whatsapp_url'] = generate_whatsapp_url(product['name'], product['price'])
    
    # Render the new product_detail.html template, passing only the single product
    return render_template('product_detail.html', product=product_copy)

if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # For production, use a proper WSGI server like Gunicorn:
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app