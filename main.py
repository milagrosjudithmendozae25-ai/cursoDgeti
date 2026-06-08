import flet as ft

from views.PanelAdministrador_view import DisciplinasView
from views.disciplinas_view import DisciplinasView
from models.database import crear_tables

def main(page: ft.Page):
    page.title = "App Concurso Civico - DGETI"
    page.window_width = 800
    page.window_height = 600
    # Tema institucional DEGETI guinda principal tomando del sitio de referencia)
    page.theme_mode = ftThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="#611232")
    page.bgcolor ="#F7F4EF"



    def route_change(e):
        ruta = page.route
        print(f"---DISPARANDO RUTEADOR_ {ruta}---")

        # Limpiamos las vistas en el stack ´para una SPA optima
        page.views.clear

        # 1. Tu rut principal que carga el panel que creaste
        if ruta == "/":
            page.views.append(
                ft.View(
                   route="/",
                   controls=[PanelAdministradorView(page)]
                   vertial_alignment=ft.MainAxisAlignment.CENTER
                   horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        # 2. Ruta para gestionar alumnos


        # 3. Ruta para gestionar disciplinas
        if ruta == "/gestionar_disciplina":
            page.views.append(
                ft.View(
                   route="/gestionar_disciplina",
                   controls=[DisciplinasView(page)]
                   padding=20,
                   scroll=ft.ScrollMode.AUTO,
                )
            )

            page.update()

        # Asignamos el evento del ruteador
        page.on_route_change = route_change

        # Aseguramos la ruta raiz por defecto
        if not page.route:
            page.route = "/"

            #Forzamos la ejecucion  manual la primera vez
            route_change(None)

if __name__ == "__main__":
    crear_tables()
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)