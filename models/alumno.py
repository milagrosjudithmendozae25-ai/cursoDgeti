class Alumno:
    def __init__(self, nombre, matricula, nss, plantel, calificacion, disciplica):):
        self.nombre = nombre
        self.matricula = matricula
        self.nss = nss
        self.plantel = plantel
        self.calificacion = calificacion
        self.disciplica = disciplica

    def __str__(self):
        return f"Alumno: {self.nombre}, Matrícula: {self.matricula}, NSS: {self.nss}, Plantel: {self.plantel}, Calificación: {self.calificacion}, Disciplina: {self.disciplica}"

        #Logica del negocio, verificamos que este dentro del rango permitido (5 a 10)

        if calificacion < 5 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 5 y 10")
        else:
            self.calificacion = calificacion

            self.disciplica = disciplica
 
 #Devuelve representaciones legible del objeto Alumno, mostrando sus atributos principales.

 def __str__(self):
        return f"Alumno: {self.nombre}, Matrícula: {self.matricula}, NSS: {self.nss}, Plantel: {self.plantel}, Calificación: {self.calificacion}, Disciplina: {self.disciplica}"