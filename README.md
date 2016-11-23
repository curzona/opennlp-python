opennlp-python
==============

Overview
--------

This package provides a Python wrapper for [Apache OpenNLP](https://opennlp.apache.org/)

Installation
------------
First, install git python and java if you haven't already.

    sudo apt-get update
    sudo apt-get install -y git python python-setuptools python-pip default-jre
    
Then, download opennlp-python and install requirements.

    git clone https://github.com/curzona/opennlp-python.git
    cd opennlp-python
    sudo pip install -r requirements.txt

Next, download [Apache OpenNLP](https://opennlp.apache.org/) tools.
  
    wget http://mirror.metrocast.net/apache//opennlp/opennlp-1.5.3/apache-opennlp-1.5.3-bin.tar.gz
    tar -zxvf apache-opennlp-1.5.3-bin.tar.gz
    cd apache-opennlp-1.5.3
  
Finally, download the pre-trained parser model from [Apache OpenNLP](http://opennlp.sourceforge.net/models-1.5/).
  
    mkdir models
    wget http://opennlp.sourceforge.net/models-1.5/en-parser-chunking.bin
    mv en-parser-chunking.bin models/
    cd ..
  
Running
-------
  
To start the server:

    python opennlp/opennlp.py --path apache-opennlp-1.5.3
  
Make sure the server is working:
  
    python opennlp/client.py

    
