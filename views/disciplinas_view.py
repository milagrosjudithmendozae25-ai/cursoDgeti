import flet as ft
from controller.disciplinas_controller import DisciplinasController

class DisciplinasView(ft.Column):
    def__init__(self, page):
        super().__init__(expand=True, spacing=15)
    
    # Conectamos esta vista con su cotrolador
    self.controller = DiscilinaController(self
                                          
    # Lista visual donde se mostraran las disciplinas registradas
    self.lista_disciplinas = ft.ListView(
        expand=True
        spacing=8
        padding=10
    )

    self.controls = [
         ft.IconButton()
            on_click=lambda _: self._page_red.go("/"),
            tooltips="Volver al panel"
        ),
        ft.Text("Gestión de Disciplinas", size=26, weight=ft,.FontWeight.BOLD),
        ft.Container(expand=True),
        ft.IconButton((
            icon=ft.IsADirectoryError
            toltips="Agregar disciplina",
            on_click=self.abrir_dialogo_agregar
        ),
    ],
    
    self.actualizar_lista  _disciplinas()

def build(self):
    return self
    
# --- Dialogos y acciones de usuario ---
def abrir_dialogo_agregar(self, e):
txt_nombre 0 f.TextField(
    label="Nombre de la nueva disciplina",
    autofocus=True,
    on_submit=lamda _: guardar(None)
)

def guardar(_):
    self.controller.registrar_disciplina(txt_nombre.value)
    self.cerrar_dialogo(dialogo)

dialogo = ft.AlertDialog(
    title=ft.Text("Agregar nueva disciplina"),
    content=txt_nombre,
    actions=[
        ft.TextButton("Cancelar", on_click=lambda _: self.cerrar_dialogo(dialogo)),
        ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE, ON_CLICK=guardar),
    ],
    ACTIONS_ALIGNMENT=FT.MainAxisAlignment.END,
)
self._abrir_dialogo(dialogo)

def abir_dialogo_editar(self, id:disciplina, nombre_actual):
txt_nombre = ft.TextField(
    label="Nuevo nombre",
    value=nombre_actual,
    autofocus=True,
    on_submit=lambda _: guardar(None)
)

def guardar(_):
    self.controller.modificar_disciplina(id_disciplina, txt_nombre.value)
    self.cerrar_dialogo(dialogo)


dialogo = ft.AlertDialog(
    modal=True,
    title=ft.Text("Editar disciplina"),
    content=txt_nuevo_nombre,
    actions=[
        ft.TextButton("Cancelar", on_click=lambda _: self.cerrar_dialogo(dialogo)),
        ft.ElevatedButton("Actualizar", icon=ft.Icons.EDIT, on_click=guardar),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
)
self._abrir_dialogo(dialogo)

def confirmar_eliminar(self, id_disciplina, nombre_disciplina):
    def eliminar(_):
        self.controller.eliminar_disciplina(id_disciplina)
        self.cerrar_dialogo(dialogo)

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Eliminar disciplina"),
            content=ft.Text(f"¿Seguro que deseas eliminar '{nombre}'?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: self.cerrar_dialogo(dialogo)),
                ft.ElevatedButton("Eliminar", icon=ft.Icons.DELETE, on_click=eliminar, bgcolor=ft.colors.RED),

            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self._abrir_dialogo(dialogo)

        # --- Metodos de resupuesta invocados por el cotrolador ---
        def mostrar_mensaje(self, mensaje, es_error=False):
            self._page_ref.snack_bar.open = True
            self._page.ref.update()

        def limpiar_formulario_disciplina(self):
            self.actualizar_lista_disciplinas()

        def actualizar_lista_disciplinas(self):
            disciplinas = self.controller.dao.listar_todas(

            if not disciplinas:
                self.lista_disciplinas.controls = [
                    ft.Container(
                        content=ft.Text("No hay disciplinas registradas."),
                        padding=10
                    )
                ]
            self._page_ref.update()

    # --- Utilidades de dialofgo ---
def _abrir_dialogo(self, dialogo):
    open_method = getattr(self._page_ref, "open", None)
    if callable(open_method):
    try:
        show_dialog_method(dialogo)
        return
    except Exception:
        pass
        
    dialogo.open = True
    try:
        self._page_ref.dialog = dialogo
    except Exception:
        overlay = getattr(self._page_ref, "overlay", None)
        if overlay is not None and dialogo not in overlay:
            overlay.append(dialogo)
    self._page_ref.update()

def _cerrar_dialogo(self, dialogo):
    close_method = getattr(self._page_ref, "close", None)
    if callable(close_method):
        try:
            close_method()
            return
        except Exception:
            pass

    hide_dialog_method()
    return
except Exception:
    pass
    
    dialogo open = False

    overlay = getattr(self._page_ref, "overlay", None)
    if overlay is not None and dialogo in overlay:
        overlay.remove(dialogo)

    self._page_ref.update()