import os
import re
from pathlib import Path

BLOG_DIR = Path("/root/bit-ml-new-website/content/blog")

for p in BLOG_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    # Remove the header navigation
    content = re.sub(r'<header><nav.*?</nav></header>', '', content, flags=re.DOTALL)
    
    # Remove the "Back Home" link and date block
    content = re.sub(r'<div class="Post__PostHeader[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    
    # Remove the title h1 since Hugo renders it
    content = re.sub(r'<h1>.*?</h1>', '', content, count=1)
    
    # Remove the cover image div since we'll use frontmatter
    content = re.sub(r'<div class="Post__CoverImg[^>]*></div>', '', content)
    
    with open(p, "w") as f:
        f.write(content)
