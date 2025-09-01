import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro Botão"
    page.padding = 20

    #Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo 👇", size=20, text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """
        Esta função será executada sempre que o botão for clicado.
        O paramêtro 'evento' contém informações sobre o clique.
        """

        #mudando o texto da mensagem
        mensagem.value="Parabéns! Você clicou no botão!"
        mensagem.color=ft.Colors.GREEN

        #IMPORTANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar page.update() para que as mudanças apareçam na tela
        page.update()

    #Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!", 
        on_click=botao_clicado,
        width=200,
        height=50,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    ) 

    #Adicionando os elementos à pagina
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)