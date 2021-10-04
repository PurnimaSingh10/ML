# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:44:48 2021

@author: so
"""

import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request 
import pickle
import numpy as np
import session_info

ab=session_info.show()