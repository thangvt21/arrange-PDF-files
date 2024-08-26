from PIL import Image
from IPython.display import display
import cv2

img = cv2.imread("E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\Retro_Lil_AJ_11_Low_Diffused_Blue_png.png")
cv2.imshow("test",img)
cv2.waitKey(0)

# with Image.open(
#     "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\Retro_Lil_AJ_11_Low_Diffused_Blue_png.png"
# ) as img:
#     display(img)
