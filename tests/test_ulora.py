import subprocess
import pytest


@pytest.mark.run(after='test_firmware_loaded')
def test_lora_code_uploaded():
    ''' Test LoRa main and library code was uploaded to the device '''
    rshell_completed = False

    rshell_cmd = [
        'rshell', '-p', '/dev/ttyUSB0', '--baud', '115200',
        '-f', './rshell/lora.rshell'
    ]
    rtn = subprocess.run(rshell_cmd, stdout=subprocess.PIPE)
    if rtn.returncode == 0:
        rshell_completed = True
    assert(rshell_completed is True)


@pytest.mark.run(after='test_lora_uploaded')
def test_lora_chirp_output_file():
    ''' Test the main LoRa code outputted a file with 10 lines of chip response  '''
    expected_chirps = 10
    chirp_sequence = 0

    with open('./archive/lora_output.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            if '{0} RSSI:'.format(i) in line:
                chirp_sequence += 1
            else:
                break

    assert(chirp_sequence == expected_chirps)
