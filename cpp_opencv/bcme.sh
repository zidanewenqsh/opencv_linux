#!/usr/bin/bash
if [ -d "build/" ];then
  rm -rf build/
fi
mkdir build
# cd build
cmake -B build
make -C build
# cp resource/3_1.jpg build/bin/3_1.jpg
# cp resource/netmnist_00_0.script build/bin/netmnist_00_0.script
# cd build/bin

cp ../resource/cat01.jpg build/bin
cd build/bin
./aopencv
