# 6ª Digitação (Aqui) 🔢 ➖ ➕ 🔄 
import flet as ft

def main(page: ft.Page):
    page.title = "Contador Completo"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    valor_contador = 0

    # Elementos da interface
    display_contador = ft.Text(
        value="0",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE,
        text_align=ft.TextAlign.CENTER
    )

    info_contador = ft.Text(
        value="Contador inciado em 0"
        size=14,
        colors=ft.Colors.GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_display():
        """Atualiza display e cor baseado no valor"""
        display_contador.value = str(valor_contador)

        if valor_contador > 0:
            display_contador.color = ft.Colors.GREEN
            info_contador.value = "Valor positivo"
        elif valor_contador < 0:
            display_contador.color = ft.Colors.RED
            info_contador.value = "Value negativo"
        else:
            display_contador.color = ft.Colors.BLUE
            info_contador.value = "Contador zerado"

        page.update()

    def incrementar(e):
        nonlocal valor_contador
        valor_contador += 1
        atualizar_display()

    def decrementar(e):
        nonlocal valor_contador
        valor_contador -= 1
        atualizar_display()

    def resetar(e):
        nonlocal valor_contador
        valor_contador = 0
        atualizar_display()

    #Botões
    page.add(
        ft.Column(
            controls=[
                ft.Text("🔢 Contador Completo", size=24, weight=ft.FontWeight.BOLD),
                display_contador,
                info_contador,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("➖", on_click=decrementar, width=80, height=80, bgcolor=ft.Colors.RED_400, color =ft.Colors.WHITE),
                        ft.ElevatedButton("➕", on_click)
                    ]
                )
            ]
        )
    )