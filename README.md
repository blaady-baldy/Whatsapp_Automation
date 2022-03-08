# Whatsapp_Automation

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Maintainers


INTRODUCTION
------------

Whatsapp Automation basically provides you with 
  1. Messages (Personalized/Standard)
  2. Media files(image/video)
  3. Pdf
to send to multiple contacts.

The idea for the project was to provide easy ways for people starting their businesses
and storing data in excel to reach out to their customers in an easy way.
Most people start registration for events/webinars/startups with the help of Google 
forms which convert the data into excel sheets.
This project helps user to generate personalised messages and reach out to their
audience in an easy and efficient way avoiding errors and saving time and space.

REQUIREMENTS
------------

This module requires Python 3 to be installed in your system.

1. To check if Python is installed in your system :

        python --version

    * Then you should see something like this :

          Python 3.9.1
    
    * If not installed, go to https://www.python.org/downloads/ 

2. Then verify if pip was installed successfully:

          pip -V

    * Then you should see something like this :

          pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)

* Another thing that is required is stable internet connection with speed of 1mbps.


INSTALLATION
------------

1. Install the Whatsapp Automation module by forking or cloning the project in your 
system by running the following command : 

        git clone https://github.com/blaady-baldy/Whatsapp_Automation.git

2. Install virtualenv using pip (if not already installed): 

        pip install virtualenv

3. Run the following command in the terminal :

        virtualenv env

    * Change the directory to the folder where you have cloned the repo and run :

          .\env\Scripts\activate

    * then you should see something like :

          (env) PS D:\python\


4. Install all dependencies by running the following command :

        pip install -r requirements.txt

5. Then to run the program run the following command in the terminal in the cloned repo :

        python app.py

6. To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’ :

        deactivate


MAINTAINERS
-----------

 * Devansh Singh - blaadybaldy@gmail.com

 


