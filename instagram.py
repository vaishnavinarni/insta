# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:44:37 2023

@author: VAISHNAVI
"""

import instaloader
import streamlit as st

# Creating an Instaloader() object
ig = instaloader.Instaloader()

# Define a Streamlit function to fetch and display Instagram profile information
def fetch_instagram_profile(username):
    try:
        # Fetching the details of the provided username using Instaloader object
        profile = instaloader.Profile.from_username(ig.context, username)
        
        # Displaying the fetched details
        st.write("Username:", profile.username)
        st.write("Number of Posts Uploaded:", profile.mediacount)
        st.write(profile.username + " is having " + str(profile.followers) + ' followers.')
        st.write(profile.username + " is following " + str(profile.followees) + ' people')
        st.write("Bio:", profile.biography)

        # Downloading the profile picture of that account
        ig.download_profile(username, profile_pic_only=True)
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit app title
st.title("Instagram Profile Information")

# Input field for the Instagram username
username = st.text_input("Enter Instagram Username:")

# Button to fetch and display profile information
if st.button("Fetch Profile"):
    if username:
        fetch_instagram_profile(username)
    else:
        st.warning("Please enter an Instagram username.")