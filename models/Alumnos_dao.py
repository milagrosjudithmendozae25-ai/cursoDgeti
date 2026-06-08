import sqite3

class AlumnosDAO:
    def __init__(self):
    self.db_name = "concurso_Dgeti.db"

    def insertar(self, alumno_objeto):
        """Recibe un objeto de la clase Alumno y la guarda en la BD."""
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("""
                    INSERT INTO alumnos (matricula, nombre, NSS, plantel, calificacion, id_disciplina)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    alumno_objeto.matricula,
                    alumno_objeto.nombre,
                    alumno_objeto.nss,
                    alumno_objeto.plantel,
                    alumno_objeto.calificacion,
                    alumno_objeto.disciplina.id_disciplina # Guardemos solo el ID de la disciplina, no el objeto completo
                ))
                conexion.commit()
                except sqlite3.IntegrityError as e:
                # Si la matricula ya existe, lanzamos un error de logica del negocio
                raise ValueError("La matrícula ya existe en la base de datos.")

    def modificar(self, alumno_objeto):
        """Recibe un objeto de la clase Alumno con datos actualizados y lo guarda usando su matrícula."""
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE alumnos
                SET nombre = ?, NSS = ?, plantel = ?, calificacion = ?, id_disciplina = ?
                WHERE matricula = ?

            """, (
                alumno_objeto.nombre,
                alumno_objeto.nss,
                alumno_objeto.plantel,
                alumno_objeto.calificacion,
                alumno_objeto.disciplina.id_disciplina, # Guardamos solo el ID de la disciplina, no el objeto completo
                alumno_objeto.matricula
            ))
            conexion.commit()
            except sqlite3.IntegrityError as e:
                # Si la matrícula no existe, lanzamos un error de logica del negocio
                raise ValueError("La matrícula ya se encuentra registrada en el sistema.")

                def modificar(self, alumno_objeto):
        """Recibe un objeto de la clase Alumno con datos actualizados y lo guarda usando su matrícula."""
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE alumnos
                SET nombre = ?, NSS = ?, plantel = ?, calificacion = ?, id_disciplina = ?
                WHERE matricula = ?

            """, (
                alumno_objeto.nombre,
                alumno_objeto.nss,
                alumno_objeto.plantel,
                alumno_objeto.calificacion,
                alumno_objeto.disciplina.id_disciplina, # Condicion clave para saber a quien modificar.
                alumno_objeto.matricula
            ))
            conexion.commit()

            def eliminar(self, matricula):
                """Elimina a un alumno usando su matricula como identificador único."""
                with sqlite3.connect(self.db_name) as conexion:
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM alumnos WHERE matricula = ?", (matricula,))
                    conexion.commit()