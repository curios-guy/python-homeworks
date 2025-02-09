import numpy as np
from PIL import Image

with Image.open('parrot.jpg') as img:
    img_arr = np.array(img)

# unversal functio for saving images
def save_image(arr, name, mode = "RGB"):
    img = Image.fromarray(arr, mode)
    img.save(f"{name}.jpg")

# for flipping image vertically and horizontally
def flip_image(img):
    # (column, row)
    flipped_hor = img[::-1]
    save_image(flipped_hor, "reversed_horizontally", "RGB")

    flipped_ver = img[:, ::-1]
    save_image(flipped_ver, "reversed_vertically", "RGB")

    divergent = img[::-1, ::-1]
    save_image(divergent, "divergent", "RGB")
# flip_image(img_arr)

# adding noise for image
def add_noise(img, noise_level=30):
    img = np.array(img, dtype=np.int16)  
    noise = np.random.randint(-noise_level, noise_level, img.shape, dtype=np.int16)  
    noisy_img = img + noise 
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    save_image(noisy_img, "noisy_img", "RGB")
    

# brighten image channels with certain value
def brighten_channels(img, channel, value):
    img = np.array(img, dtype = np.int16) 
    img[:, :, channel] += value
    img = np.clip(img, 0, 255).astype(np.uint8)
    save_image(img, "red_extra", "RGB")


# crops 100x100 square ni centre of image and paints it in black
def apply_mask(img):
    img_copy = img.copy()
    c0 = int(((img_copy.shape)[0]-100)/2)
    c1 = c0 + 100
    r0 = int(((img_copy.shape)[1]-100)/2)
    r1 = r0 + 100
    img_copy[c0:c1, r0:r1] = 0
    # previous code, ignore this
    # img[c0:c1, r0:r1, 0] = 0
    # img[c0:c1, r0:r1, 1] = 0
    # img[c0:c1, r0:r1, 2] = 0
    save_image(img_copy, 'blacked')

while True:
    ask = int(input("Welcome\n1. Flip the image\n2. Add random noise\n3. Brighten channels\n4. Apply a Mask\n5. Quit\nChoose: "))
    if ask in [1,2,3,4]:
        if ask == 1:
            flip_image(img_arr)
        elif ask == 2:
            try:
                noise = int(input("Noise level: "))
                add_noise(img_arr, noise)
            except ValueError as e:
                print(f"Error occured: {e}")
                print("Try again with proper inputs")
                continue
        elif ask == 3:
            try:
                channel = int(input("Choose channel (0, 1, 2): "))
                value = int(input("Choose value: "))
                if channel in [0,1,2]:
                    brighten_channels(img_arr, channel, value)
                else: print("Invalid input entered")
            except ValueError as e:
                print(f"Error occured: {e}")
                print("Try again with proper inputs")
                continue
        elif ask == 4:
            apply_mask(img_arr)
            print("DONE")
        elif ask == 5:
            break
    else: print("Choose between the options please.")