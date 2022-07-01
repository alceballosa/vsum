#!/bin/sh

mkdir data/external/summe
mkdir data/external/tvsum
wget -P data/external/summe/ https://data.vision.ee.ethz.ch/cvl/SumMe/SumMe.zip 
unzip data/external/summe/SumMe.zip
wget -P data/external/tvsum/ http://people.csail.mit.edu/yalesong/tvsum/tvsum50_ver_1_1.tgz 
tar -xvzf data/external/tvsum/tvsum50_ver_1_1.tgz
