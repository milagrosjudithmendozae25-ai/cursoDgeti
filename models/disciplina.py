def __init__(self, nombre, idDisciplina=None):
    self.nombre = nombre
    self.idDisciplina = idDisciplina

    def __str__(self):
        return f"Disciplina: {self.idDisciplina} - {self.nombre}"