from PIL import Image
import tkinter as tk  # tk大体
from tkinter import filedialog  # line 18, 用于浏览文件
import os  # line 66, 用于打开输出文件
import time  # 用于显示当前时间（日志中）

ASCII_HIGH = '''$@%8&#*1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM/\|()1{}[]?-_+~<>i!lI;:,'"\^`. '''


time_started=time.time()
print(time_started)

# 打开文件
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]请选择图片路径...  Please browse the picture...')
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# 行&列
rows = 180
cols = 120
output = 'output.txt'
image_path = file_path
image = Image.open(image_path)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]正在向你展示原图...  Now show the real picture to you...')
image.show()
image.save('原图.PNG')

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]成功另存为原图！  Save again the real picture successfully!')

# 调整图片大小
image = image.resize((rows, cols))
# 转为为字符
txt = ''
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]转换中...  Changing...')

for col in range(cols):
    for row in range(rows):
        color = image.getpixel((row, col))
        # 如果是RGBA模式且alpha通道为0，返回空字符
        if image.mode == "RGBA" and color[3] == 0:
            char = ' '
        else:
            gray = int(
                0.2126 *
                color[0] +
                0.7152 *
                color[1] +
                0.0722 *
                color[2])
            # 比率 0-255 <---> 0-70
            length = len(ASCII_HIGH)
            rate = length / 256.0
            char = ASCII_HIGH[int(gray * rate)]
        txt += char
    txt += '\n'

# 写入文件
with open(output, 'w') as f:
    f.write(txt)

time_finish=time.time()
time_used=time_finish-time_started

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]转换成功，用时', time_used, '秒。即将为您打开文件...  ', 'Changed successfully, total use',time_used,'second. Opening the file...')
os.system('output.txt')  # 打开文件
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '[INFO]已为您打开文件！  Open file successfully!')
