# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:34:10 2021

@author: KM
"""

import streamlit as st
import os
from PIL import Image
import random

st.write("YO...")
st.image('photo/front.jpg')
choice = st.selectbox('Choose your partner..',('Boy','Girl'))
startin = st.checkbox('start')

def finding(loc):
    total = len(os.listdir(loc)) - 1
    count = random.randint(0,total)
    return count

def showing(Gender,TorNT,LorS):
    
    if Gender == 'G':
        last = 'Girl'
    if Gender == 'B':
        last = 'Boy'
        
    st.write('This is your dream' + last)
    inidir = 'photo/' + Gender + "/" + TorNT + "/" + LorS + "/"
    
    countie = finding(inidir)
    
    imagee= Image.open(inidir + os.listdir(inidir)[countie])
    st.image(imagee, width = 400, caption = 'Hope you get a wonderful soulmate...<3')
    col1,col2 = st.columns(2)
    with col1:
        st.write('Wanna try your miracle next time..! ')
    with col2:
        st.button('Click here')
    

    
    

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
    tatnotat('B')
    

if startin == True and choice == 'Girl':
    tatnotat('G')

