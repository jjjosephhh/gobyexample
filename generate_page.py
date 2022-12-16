import os
import shutil
from PIL import Image
from constants import urls, dest_dir, dest_file

paths = [os.path.join("gobyexample", url.split("/").pop() + ".png") for url in urls]

if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
  shutil.rmtree(dest_dir)
os.mkdir(dest_dir)

images = []
for path in paths:
    im = Image.open(path)
    path = path.replace("gobyexample", dest_dir)
    path = path.replace(".png", ".webp")
    images.append(path.replace('docs', '.'))
    im.save(path, format='webp', optimize=True, quality=100)

images = '\n'.join([f'<img src="{im}" style="width: 100%;"/>' for im in images])

zines_dirs = ['debugging', 'networking', 'perf', 'strace', 'tcpdump', 'wizard']
zines_dirs = [os.path.join('docs', 'zines-staging', x) for x in zines_dirs]
zines_files = [os.path.join(x, y).replace('docs', '.') for x in zines_dirs for y in sorted(os.listdir(x)) if '.webp' in y]
zines_files = '\n'.join([f'<img src="{im}" style="width: 100%;"/>' for im in zines_files])

scripts = """
<script>
  function pageScroll() {
    window.scrollBy(0, 0.5);
    scrolldelay = setTimeout(pageScroll, 30);
  }
  window.onload = function() {
    pageScroll();
  }
</script>
"""
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body style="padding: 16px;">
{images}
{zines_files}
{scripts}
</body>
</html>
"""

if os.path.exists(dest_file):
  os.remove(dest_file)

with open(dest_file, 'w') as f:
  f.write(html_content)
