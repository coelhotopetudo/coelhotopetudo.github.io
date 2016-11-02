cd TrinityCore
mkdir build
cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=/home/$USER/server -DTOOLS=1 -DWITH_WARNINGS=1
make -j $(nproc)
make -j $(nproc) install
