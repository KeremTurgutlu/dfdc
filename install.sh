#!/bin/bash

dpkg -i /kaggle/input/decord/ffmpeg/ffmpeg/*.deb  &> /dev/null

mkdir reader && cp -r /kaggle/input/decord/decord/* /kaggle/working/reader

cd /kaggle/input/decord/cmake-3.16.4-Linux-x86_64/cmake-3.16.4-Linux-x86_64
cp -r bin /usr/
cp -r share /usr/
cp -r doc /usr/share/
cp -r man /usr/share/

cp /usr/local/nvidia/lib64/libnvcuvid.* /usr/local/cuda/lib64
cp /usr/local/nvidia/lib64/libnvidia-ml.* /usr/local/cuda/lib64
cp /usr/local/nvidia/lib64/libcuda.so /usr/lib/x86_64-linux-gnu/
cp /usr/lib/x86_64-linux-gnu/libpthread.so /lib/libpthread.so.0
cp /usr/lib/x86_64-linux-gnu/libpthread_nonshared.a /usr/lib/
cp /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 /lib/
cp /usr/lib/x86_64-linux-gnu/libc_nonshared.a /usr/lib/
cp /lib/x86_64-linux-gnu/libc.so.6 /lib/

cd /kaggle/working/reader
mkdir build
cd build
cmake .. -DUSE_CUDA=ON &> /dev/null
make &> /dev/null