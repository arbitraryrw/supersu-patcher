# SuperSu Patcher
SuperSu patcher, also known as SuperNu, is a utility that patches the [SuperSu](https://supersuroot.org/) binaries to evade common root detection techniques. This is done by simply patching the `su` binaries and associated references to `nu`. 

SuperSu Patcher was tested on a OnePlus 5t using [SR5-SuperSU-v2.82-SR5-20171001224502](https://forum.xda-developers.com/apps/supersu/2014-09-02-supersu-v2-05-t2868133), steps to root can be found [here](https://forums.oneplus.com/threads/guide-oneplus-5-how-to-unlock-bootloader-flash-twrp-root-nandroid-efs-backup-and-more.548216/). 

### Basic Usage
Run the `run.py` python3 file and pass the SuperSU archive as a parameter as seen below:

```python
python3 run.py -i <path_to_supersu_archive>
```

### Further Usage
For further usage instructions please refer to the help dialogue.

```bash
➜ python3 run.py --help

usage: run.py [-h] [-q] [-p] [-o DIRECTORY] -i SUPERSU ZIP

supersu patcher

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           don't print status messages to stdout
  -p, --purge           purge output directory before running
  -o DIRECTORY, --ouput DIRECTORY
                        output directory for final artifacts

required arguments:
  -i SUPERSU ZIP, --input SUPERSU ZIP
                        input super su file to patch
```

### System Dependencies
This project requires [radare2](https://github.com/radareorg/radare2) to be installed on the system.

### Python3 Dependencies
All the python3 dependencies are documented in the [requirements.txt](https://github.com/arbitraryrw/supersu-patcher/blob/master/requirements.txt) file, to install the dependencies run:

```python
python3 -m pip install -r requirements.txt
```

### References / Inspiration
- [Common Root Detection Methods](https://mobile-security.gitbook.io/mobile-security-testing-guide/android-testing-guide/0x05j-testing-resiliency-against-reverse-engineering#testing-root-detection-mstg-resilience-1)
- [Google SafetyNet](https://developer.android.com/training/safetynet/attestation)
- [Magisk](https://magiskmanager.com/)
- [Magisk Hide](https://www.xda-developers.com/how-to-use-magisk/)
- [SuperSu](https://supersuroot.org/)
- [Root Cloak](https://repo.xposed.info/module/com.devadvance.rootcloak2)
