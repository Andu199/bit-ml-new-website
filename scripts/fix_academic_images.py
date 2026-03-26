import os
import re
from pathlib import Path

NEWS_DIR = Path("/root/bit-ml-new-website/content/news")

for p in NEWS_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    if "type: academic" in content and "cover:" not in content:
        # Find the first image in the content
        match = re.search(r'!\[.*?\]\((.*?)\)', content)
        if match:
            img_src = match.group(1)
            # Add to frontmatter
            content = content.replace("type: academic\n", f"type: academic\ncover:\n  image: {img_src}\n")
            with open(p, "w") as f:
                f.write(content)
