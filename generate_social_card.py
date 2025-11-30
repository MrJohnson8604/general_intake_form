"""
Generate a 1200x630 social media card for Fortiz Group
This script creates an optimized Open Graph/Twitter card image
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
OUTPUT_PATH = "assets/img/fortiz-social-card.png"
LOGO_PATH = "assets/img/fortiz-group-logo.png"
WIDTH = 1200
HEIGHT = 630

# Brand colors (adjust to match your brand)
BACKGROUND_COLOR = "#1a4d3e"  # Dark teal/green
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#3d9970"  # Lighter teal

def create_social_card():
    """Create a 1200x630 social media card"""
    
    # Create base image with gradient-like effect
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Add subtle gradient overlay
    for i in range(HEIGHT):
        alpha = int(30 * (i / HEIGHT))
        color = f"#{hex(int(ACCENT_COLOR[1:3], 16) - alpha)[2:].zfill(2)}{hex(int(ACCENT_COLOR[3:5], 16) - alpha)[2:].zfill(2)}{hex(int(ACCENT_COLOR[5:7], 16) - alpha)[2:].zfill(2)}"
        try:
            draw.line([(0, i), (WIDTH, i)], fill=color, width=1)
        except:
            pass
    
    # Load and resize logo
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH)
        
        # Convert to RGBA if needed
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Resize logo to fit nicely (max 400px wide, maintaining aspect ratio)
        logo_max_width = 400
        aspect_ratio = logo.height / logo.width
        new_width = min(logo.width, logo_max_width)
        new_height = int(new_width * aspect_ratio)
        logo = logo.resize((new_width, new_height), Image.LANCZOS)
        
        # Calculate position (centered horizontally, upper third vertically)
        logo_x = (WIDTH - new_width) // 2
        logo_y = 120
        
        # Paste logo with transparency
        img.paste(logo, (logo_x, logo_y), logo)
        
        # Add text below logo
        text_y = logo_y + new_height + 40
    else:
        print(f"Warning: Logo not found at {LOGO_PATH}")
        text_y = 200
    
    # Add text
    try:
        # Try to use a nice font
        font_title = ImageFont.truetype("arial.ttf", 52)
        font_subtitle = ImageFont.truetype("arial.ttf", 32)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Main title
    title = "FORTIZ GROUP"
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    draw.text((title_x, text_y), title, fill=TEXT_COLOR, font=font_title)
    
    # Subtitle
    subtitle = "Funding, Credit & Real Estate Solutions"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (WIDTH - subtitle_width) // 2
    draw.text((subtitle_x, text_y + 70), subtitle, fill=TEXT_COLOR, font=font_subtitle)
    
    # Add decorative line
    line_y = text_y + 140
    line_margin = 300
    draw.line([(line_margin, line_y), (WIDTH - line_margin, line_y)], fill=ACCENT_COLOR, width=3)
    
    # Save the image
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    img.save(OUTPUT_PATH, 'PNG', optimize=True)
    print(f"✓ Social card created successfully: {OUTPUT_PATH}")
    print(f"  Size: {WIDTH}x{HEIGHT}px")
    print(f"  File size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")

if __name__ == "__main__":
    create_social_card()
