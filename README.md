# jenkins_esp32_lora_testing


## Creating tests with Jenkins and pytest
-----------------------------------------

This repository contains pytest cases, MicroPython code and rshell scripts that determine if an esp32 LoRa development board transmits a rf signal. The objectives of this project is to create a test suite that ...

* Loads the latest MicroPython firmware onto a esp32 device
* Loads and executes MicroPython code on the esp32 device
* Listen for LoRa chips with an SDR

To achieve these objectives Jenkins will ...

* Use a git repository
* Use Pipenv to install python packages into its own user space
* Use a submodule for external MicroPython package
* Upload and then execute code on the esp32 device
* Use pytest to write html and xml reports
* Archive outputs from the embedded device
* Tag a git repository with successful builds

The full article for this repository can be at https://tgu-ltd.uk/creating-tests
