import os
import re
from pathlib import Path

NEWS_DIR = Path("/root/bit-ml-new-website/content/news")

for p in NEWS_DIR.glob("*/index.md"):
    with open(p, "r") as f:
        content = f.read()
    
    if "type: academic" in content and "research_direction:" not in content:
        # Determine direction based on content
        direction = "generalization"
        lower_content = content.lower()
        if "deepfake" in lower_content:
            direction = "deepfake"
        elif "language" in lower_content or "nlp" in lower_content or "molecule" in lower_content or "code" in lower_content:
            direction = "nlp"
        elif "reinforcement" in lower_content or "rl" in lower_content:
            direction = "rl"
            
        # Insert research_direction
        content = content.replace("type: academic\n", f"type: academic\nresearch_direction: {direction}\n")
        
        with open(p, "w") as f:
            f.write(content)
