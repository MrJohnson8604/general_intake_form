"""
Generate a 1200x630 social media card for Fortiz Group
This script creates an optimized Open Graph/Twitter card image
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
OUTPUT_PATH = "assets/img/fortiz-social-card.png"
LOGO_PATH = "assets/img/Fortiz-Group-Logo.png"
WIDTH = 1200
HEIGHT = 630

# Background: now plain white per request
BACKGROUND_COLOR = "#ffffff"

def create_social_card():
    """Create a 1200x630 social media card"""
    
    # Create base image (solid white)
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Load and resize logo
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH)
        
        # Convert to RGBA if needed
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Resize logo to fit nicely (max 600px wide now for more presence)
        logo_max_width = 600
        aspect_ratio = logo.height / logo.width
        new_width = min(logo.width, logo_max_width)
        new_height = int(new_width * aspect_ratio)
        logo = logo.resize((new_width, new_height), Image.LANCZOS)
        
        # Calculate position (centered horizontally, upper third vertically)
        logo_x = (WIDTH - new_width) // 2
        # Center vertically (with slight upward bias ~10%)
        logo_y = int((HEIGHT - new_height) * 0.40)
        
        # Paste logo with transparency
        img.paste(logo, (logo_x, logo_y), logo)
        
        # No text; keep for potential future additions
        text_y = None
    else:
        print(f"Warning: Logo not found at {LOGO_PATH}")
        text_y = 200
    
    # Removed all text & decorative elements per request.
    
    # Save the image
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    img.save(OUTPUT_PATH, 'PNG', optimize=True)
    print(f"✓ Social card created successfully: {OUTPUT_PATH}")
    print(f"  Size: {WIDTH}x{HEIGHT}px")
    print(f"  File size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")

if __name__ == "__main__":
    create_social_card()
