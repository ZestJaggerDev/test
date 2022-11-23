from functools import reduce
Alumnos = [
    {'Alumno': 'Alvaro', 'Edad': 22, 'Sexo': 'F', 'Calificación': 72},
    {'Alumno': 'Ricardo', 'Edad': 25, 'Sexo': 'M', 'Calificación': 88},
    {'Alumno': 'Santiago', 'Edad': 25, 'Sexo': 'M', 'Calificación': 77},
    {'Alumno': 'Jessi', 'Edad': 12, 'Sexo': 'F', 'Calificación': 90},
    {'Alumno': 'Angel Rodrigo', 'Edad': 19, 'Sexo': 'M', 'Calificación': 75},
    {'Alumno': 'Manuel', 'Edad': 20, 'Sexo': 'M', 'Calificación': 90},
    {'Alumno': 'Audel', 'Edad': 22, 'Sexo': 'M', 'Calificación': 90},
    {'Alumno': 'Edgar Paulo', 'Edad': 25, 'Sexo': 'M', 'Calificación': 10},
    {'Alumno': 'Carla Jacqueline', 'Edad': 24, 'Sexo': 'M', 'Calificación': 99},
    {'Alumno': 'Valentin ', 'Edad': 23, 'Sexo': 'M', 'Calificación': 82},
    {'Alumno': 'Alejandro', 'Edad': 20, 'Sexo': 'M', 'Calificación': 100},
    {'Alumno': 'Esteban', 'Edad': 18, 'Sexo': 'M', 'Calificación': 66},
    {'Alumno': 'Briant', 'Edad': 22, 'Sexo': 'M', 'Calificación': 40},
    {'Alumno': 'Alejandrina', 'Edad': 20, 'Sexo': 'M', 'Calificación': 96},
    {'Alumno': 'José Eduardo', 'Edad': 18, 'Sexo': 'M', 'Calificación': 70},
    {'Alumno': 'Manelick', 'Edad': 20, 'Sexo': 'M', 'Calificación': 70},
]
opcion = input('Elija una opcion: (Mujeres,Hombres,PMujeres,PHombres,Mayores)');
if opcion == 'Mujeres':
    mujeres = list(filter(lambda x:x['Sexo']=='F',Alumnos))
    print("Sexo Femenino: ", mujeres)
    
if opcion == 'Hombres':
    hombres = list(filter(lambda x:x['Sexo']=='M',Alumnos))
    print('Sexo Masculino: ', hombres)

elif opcion == 'PMujeres':
    promedioM = list(filter(lambda x:x['Sexo']=='F',Alumnos))
    Calificación = reduce(lambda x, y: x + y['Calificación'], promedioM,0)
    promedio = Calificación/len(promedioM)
    print('Promedui de mujeres: ',promedio)
    
elif opcion == 'PHombres':
    promedioH = list(filter(lambda x:x['Sexo']=='M',Alumnos))
    edad = reduce(lambda x, y: x + y['Edad'], promedioH,0)
    promedio = edad/len(promedioH)
    print('Promedio de hombres:', promedio)

if opcion == 'Mayores':
    Mayores = list(filter(lambda x:x['Edad'] >22,Alumnos))
    promedio= (Mayores)
    print(Mayores)
