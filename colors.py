#  In the name of God, the Compassionate, the Merciful
#  OS Wet (c) 2019 Mani Jamali. Free Software under GNU GPL v3.0
#  This code is a part of 'libwet' project.
# colors.py

class colors:
    fg_black = 30
    fg_red = 31
    fg_green = 32
    fg_yellow = 33
    fg_blue = 34
    fg_purple = 35
    fg_cyan = 36
    fg_white = 37

    style_none = 0
    style_bold = 1
    style_underline = 2
    style_negative1 = 3
    style_negative2 = 5

    bg_black = 40
    bg_red = 41
    bg_green = 42
    bg_yellow = 43
    bg_blue = 44
    bg_purple = 45
    bg_cyan = 46
    bg_white = 47

    def set_color (style,fg,bg):
        return "\033["+str(style)+";"+str(fg)+";"+str(bg)+"m"

    def get_ok():
        return "\033["+str(colors.style_none)+";"+str(colors.fg_white)+";"+str(colors.bg_black)+"m"

    def get_warning():
        return "\033[" + str(colors.style_none) + ";" + str(colors.fg_yellow) + ";" + str(colors.bg_black) + "m"

    def get_error():
        return "\033[" + str(colors.style_none) + ";" + str(colors.fg_red) + ";" + str(colors.bg_black) + "m"

    def show (name,type,message):
        if type=="ok":
            print (colors.get_ok()+name+": "+message + colors.get_ok())
        elif type=="warning":
            print (colors.get_warning()+name+": "+message + colors.get_ok())
        elif type=="error":
            print (colors.get_warning()+name+": "+message + colors.get_ok())
        else:
            colors.show("libwet","error",type+": type not exists.")

