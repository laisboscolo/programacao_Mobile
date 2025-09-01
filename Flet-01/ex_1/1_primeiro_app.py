# Primeiro programa desenvolvido em Python

import flet as ft

# def : definir
def main(page: ft.Page):

    # configurações básicas
    page.title = "Meu primeiro app Flet"
    page.padding = 20
    # padding = espaçamento interno

    meu_texto = ft.Text(
        value = "Hello Word!",
        size = 24,
        # size = tamanho
        color = ft.Colors.RED,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER
    )

    page.add(meu_texto)
    # page.add(meu_texto) / page=pagina / add = adicione / meu texto

    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com Flet, você pode criar apps incriveis!", size=16, color=ft.Colors.GREEN)
    )

ft.app(target=main)
    
    

