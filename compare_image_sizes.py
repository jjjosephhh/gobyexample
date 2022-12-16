import os
from constants import urls, dest_dir

original_paths = [os.path.join("gobyexample", url.split("/").pop() + ".png") for url in urls]
compressed_paths = [os.path.join(dest_dir, url.split("/").pop() + ".webp") for url in urls]

for original, compressed in zip(original_paths, compressed_paths):
  original_name = original.split('/').pop()
  compressed_name = compressed.split('/').pop()

  original_size = os.path.getsize(original)
  compressed_size = os.path.getsize(compressed)

  print(original_name, original_size)
  print('\t--->', compressed_name, compressed_size)