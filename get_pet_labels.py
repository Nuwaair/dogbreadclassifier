#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Noora Almarri
# DATE CREATED:  16/11/2020                                
# REVISED DATE: 20/11/2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).

##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    in_files= listdir(image_dir)  # Creates list of files in directory
    results_dic = dict() # Creates empty dictionary for the petlabels

    for idx in range(0, len(in_files), 1):  # Processes through each file in the directory, extracting only the words
        # of the file that contain the pet image label
        if in_files[idx] [0] != ".":
            image_name = in_files[idx].rsplit("_")
            pet_label = ""
            for word in image_name:
                if word.isalpha():
                    pet_label += word.lower() + " "
                    pet_label = pet_label.strip() #strip the tailing white space
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:",in_files[idx])
      
    # Replace None with the results_dic dictionary that you created with this # function
    return(results_dic)
