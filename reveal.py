# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:34:10 2021

@author: KM
"""

import streamlit as st
import os
from PIL import Image


st.write('Reveal Your Ideal Type')
choice = st.selectbox('Make a choice',('Boy','Girl'))
startin = st.checkbox('start')



def showing(Gender,TorNT,LorS):
    st.write(Gender,TorNT,LorS)
    if Gender == 'G':
        last = 'Girl'
    if Gender == 'B':
        last = 'Boy'
    inidir = 'photo\\' + Gender + "\\" + TorNT + "\\" + LorS + "\\"
    imagee= Image.open(inidir + os.listdir(inidir)[0])
    resized_image = imagee.resize((225,250),Image.ANTIALIAS)
    st.image(imagee, caption = 'This is your dream ' + last, width = 350)
    

def LHSH(Gender,TorNT):
    st.write('Which type do you prefer?')
    col1, col2 = st.columns(2)
    with col1:
        LH = st.checkbox('Long Hair')
    with col2:
        SH = st.checkbox('Short Hair')
    if LH == True:
        showing(Gender,TorNT,'LH')
        
    if SH == True:
        showing(Gender,TorNT,'SH')
 
def tatnotat(Gender):
    st.write('Do you like your soulmate with tattoos?')
    col1, col2 = st.columns(2)
    with col1:
        tat = st.checkbox('Yes')
    with col2:
        notat = st.checkbox('No')
    
    if tat == True:
        LHSH(Gender,'T')
    if notat == True:
        LHSH(Gender,'NT')


if startin == True and choice == 'Boy':
    st.write('boy')
    tatnotat('B')
    

if startin == True and choice == 'Girl':
    st.write('girl')
    tatnotat('G')

