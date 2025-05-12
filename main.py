import segno
from PIL import Image
import random
import os
import platform

#clear
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear_screen()

# color
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]

color1, color2, color3, color4, color5 = random.sample(colors, 5)
baner = f"""{color5}
         _  _ ____ _  _ ____    ____    ____ ____    ____ ____ ___  ____
         |\/| |__| |_/  |___    |__|    |  | |__/    |    |  | |  \ |___
         |  | |  | | \_ |___    |  |    |_\| |  \    |___ |__| |__/ |___


                      \033[34mhttps://github.com/kenjayevdev
                           \033[32mhttp://devscript.uz/\n
        {color2}[\033[31m#\033[0m\033[33m]\033[31mProgram information: This program allows you to create QR Codes{color1}[\033[31m#\033[0m\033[33m]\n
"""
print(baner)

def create_qr():
    data = input("\n\033[33mEnter information for QR Code:")
    id = random.randint(1,10000)
    filename = f'qr_code_colored{id}.png'
    
    # Generate QR code
    qrcode = segno.make(data, version=7, error='h')

    # Save in color
    qrcode.save(filename, scale=4, dark='darkred',
                data_dark='darkorange', data_light='yellow')

    # Open the image
    def open_img():
        if platform.system() == "Windows":
            img = Image.open(filename)
            img.show()
        else:
            pass
    open_img()
    print(f"\n\033[34mQR Code '\033[32m{filename}' \033[34msaved and opened with the name.")

# Main loop
while True:
    create_qr()
    choice = input("\n\033[31mDo you want to create another QR code? Yes (1) / No (0): ")
    if choice.strip() != '1':
        print("\n\033[0mThe program is over. Goodbye!")
        break
