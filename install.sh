#!/bin/bash

#if [ "$(uname)" != "Linux" ]; then
#    echo "Only linux install is supported at the moment"
#	exit 0
#fi

if ! [ $(id -u) -eq 0 ]; then
	echo "run as root (look at the install script if you're paranoid)"
	exit 0
fi

b_path="/usr/local/bin/scanlan"
s_path="/usr/local/src/scanlan"

if [ $(test -L $b_path) ]; then
	echo "removing previous symlink"
	rm -rf $b_path
fi

echo "installing to $s_path"
mkdir -p $s_path
cp scanlan.py $s_path
ln -sf $s_path/scanlan.py $b_path

echo "install successful"
echo "you can now delete this folder and everything in it"
