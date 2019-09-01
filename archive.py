#  In the name of God, the Compassionate, the Merciful
#  OS Wet (c) 2019 Mani Jamali. Free Software under GNU GPL v3.0
#  This code is a part of 'libwet' project.
# archive.py

import os, shutil, py_compile

class archive:
    def create_data(data_name):
        data_file = "/var/cache/wapp/archives/build/data"
        if os.path.isdir(data_name):
            shutil.make_archive(data_file, "xztar",data_name)

    def create_code(code_name):
        if os.path.isdir(code_name):
            code_file = "/var/cache/wapp/archives/build/code"
            shutil.make_archive(code_file, "xztar",code_name)

    def unpack_data(self):
        if self=="@unpack":
            data_file = "/var/cache/wapp/archives/build/data.tar.xz"
            data_path = "/var/cache/wapp/archives/data"
            if os.path.isfile(data_file):
                shutil.unpack_archive(data_file, data_path, "xztar")
        else:
            data_file = "/var/cache/wapp/archives/build/data.tar.xz"
            if os.path.isfile(data_file):
                shutil.unpack_archive(data_file, self, "xztar")

    def unpack_code():
        code_file = "/var/cache/wapp/archives/build/code.tar.xz"
        code_path = "/var/cache/wapp/archives/code"
        if os.path.isfile(code_file):
            shutil.unpack_archive(code_file, code_path, "xztar")

    def compile(src, dest):
        code_path = "/var/cache/wapp/archives/code/"
        data_path = "/var/cache/wapp/archives/data/"
        if not os.path.isdir (data_path): os.mkdir (data_path)
        if str(src).endswith(".py"):
            py_compile.compile(code_path + src, data_path + dest)
        else:
            colors.show("libwet","error",str(src)+": cannot compile: Unknown code.")

    def wrapp_data():
        data_path = "/var/cache/wapp/archives/data"
        data_file = "/var/cache/wapp/archives/build/data"
        shutil.make_archive(data_file, "xztar", data_path)

    def wrapp_code():
        code_path = "/var/cache/wapp/archives/code"
        code_file = "/var/cache/wapp/archives/build/code"
        shutil.make_archive(code_file, "xztar", code_path)