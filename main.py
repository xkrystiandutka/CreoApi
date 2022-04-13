#import creopysonApi
import creopyson

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)
c.creo_cd("D:\API")
c.file_open("kr_du_13k1.prt")
c.view_activate("FRONT")

while True:
    try:
        h = float(input("Podaj h"))
        w = float(input("Podaj w"))
        l = float(input("Podaj l"))
        t_h = float(input("Podaj t_h"))
        t_w = float(input("Podaj t_w"))
        t_l = float(input("Podaj t_l"))  
        if h < 0 or w < 0 or l < 0 or t_h < 0 or t_w < 0 or t_l < 0 :
            print("wartości przyjmują wartości ujemne :(, podaj wartości jeszcze raz")
            continue
    except ValueError:  
        print("When I ask for a number, give me a number. Come on!")
    else:
        c.dimension_set('d3', float(h))
        c.dimension_set('d4', float(w))
        c.dimension_set('d6', float(l))
        c.dimension_set('d17', float(t_h))
        c.dimension_set('d8', float(t_w))
        c.dimension_set('d18', float(t_l))

        d19 = (float(h)-float(t_h))/2
        c.dimension_set('d19', d19)

        materials = c.file_list_materials()
        counter = 0
        for x in materials:
            print(str(counter) + " - " + x)
            counter = counter+1

        material = int(input("Wybierz material(liczba):"))

        c.file_set_cur_material(str(materials[material]))

        text = str(input("wpisz tekst: "))
        c.parameter_set("TEXT", text)

        c.file_regenerate()
        break
