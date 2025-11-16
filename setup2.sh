sudo ../venv/bin/pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
sudo ../venv/bin/pip3 install numpy
sudo ../venv/bin/pip3 install rpi_ws281x 
sudo ../venv/bin/pip3 install adafruit-circuitpython-neopixel
sudo ../venv/bin/pip3 install --force-reinstall adafruit-blinka

sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint disable_raspi_config_at_boot 0

echo 'sudo syzygy/venv/bin/python3 syzygy/gravimatrix/dev/test_buttons-12x10.py' >> ~/.bashrc