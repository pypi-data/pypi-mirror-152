# [letsgoING](https://letsgoing.org/) RemoteLab ArduinoControl for Raspberry Pi

This package allows to perform IO on a real Arduino from a Raspberry Pi.  
Combine with VNC remote desktop and the Arduino IDE for basic Arduino teaching without the wiring hassle.

## Installation

    python3 -m pip install letsgoing-rpi-arduinocontrol

### Troubleshooting
pip likely installs to your local path, which is not included by default. Try adding .local/bin to your path:

    echo export PATH=$HOME/usr/local/bin:$PATH >> .bashrc && source .bashrc

The Pillow library is known for weird hiccups, try manual reinstallation:

    python3 -m pip install --upgrade --force-reinstall Pillow

## Releasing a new version to PyPI
Consider testing the release on test.pypi.org first!

    # clone the repo
    git clone https://github.com/tobiglaser/letsgoing-rpi-arduinocontrol

    # install locally
    python3 -m pip install .

    #test
    letsgoing-rpi-arduinocontrol
    
    # build the package
    export PYTHONIOENCODING=utf-8  # because it complaines otherwise
    python3 -m build

    # upload to PyPI
    twine upload dist/*

    # clean up before next upload
    rm dist/*

### More info:
[testpypi](https://packaging.python.org/en/latest/guides/using-testpypi/)

[packaging projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

[CI/CD ?](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)