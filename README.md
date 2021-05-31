# Developing-of-Funcx-Prototype

Setup/Installation for Funcx
For installing of the environment please follow the link: 
https://github.com/Funcx-faas/Funcx
Installation of Funcx client and agent using Cloud as the Edge device	
Setting up an Environment:  Use the following commands: 
1.	Create an EC2 instance in AWS. 
2.	Create 2nd EC2 instance in AWS.
3.	SSH into the 1st EC2 instance created and install the python version 3.6: 

          sudo su
          python3 –version
          sudo apt update
          sudo apt install python3-pip
          python3 -m pip  install Funcx
          
4.	SSH into the 1st EC2 instance created and install the python version 3.6.

          sudo su
          python3 –version
          sudo apt update
          sudo apt install python3-pip
          python3 -m pip  install Funcx-endpoint
 


5.	The first time you try to configure an endpoint, it gives you an authentication code through the globus ID. Copy paste the ID.

 
7.	In order to configure the endpoint, use the command: 
        
        Funcx-endpoint configure <endpoint name>


8.	In order to start the Endpoint, use the command:
        
        Funcx-endpoint start <endpoint name>


9.	Your endpoint will now be active and will come along with a unique identifier ID that you can use to retrieve the status and results of your task.
 

 

10. In order to list the endpoint, that are active on your machine, use the command: 
          
          Funcx-endpoint list
 
11.	In order to run the function, specify the endpoint ID on which you want your function to run and the function ID in your function.
       Refer the Matrix100.py function above. 


12.	In order to try more function, follow the link: https://Funcx.readthedocs.io/en/latest/endpoints.html
Try creating an endpoint on the 2nd EC2 Instance and try running the function on that endpoint from the first EC2 instance.

Installation of Funcx client and function endpoint using the Raspberry Pi as the edge:

1.	Download the Raspberry Pi Imager and put the Raspbian OS in your SD Card.
2.	In order to install the python 3.6 follow the following steps.
3.	Raspbian has a default python version of 2.7.13 which isn’t compactible with the Funcx. 
Note: This task may take upto 5 hours
4.	In order to check the python version and install python 3.6 follow the following steps:
          
          python –version
          sudo apt-get update
 
          sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
 
         cd /tmp/
 
         wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
 
        tar xf Python-3.6.4.tar.xz
 
 
        cd Python-3.6.4
      	./configure
       make
       sudo make altinstall
    	ls /usr/bin/python*
       ls /usr/local/bin/python*
       sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
       sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
       sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 3

You will now have the python version 3.6 install on your Raspberry pi.
 
 
Funcx Tutorials using Raspberry Pi as the Edge Device: 
Follow the same steps mentioned for the installing the Funcx client and the Funcx-endpoint in the cloud.
1.	 Refer the tutorial: https://Funcx.readthedocs.io/en/latest/endpoints.html
Installing Funcx-agent/endpoint and the Funcx-client and invoking the functions on Ubuntu using Laptop as the Edge device.
Installing on Ubuntu 20.4 with Python 3.6, Ubuntu 20.4 has a default version of 3.8 which isn’t compactible with Funcx and thus we make the default version to 3.6 in our system.

1.	Follow the link for making the 3.6 python default
a.	https://towardsdatascience.com/building-python-from-source-on-ubuntu-20-04-2ed29eec152b?gi=269e5dc7bdb4

2.	Refer the link:
a.	https://Funcx.readthedocs.io/en/latest/endpoints.html

 

 

 

 

 

 


 
 



 

