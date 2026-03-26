import os
import re
from pathlib import Path

BLOG_DIR = Path("/root/bit-ml-new-website/content/blog")

for p in BLOG_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    # Fix the double --- issue
    if "---\ncover:\n  image:" in content:
        # Remove the extra --- block
        content = re.sub(r'---\ncover:\n  image: (.*?)\n---\n\n', '', content)
        
        # Insert cover into the main frontmatter
        match = re.search(r'<img[^>]*src="([^"]+)"', content)
        if match:
            img_src = match.group(1)
            content = content.replace("type: blog\n---", f"type: blog\ncover:\n  image: {img_src}\n---")
            
        with open(p, "w") as f:
            f.write(content)
