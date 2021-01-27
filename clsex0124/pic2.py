from PIL import Image
img = Image.open("D:/Code/python/clsex0124/Draius.jpeg") # 打开
# img = Image.open("./img/cat.jpg") # 打开

#转换为黑白图片，参数"L"表示黑白模式
out = img.convert("L") # 灰度  先将彩色图片转换为黑白图片
width, height = out.size # 赋值
out = out.resize((int(width * 0.2),int(height * 0.1))) # 改变图像的大小
width, height = out.size # 赋值

#生成字符画所需的字符集
asciis = "@%#*+=-. "
texts  = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        texts += asciis[int(gray / 255 * 8)]
    texts += "\n"
with open("bijini.txt","w") as file:
    file.write(texts)
