import os
import re
from pathlib import Path

BLOG_DIR = Path("/root/bit-ml-new-website/content/blog")

for p in BLOG_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    # Extract the first image
    match = re.search(r'<img[^>]*src="([^"]+)"', content)
    if match:
        img_src = match.group(1)
        # Add to frontmatter
        if "cover:" not in content:
            content = content.replace("---\n\n", f"---\ncover:\n  image: {img_src}\n---\n\n")
            with open(p, "w") as f:
                f.write(content)
