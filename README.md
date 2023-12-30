# Copy files from directoy using python

# Purpose
This file will detail the steps required to copy files from one directory in the Android filesystem to the external SD Card using a python script, on macrodroid. I'm doing this because google camera doesn't support saving photos to the external Micro SD card, and I've read you can use macrodroid and a bash script to move files periodically. I'm doing the actual file movement script in python because I know way more python than bash :-)

# Dependecies
This project is targeted for a very specific use case, if you're going to try and replicate this, you will need the following:

- A phone or tablet running Android OS. At the time of writing, Android 13 was used. Device must be rooted.
- [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=en_US)
- [Termux](https://f-droid.org/packages/com.termux/)
- [Termux:Tasker](https://f-droid.org/es/packages/com.termux.tasker/)
- The files from this repository
- Android: A file manager that will allow you to read/write to the root partition
- Optional: A Micro SD card, but you could move your files to another directory of your choice.

# Instructions

1. Download Macrodroid from the playstore. Give all the required permissions in order for the app to function properly. You may also need to install helper apps for your device. For more info, visit [This](https://macrodroidforum.com/wiki/index.php/MacroDroid_Wiki) link.
2. Download Termux from F-Droid. Give it the required permissions
3. Download Termux:Tasker plugin from F-Droid. Give it the required permissions
4. Copy the files from this repository to the android device ([main.py](./main.py), [run.sh](./run.sh)). I used the Downloads directory as example
5. 
