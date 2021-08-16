#!/bin/sh
sudo netctl stop-all
sudo ifconfig wlo1 up
sudo iw wlo1 scan
sudo ifconfig wlo1 down
sudo 
