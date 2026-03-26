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
            with open(p, "w") as f:
                f.write(content)
