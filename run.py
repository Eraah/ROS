#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

bashCommand = "sshpass -p maker ssh robot@ev3dev.local python3 ROS/main.py"
process = subprocess.Popen(bashCommand.split())
