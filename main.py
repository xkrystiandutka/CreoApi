from mimetypes import init
import creopyson
import os

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)
c.creo_cd("D:\API")
c.file_open("kr_du_13k1.prt")
c.view_activate("FRONT")

# CONSTANTS
creoPath = 'C:/Program Files/PTC/Creo 7.0.1.0/Parametric/bin/nitro_proe_remote.bat'
fileName = 'kr_du_13k1.prt'
worikngPath = 'D:/API/'
def basicParameters():
    H = 200     # HEIGHT MODEL
    W = 500     # WIDTH MODEL
    D = 45      # DEPTH MODEL
    T_H = 75    # HEIGHT TEXT
    T_D = 25    # DEPTH TEXT
    T_L = 15    # LEFT POSITION TEXT
    Center = (float(H)-float(T_H))/2 #CENTER TEXT
    return H, W, D, T_H, T_D, T_L, Center


def userParameters():
        print("REMEMBER THAT PARAMETERS MUST BE GREATER THAN 0!")
        H = float(input("Modify height model: "))
        W = float(input("Modify width model: "))
        D = float(input("Modify depth: "))
        T_H = float(input("Modify height text: "))
        T_D = float(input("Modify depth text: "))
        T_L = float(input("Modify left position text: ")) 
        Center = (float(H)-float(H))/2
        if H < 0 or W < 0 or D < 0 or T_H < 0 or T_D < 0 or T_L < 0:
            print("One of the parameters you specified is less than zero, correct it!")
            userParameters()
        else:
            return H, W, D, T_H, T_D, T_L, Center


def creoDimension(Parameters):
    c.dimension_set('d3', float(Parameters[0]))
    c.dimension_set('d6', float(Parameters[1]))
    c.dimension_set('d4', float(Parameters[2]))
    c.dimension_set('d17', float(Parameters[3]))
    c.dimension_set('d8', float(Parameters[4]))
    c.dimension_set('d18', float(Parameters[5]))
    c.dimension_set('d19', Parameters[6])
    c.file_regenerate()  


def dimensionSet():
    os.system('cls')
    userInput = input("Do you want to modify paramaters (y/n)? ")
    userInput
    if userInput == 'y':
        creoDimension(userParameters())
        print('Succesfully updated the models parameters')
    elif userInput == 'n':
        print('Create Model with starts paramaters')
        creoDimension(basicParameters())
    else:
        print('Error: Wrong input, Use y or n! Try again')
        dimensionSet()

def chooseMaterial():
    os.system('cls')
    materials = c.file_list_materials()
    counter = 0
    for x in materials:
        print(str(counter) + " - " + x)
        counter = counter+1

    material = int(input("Select material(number): "))

    c.file_set_cur_material(str(materials[material]))

def changeText():
    os.system('cls')
    text = str(input("Write text: "))
    c.parameter_set("TEXT", text)
    c.file_regenerate()

def authorApi():
    print ("""
                                    _                                               
                        /\         (_)                                              
   ___ _ __ ___  ___   /  \   _ __  _                                               
  / __| '__/ _ \/ _ \ / /\ \ | '_ \| |                                              
 | (__| | |  __/ (_) / ____ \| |_) | |                                              
  \___|_|  \___|\___/_/    \_\ .__/|_|  _               _____        _   _          
 | |           | |/ /        | |   | | (_)             |  __ \      | | | |         
 | |__  _   _  | ' / _ __ _  |_|___| |_ _  __ _ _ __   | |  | |_   _| |_| | ____ _  
 | '_ \| | | | |  < | '__| | | / __| __| |/ _` | '_ \  | |  | | | | | __| |/ / _` | 
 | |_) | |_| | | . \| |  | |_| \__ \ |_| | (_| | | | | | |__| | |_| | |_|   < (_| | 
 |_.__/ \__, | |_|\_\_|   \__, |___/\__|_|\__,_|_| |_| |_____/ \__,_|\__|_|\_\__,_| 
         __/ |             __/ |                                                    
        |___/             |___/                                                     
"""
)

def userChoose():
    print("[1] - Set working path")
    print("[2] - Modify model paramaters & Modify text paramaters")
    print("[3] - Modify text")
    print("[4] - Change the models material")
    print("[q] - Quit / exit the program")
    return input("\nWhat would you like to do? ")

def initCreoApi():
    authorApi()
    userChoose()
    dimensionSet()
    chooseMaterial()
    changeText()
    
#Start programme CREOAPI

initCreoApi()