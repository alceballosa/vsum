#!/bin/sh
mkdir videosum_datasets
mkdir videosum_datasets/summe
mkdir videosum_datasets/tvsum
wget -P videosum_datasets/summe/ https://data.vision.ee.ethz.ch/cvl/SumMe/SumMe.zip && unzip videosum_datasets/summe/SumMe.zip
wget -P videosum_datasets/tvsum/ http://people.csail.mit.edu/yalesong/tvsum/tvsum50_ver_1_1.tgz && tar -xvzf videosum_datasets/summe/tvsum50_ver_1_1.tgz