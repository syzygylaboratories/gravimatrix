pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
pip3 install numpy
pip3 install rpi_ws281x 
pip3 install adafruit-circuitpython-neopixel
python3 -m pip install --force-reinstall adafruit-blinka


sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint disable_raspi_config_at_boot 0

echo 'sudo syzygy/gravimatrix/venv/bin/python syzygy/gravimatrix/gravimatrix-12x10.py' >> ~/.bashrc