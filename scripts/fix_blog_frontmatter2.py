import os
import re
from pathlib import Path

BLOG_DIR = Path("/root/bit-ml-new-website/content/blog")

for p in BLOG_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    # Check if the frontmatter is missing the closing ---
    if content.startswith("---") and "---" not in content[3:]:
        # It's missing the closing ---
        # Let's find the first <div> and put --- before it
        idx = content.find("<div")
        if idx != -1:
            content = content[:idx] + "---\n\n" + content[idx:]
            
            # Also add cover if we find an image
            match = re.search(r'<img[^>]*src="([^"]+)"', content)
            if match:
                img_src = match.group(1)
                content = content.replace("type: blog\n---", f"type: blog\ncover:\n  image: {img_src}\n---")
                
            with open(p, "w") as f:
                f.write(content)
