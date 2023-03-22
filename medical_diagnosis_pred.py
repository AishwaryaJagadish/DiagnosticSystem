# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:04:12 2023

@author: Aishwarya
"""
import numpy
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('F:/Projects 2022/PYTHON/Medical Diagnosis System/Models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('F:/Projects 2022/PYTHON/Medical Diagnosis System/Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('F:/Projects 2022/PYTHON/Medical Diagnosis System/Models/parkinsons_disease_model.sav','rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],icons=['activity','heart','person'],default_index=0)
                          
                       

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")