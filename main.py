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
    H = float(input("Modify height model: "))
    W = float(input("Modify width model: "))
    D = float(input("Modify depth: "))
    T_H = float(input("Modify height text: "))
    T_D = float(input("Modify depth text: "))
    T_L = float(input("Modify left position text: ")) 
    Center = (float(H)-float(H))/2
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


# Clears the terminal screen, and displays a title bar.
os.system('cls')

def dimensionSet():
    userInput = input("Do you want to modify paramaters (y/n)? ")
    if userInput == 'y':
        creoDimension(userParameters())
    elif userInput == 'n':
        print('Create Model with starts paramaters')
        creoDimension(basicParameters())
    else:
        print('Error: Wrong input, Use y or n! Try again')
        dimensionSet()

dimensionSet()

