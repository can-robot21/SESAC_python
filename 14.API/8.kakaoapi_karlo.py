import io
import base64
from PIL import Image

# Base64 인코딩 함수
def imageToString(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return my_encoded_img

# Base64 디코딩 및 이미지 변환 함수
def stringToImage(base64_string, mode='RGBA'):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img

# 이미지 파일 불러오기
img = Image.open('my_image.png')

# 이미지를 Base64 인코딩하기
img_base64 = imageToString(img)

# Base64 인코딩된 값을 디코딩해 이미지로 변환하기
image = stringToImage(img_base64, mode='RGB')