#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Noora Almarri
# DATE CREATED:  18/11/2020                               
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 

from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):

    for key in results_dic:
       
       # TODO: 3a. Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label       
       model_label = classifier(images_dir+key, model)
       model_label = model_label.lower() #change to lower case
       model_label = model_label.strip() #remove the white space

# defines truth as pet image label 
       truth = results_dic[key][0]
       # TODO: 3c. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           1 (where the value of 1 indicates a match between pet image 
       #           label and the classifier label) to the results_dic dictionary
       #           for the key indicated by the variable key 
       #
       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match(1) using extend list function
       
       if truth in model_label:
            results_dic[key].extend((model_label, 1))
       else:
           results_dic[key].extend((model_label, 0))


                         
                         
        
                         
           

    