# HomeworkMachine
This project is capable of converting computer characters to hand-written characters, you need to install pytesserect exe as well as the library.
Copy the "CodeWithGUI.py" and "AutoDownloader.py" file in same folder on the desktop and run, all the images will be automatically downloaded in the same folder.

**Feature : **\
!(https://qphs.fs.quoracdn.net/main-qimg-af25ffc0e676f14d4236a726b5f0ada3)

**Install instructions :**

Add Python IDLE to your path, if you are already aware of PIP then you can skip this   step.To do that, download the latest version of IDLE and…\
![Python setup](https://qphs.fs.quoracdn.net/main-qimg-00614a62293ad3dca4a92503ed4f5caa)

Now, open cmd or Command Prompt on your computer and type - pip, if everything is find, you should see something like this\
![Command prompt](https://qphs.fs.quoracdn.net/main-qimg-aebda86ffaa2611323c3f61e9b2b87cf)

Now type `pip install numpy` press enter
After it’s installed, type `pip install keyboard`
and after it’s installed, type `pip install Pillow`
and do the same for cv2 library.

After all the libraries are installed, open this [link](https://github.com/UB-Mannheim/tesseract/wiki)
and download 32bit or 64bit installer of tesseract-ocr, the page should look something like this\
![This is image not text](https://qphs.fs.quoracdn.net/main-qimg-c84fb522047f2d1b12f73e5d99ba50ba)

Just click next a few times and it’s installed, now open the place where it’s and search for an exe file there named teserract, something like this and **copy it’s path somewhere, we will need it later. (Remember this step)**\
![tessseract is installed](https://qphs.fs.quoracdn.net/main-qimg-baa69bf667ace72b4168ce2a4764bb8c)

Now open the [source code of the project](https://github.com/Ankit404butfound/HomeworkMachine)
and open the folder named “Programs” and download these two programs\
![Source code programs](https://qphs.fs.quoracdn.net/main-qimg-168da4e13e676f5ec2b02c622a23fe2a)

Now after they are downloaded, create a folder on Desktop and save both files in that folder\
![desktop 1](https://qphs.fs.quoracdn.net/main-qimg-c2c38726960f3c6da0811aee95b2861d)\
![desktop 2](https://qphs.fs.quoracdn.net/main-qimg-b37bbb223249b47ad994b7db2a900e6f)

Now, double click on AutoDownloader file and if all libraries are correctly installed, the code will download all images in the same folder\
![first time open](https://qphs.fs.quoracdn.net/main-qimg-772154e701e08706e1a3b3291070c7dd)

Meanwhile, open the CodeWithGUI file with IDLE to view it’s source code and you will see a line like this\
![img1](https://qphs.fs.quoracdn.net/main-qimg-437645103aa902c28cea753353a0c1de)\
![img2](https://qphs.fs.quoracdn.net/main-qimg-fa636461eef8e851406b3f4aadaa1a41)

You’d need to edit that line, so this is where we need the path of that exe file I told you about earlier\
![path i told earlier](https://qphs.fs.quoracdn.net/main-qimg-baa69bf667ace72b4168ce2a4764bb8c)

After you copied the file’s path, open that source code and replace this part of the line with the path of your own exe file\
![path of exe file](https://qphs.fs.quoracdn.net/main-qimg-8fb20c483fec85ac52549c6c4fd996de)

DO NOT TOUCH ANYTHING ELSE, not even those quotations, message me before moving on if you want.

Now save the changes you have made and close it. Now again open cmd or command prompt ant type pip install pytesseract. After it’s installed goto that folder.

Now run CodeWithGUI and you should see this if everything works fine\
![check if everything is fine](https://qphs.fs.quoracdn.net/main-qimg-56fdba17cd8d2a21683d448a708a0802)

Now move the image from which you want to read texts from, in the same folder and input it’s name in the entry field and press extract. It will take some time to convert.\
![now move the image](https://qphs.fs.quoracdn.net/main-qimg-b51643e3d8d6f02a875fb130d761a2b1)

The output should look like this, however that capital letters will not be there as I am working on it.

Now, if you want to use the scan feature, press on the button and it will tell you what to do.
