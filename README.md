# FSDI_Final
Django app that counts movement through an area, records it, and displays it in real time.

![Image](https://raw.githubusercontent.com/chparmley/FSDI_Final/main/Resources/Hive.png)

Installation
------------
clone repo

cd inside cloned folder

*python3 -m venv venv

*source venv/bin/activate

*pip install cmake

*pip install -r requirements.txt


How to run
--------------
cd Traffic_Monitor

python3 manage.py runserver 0.0.0.0:8000


Accessing the app
------------------
On any device on same network as the host:

http://'your.host.ip.address':8000

Register an account then login

The app is set up with dummy data for demo purposes.

Delete data as necessary through the admin page, or the sqlite db directly.

Click the edit button to adjust to set webcam or ip camera link before running people counting script.

Update coming with default admin credentials.



Launching Image Recognition
---------------------------
Leave the app server running and in new terminal withing cloned folder 'FSDI_Final':

cd People-Counting-in-Real-Time

python Run.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel
