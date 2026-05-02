"""
un alumno desea saber cual sera su promedio general en tres materias 
mas dificiles que cursa y cual sera el promedio que obtendra en cada una
de ellas,
estas materias se evaluan como se muestra a continuacion

1. programacion
examen 90%
2 tareas 10%

2. algebra lineal
examen 80%
2 tareas 20%

3. sistemas
examen 85%
2 tareas 15%
"""
def ingresarDatos():
    asignaturas=("Programacion","Algebra Lineal","Ingenieria de Sistemas")
    examenes={}
    practicas={}
    for asig in asignaturas:
        exam=float(input(f"Ingrese la nota del examen de {asig}:"))
        prac=[0]*2
        for i in range(2):
            prac[i]=float(input(f"Ingrese la nota de la práctica {i+1} de {asig}:"))
        examenes[asig]=exam
        practicas[asig]=prac
    return (asignaturas,examenes,practicas)
def promedios():
    (a,e,p)=ingresarDatos()
    promedios={}
    total=0
    for asig in a:
        if(asig=="Programacion"):
            promedios[asig]=e[asig]*90/100+(p[asig][0]+p[asig][1])/2*10/100
        elif(asig=="Algebra Lineal"):
            promedios[asig]=e[asig]*80/100+(p[asig][0]+p[asig][1])/2*20/100
        else:
            promedios[asig]=e[asig]*85/100+(p[asig][0]+p[asig][1])/2*15/100
        total+=promedios[asig]
    total/=3
    return (a,e,p,promedios,total)
def mostrar():
    temp=promedios()
    print(f"Los promedios de las asignaturas son {temp[3]}")
    print(f"el promedio total es {temp[4]}")
mostrar()

