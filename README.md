# FSDI_Final
Django App counts movement through an entryway, records it, and displays it in real time.

<img src=https://raw.githubusercontent.com/chparmley/FSDI_Final/main/Resources/Hive.png width="200">

Installation
------------
clone repo

cd inside cloned folder

*source venv/bin/activate

*pip install matplotlib

Note: update coming with updated requirments.txt and will eventually remove included virtual environment




How to run
--------------
cd Traffic_Monitor

python3 manage.py runserver 0.0.0.0:8000



Accessing the app
------------------
On any device on same network as the device used in the previous step:

http://that.devices.ip.address:8000 <--not for clicking, will format out hyperlink later

Register an account and then login

The app is set up with dummy data for demo purposes.

Delete data as necessary through the admin page, or the sqlite db directly.

Click the edit button to adjust to set ip camera url before running people counting script.

Note: Update pending that will include default admin credentials.



Launching Image Recognition
---------------------------
Leave the app server running and launch new terminal within the main folder 'FSDI_Final':

cd People-Counting-in-Real-Time

python Run.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel

Note: After running follow the terminal menu instructions
