import cv2
import glob
from pathlib import Path

all_imgs = glob.glob("practice/*jpg")

for image in [Path(filename).stem for filename in all_imgs]:
    img = cv2.imread(f"practice/{image}.jpg",0)
    resized_img = cv2.resize(img,(100,100))
    cv2.imwrite(f"practice/{image}_resized.jpg",resized_img)

