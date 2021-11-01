#!/bin/bash

b_path="/usr/local/bin/scanlan"
s_path="/usr/local/src/scanlan"

if [ $(test -L $b_path) ]; then
	echo "removing previous symlink"
	rm -rf $b_path
fi

python3 -m pip install -r ./require.txt --user

echo "installing to $s_path"
sudo mkdir -p $s_path
sudo cp scanlan.py $s_path
sudo ln -sf $s_path/scanlan.py $b_path

echo "install successful"
echo "you can now delete this folder and everything in it"
