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
    new_path = path.replace("gobyexample", dest_dir).replace(
        ".png", ".webp"
    )
    images.append(new_path)
    im.save(new_path, format='webp', optimize=True, quality=100)

images = '\n'.join([f'<img src="{im}" style="width: 100%; margin: 8px 0;"/>' for im in images])

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
</body>
</html>
"""

if os.path.exists(dest_file):
  os.remove(dest_file)

with open(dest_file, 'w') as f:
  f.write(html_content)
