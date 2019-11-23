# limesdr_dev

## Install Dependencies

- GNURadio Companion
- GNURadio Companion-dev
- Limesuite
- gr-limesdr

### LimeSuite

The drivers PPA for Ubuntu has a recent build of LimeSuite:
``` bash
sudo add-apt-repository -y ppa:myriadrf/drivers
sudo apt-get update
sudo apt-get install limesuite liblimesuite-dev limesuite-udev limesuite-images
sudo apt-get install soapysdr-tools soapysdr-module-lms7

#soapysdr-tools use to be called just soapysdr on older packages
sudo apt-get install soapysdr soapysdr-module-lms7
```


### gr-limesdr source and sink:
Building and installing gr-limesdr from source
Enter the following commands in terminal:
``` bash
  git clone https://github.com/myriadrf/gr-limesdr
  cd gr-limesdr
  mkdir build
  cd build
  cmake ..
  make
  sudo make install
  sudo ldconfig
```

Reload GNU Radio blocks by restarting GNU Radio or by pressing Reload blocks button in top bar of GRC.
 gr-limesdr blocks should appear under LimeSuite category.
