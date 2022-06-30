import creopyson
import os

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)
c.creo_cd("D:\API")
c.file_open("model.prt")
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
        Center = (float(H)-float(T_H))/2
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
    if userInput == 'y':
        creoDimension(userParameters())
        print('Succesfully updated the models parameters')
        userChoose()
    elif userInput == 'n':
        print('Create Model with starts paramaters')
        creoDimension(basicParameters())
        userChoose()
    else:
        print('Error: Wrong input, Use y or n! Try again')
        dimensionSet()

def chooseMaterial():
    materials = c.file_list_materials()
    counter = 0
    for x in materials:
        print(str(counter) + " - " + x)
        counter = counter+1

    material = int(input("Select material(number): "))
    if material > -1 and material < 11: 
        c.file_set_cur_material(str(materials[material]))
        os.system('cls')
        userChoose()
    else:
        os.system('cls')
        print("Enter a number between 1 and 10")
        chooseMaterial()

def changeText():
    os.system('cls')
    text = str(input("Write text: "))
    c.parameter_set("TEXT", text)
    c.file_regenerate()
    userChoose()

def setCreoWorkingPath():
    os.system('cls')
    userInput = input("Do you want to modify working directory (y/n)? ")
    if userInput == 'n':
        worikngPath = 'D:/API/'
        print("he path of the working directory remains the same!")
        userChoose()
    elif userInput == 'y':
        newWorkingPath = input('Set new working path for creo:')
        c.creo_cd(newWorkingPath)        
        userChoose()
    else:
        print('Error: Wrong input, Use y or n! Try again')
        setCreoWorkingPath()

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
    authorApi()
    print("[1] - Set working path")
    print("[2] - Modify model paramaters & Modify text paramaters")
    print("[3] - Modify text")
    print("[4] - Change the models material")
    print("[q] - Quit / exit the program")
    task = input("\nWhat would you like to do? ")
    if task == '1':
        print("Set working path")
        setCreoWorkingPath()
    elif task == '2':
        print("Modify model paramaters & Modify text paramaters")
        dimensionSet()
    elif task == '3':
        print("Modify text")
        changeText()
    elif task == '4':
        print("Change the models material")
        chooseMaterial()
    elif task == 'q':
        exit()
    else:
        print("Error: Wrong input! Try again")

def initCreoApi():
   userChoose()
  
#Start programme CREOAPI

initCreoApi()