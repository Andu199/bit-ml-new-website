import urllib.request
from bs4 import BeautifulSoup
import re
import os
import shutil
from pathlib import Path
from urllib.parse import urljoin, quote
from datetime import datetime

base_url = "https://bit-ml.github.io/"
req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

blog_links = []
for a in soup.find_all('a', href=True):
    if 'blog' in a['href'] and a['href'] not in blog_links:
        blog_links.append(a['href'])

print(f"Found {len(blog_links)} blog links")

out_dir = Path("/root/bit-ml-new-website/content/blog")
out_dir.mkdir(parents=True, exist_ok=True)

for link in blog_links:
    full_url = urljoin(base_url, link)
    print(f"Fetching {full_url}")
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        page_html = urllib.request.urlopen(req).read()
        page_soup = BeautifulSoup(page_html, 'html.parser')
        
        title_elem = page_soup.find('h1')
        if not title_elem:
            continue
        title = title_elem.get_text(strip=True)
        
        date_elem = page_soup.find('time') or page_soup.find('span', class_='date')
        date_str = "2020-01-01"
        if date_elem:
            date_str = date_elem.get_text(strip=True)
            # Try to parse date, if fails, use default
            try:
                date_obj = datetime.strptime(date_str, "%B %d, %Y")
                date_str = date_obj.strftime("%Y-%m-%d")
            except:
                pass
                
        slug = link.strip('/').split('/')[-1]
        if not slug or slug == 'blog':
            continue
            
        post_dir = out_dir / slug
        post_dir.mkdir(exist_ok=True)
        
        content_elem = page_soup.find('article') or page_soup.find('div', class_='content')
        if not content_elem:
            continue
            
        # Download images
        for img in content_elem.find_all('img'):
            img_src = img.get('src')
            if img_src:
                img_url = urljoin(full_url, img_src)
                img_name = img_src.split('/')[-1]
                img_path = post_dir / img_name
                try:
                    # encode url
                    encoded_url = quote(img_url, safe=':/')
                    req = urllib.request.Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    img['src'] = img_name
                except Exception as e:
                    print(f"Failed to download {img_url}: {e}")
                    
        md_content = f"""---
title: "{title}"
date: {date_str}
type: blog
---

{content_elem.encode_contents().decode('utf-8')}
"""
        with open(post_dir / "index.md", "w") as f:
            f.write(md_content)
            
    except Exception as e:
        print(f"Failed to process {full_url}: {e}")

