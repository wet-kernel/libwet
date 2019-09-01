#!/usr/bin/env bash

wapp="python3 /bin/wapp"

echo -n "Installing libwet ... "
mkdir code
> code/libwet.py
cat colors.py >> code/libwet.py
cat archive.py >> code/libwet.py
$wapp -c libwet libwet.control
$wapp -i libwet
rm -r code
echo "done"
