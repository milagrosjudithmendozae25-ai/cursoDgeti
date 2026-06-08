# controlers/disciplinas_controller.py
from models.Disciplinas_dao import DisciplinaDAO

class DisciplinasController:
    def__init__(self, vista):
        # Creamos una instancia de nuestro DAO para cominicarnos con la base de datos
        self.dao = DisciplinaDAO()

        def registrar_disciplina(self, nombre):
            """Logica del negocio y control para dar de alta una dissciplina."""
            # Validacion simple de logica de negocio: ¡que el nombre no este vacio!
            if not nombre or nombre.strip()) == "":
                self.vista.mostrar_mensaje("Eror: El nombre de la disciplina no puede estar vacío.", es_error=True)
                return

                try:
                    # Si todo esta bie, llamamos al modelo para intertar
                    self.dao.insertar(nombre.strip())
                    self.vista.mostrar_mensaje(f"¡Disciplina '{nombre}' registrada con exito!")
                    self.vista.limpiar_formulario_disciplina() # Le pedimos a la vista que limpie su caja de texto
                except Exception as e:
                    self.vista.mostrar_mensaje(f"Error al guardar en la base de datos (e)", es_error=True)

                    # Funcion ara modificar una disciplina, recibe el id de la disciplina a modificar y el nuevo nombre que se le quiere poner
        def modificar_disciplina(self, id_disciplina, nuevo_nombre):
            """Logica para actualizar el nombre de una disciplina."""
            if not nuevo_nombre or nuevo_nombre.strip() == "":
                self.vista.mostrar_mensaje("Error: El nuevo nombre de la disciplina no puede estar vacío.", es_error=True)
                return

                try:
                    self.dao.modificar(id_disciplina, nuevo_nombre.strip())
                  self.vista.mostrar_mensaje("¡Disiciplina actualizada con exito!")
                  self.vista.actualizar_lista_disciplinas() # Le dice a la vista que refresque la pantala
                  except Exception as e:
                    self.vista.mostrar_mensaje(f"Error al modificar: {e}", es_error=True)
                
                # Funcion para eliminar una disciplina, recibe el id de la disciplina a eliminar
                SELF.DAO.ELIMINAR(ID