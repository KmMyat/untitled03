# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:34:10 2021

@author: KM
"""

import streamlit as st
import os
from PIL import Image


st.title('Reveal Your Ideal Type')
st.image('photo/front.jpg')
choice = st.selectbox('Choose your partner..',('Boy','Girl'))
startin = st.checkbox('start')



def showing(Gender,TorNT,LorS):
    
    if Gender == 'G':
        last = 'Girl'
    if Gender == 'B':
        last = 'Boy'
        
    st.write('This is your dream' + last)
    inidir = 'photo/' + Gender + "/" + TorNT + "/" + LorS + "/"
    '''
    st.write(inidir)
    st.write(os.listdir(inidir)[0])
    '''
    
    imagee= Image.open(inidir + os.listdir(inidir)[0])
    resized_image = imagee.resize((225,250),Image.ANTIALIAS)
    st.image(resized_image,width = 400)
    st.write('Hope you get a wonderful soulmate')
    '''
    st.image('photo/G/T/LH/GTLH.jpg')
    '''
    
    

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

