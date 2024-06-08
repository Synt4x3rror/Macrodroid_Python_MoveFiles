# Copy Files to Directory - Termux + Python + Macrodroid

## Purpose
This file will detail the steps required to move files from one directory in the Android filesystem to the external SD Card using a python script, on macrodroid. I'm doing this because google camera doesn't support saving photos to the external Micro SD card, and I've read you can use macrodroid and a bash script to move files periodically. I'm doing the actual file movement script in python because I know way more python than bash :-)

## Dependecies
This project is targeted for a very specific use case, if you're going to try and replicate this, you will need the following:

- A phone or tablet running Android OS. At the time of writing, Android 13 was used. Device must be rooted.
- [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=en_US)
- [Macrodroid Helper App](https://www.macrodroidforum.com/index.php?threads/macrodroid-helper-apk.1/)
- [Termux](https://f-droid.org/packages/com.termux/)
- [Termux:Tasker](https://f-droid.org/es/packages/com.termux.tasker/)
- [Python](https://wiki.termux.com/wiki/Python) for termux
- The files from [this repository](https://github.com/Synt4x3rror/Macrodroid_Python_MoveFiles)
- Android: A file manager that will allow you to read/write to the root partition (optional)
- Optional: A Micro SD card, but you could move your files to another directory of your choice.

## Instructions

1. Download Macrodroid from the playstore. Give all the required permissions in order for the app to function properly. You may also need to install helper apps for your device. For more info, visit [This](https://macrodroidforum.com/wiki/index.php/MacroDroid_Wiki) link.
2. Download and install the Macrodroid Helper app from the link in [dependencies](#dependencies). Give it the appropiate permissions.
Open the MD Helper app and make sure you enable at least 'Files' and 'Photos and Videos' ticks.\
    <img src="./github/images/mdh_permissions.png" height="600"></img>
    <img src="./github/images/mdh_permission.png" height="600"></img>
3. Download Termux from F-Droid. Give it the required permissions
4. Download Termux:Tasker plugin from F-Droid. Give it the required permissions
5. Copy the files from [this repository](https://github.com/Synt4x3rror/Macrodroid_Python_MoveFiles) to the android device ([main.py](./main.py), [run.sh](./run.sh)). I used the Downloads directory as example. Make sure to use a directory in the internal storage (not on the SD Card).
6. Open termux and navigate to the directory where you copied the scripts.
   ![Change Directory](./github/images/cd_downloads.png)
7. Use the chmod command to assign the execution permission to [run.sh](./run.sh)
    ```
    chmod +x run.sh
    ```
8. Create a /tasker directory on the termux directory. I'm also creating a /Scripts directory but it's optional.
   ```
   mkdir ~/.termux/tasker
   ```
   ```
   mkdir ~/.termux/tasker/Scripts
    ```
   ![Create Directory in Termux Environment](./github/images/mkdir_termux.png)
9. Copy the run.sh file to that directory. If using a file manager, the full path to the directory will be:
    ```
   /data/data/com.termux/files/home/.termux/tasker/Scripts
   ```
   **Remember that path, we will be using it shortly!**
10. (Optional but **highly** recommended) Test that the shell script is working properly. The shell script takes three parameters:
   - Path to python file [main.py](./main.py)
   - Source directory from where to move photos from
   - Target Directory

      Example:
      ```
      /data/data/com.termux/files/home/.termux/tasker/Scripts/run.sh "/storage/emulated/0/Download/Scripts/main.py" "/storage/emulated/0/DCIM/Camera" "/storage/6332-3630/DCIM"
      ```
      If you get "Script Finished" as output, congrats! Script ran successfully!
      ![Script Test](./github/images/script_test.png)

11. On Macrodroid choose the "Add Macro" button. On the next screen assign the macro a name.
12. Choose a trigger that works for you. The most basic example I could think of is the widget button, so I'll be using that one in this example.\
   <img src="./github/images/Initial_steps_md.png" height="800"></img>

13. On the actions block add a new action. Choose Applications > Tasker/Locale Plugin > Termux:Tasker > Termux
14. On the executable path copy the path to the .sh file. See step 9
15. On the arguments box, copy IN ORDER the path to the python file, path to source directory, and path to target directory. Leave the rest of the parameters as default. Press the save button on the top left.\
   <img src="./github/images/termux:tasker.png" height="800"></img>

16. Leave parameters as default and press OK\
   <img src="./github/images/termux:tasker2.png" height="800"></img>

17. Press on the bottom right icon to save your macro
17. Test your macro. Any issues should be catched by the macrodroid log. Best of luck!
