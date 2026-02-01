import numpy as np

np.random.seed(10)
gambar_rgb = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)

print("=== Original RGB Image (4x4x3) ===")
print(gambar_rgb)

gambar_grey = np.mean(gambar_rgb, axis=2).astype(np.uint8)

print("\n=== Grayscale Image (4x4) ===")
print(gambar_grey)

bright_grey = np.clip(gambar_grey.astype(np.int16) + 50, 0, 255).astype(np.uint8)

print("\n=== Bright Greyscale ===")
print(bright_grey)

pixel_terang = bright_grey[bright_grey > 200]
print(f"\n* Jumlah pixel sangat terang: {len(pixel_terang)}")
