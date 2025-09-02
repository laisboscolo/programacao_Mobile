# 10a Desafio 2 Digitação (Aqui) 🕶️ ⌚ 🎧 📚 👕 👟 💻 📱 ❌ 🎉 ⚠️ 🛍️ 🔄
import flet as ft

def main(page: ft.Page):
    # configuraçoes inicias da pagina
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO #permite rolagem automatica
    page.bgcolor = ft.Colors.GREY_50 #cor de funda pagina \ pq esses numeros?

    # Estado da aplicação - variaveis que armazenam dados do carrinho
    carrinho = [] #lista que armazena os produtos no carrinho
    total_carrinho = 0.0 #valor total dos produtos no carrinho

    # elementos da interface (declarados primeiro para serem acessiveis nas funçoes)
    # grid que exibe os produtos em formato de grade
    area_produtos = ft.GridView(
        expand=1, 
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=0.9,
        spacing=15,
        run_spacing=15
    )
    # Textos que mostram informaçoes do cacrrinho
    contado_carrinho = ft.Text("carrinho(0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    #Lista que exibe os itens do carrinho
    lista_carrinho = ft.ListView(height=150, spacing=5)
    #Texto para exibir notificações ao usuario
    notificacao = ft.Text("", size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    def adicionar_ao_carrinho(nome, preco):
        """Adiciona um produto ao carrinho de compras"""
        nonlocal total_carrinho 
        carrinho.append({"nome": nome, "preco": preco})
        # soma o preço do produto ao total
        total_carrinho += preco
        # atualiza a interface do carrinho
        atualizar_carrinho()
        #mostrar notificaçao de sucesso
        mostrar_notificacao(f"✅ {nome} adicionado!")

    def criar_card_produto(nome, preco, categoria,emoji, cor):
        """Criar um card de produto reutilizável que funciona como botão"""
        return ft.Container(
            content=ft.column([
                #emoji do produto
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                #nome do produto
                ft.Text(
                    nome,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                # preço do produto
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignmnt.CENTER,
            spacing=10
            ),
            bgcolor=cor,
            padding=20,
            border_radius=15,
            width=160,
            height=180,
            # sombra para dar profundidade
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            # Tornando o card inteiro clicavel - chama funçao de adicionar ao carrinho
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            # efeito visual de ondulaçao ao clicar (ripple effect)
            ink=True,
            # Animação suave para transiçoes
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT)
        )
    
    # Lista de produtos disponiveis na loja
    # cada produto e´um dicionario com informaçoes como nome, preço, categoria, emoji e cor
    produtos = [
        {"nome":"Smartphone", "preco": 899.99, "categoria": "Eletrônicos", "emoji": "📱", "cor":ft.Colors.BLUE_600},
        {"nome": "Notebook", "preco": 2499.90, "categoria": "Eletrônicos", "emoji": "💻", "cor":ft.Colors.PURPLE_600},
        {"nome": "Tênis", "preco": 299.99, "categoria": "Roupas", "emoji": "👟", "cor": ft.Colors.GREEN_600},
        {"nome": "Camisa", "preco": 89.99, "categoria": "Roupas", "emoji": "👕", "cor": ft.Colors.ORANGE_600},
        {"nome": "Livro", "preco": 45.00, "categoria": "Educação", "emoji": "📚", "cor": ft.Colors.BROWN_600},
        {"nome": "Fone", "preco": 199.99, "categoria": "Eletrônicos", "emoji": "🎧", "cor":ft.Colors.RED_600},
        {"nome": "Relógio", "preco": 350.00, "categoria": "Acessórios", "emoji": "⌚", "cor": ft.Colors.TEAL_600},
        {"nome": "Óculos", "preco":250.00, "categoria": "Acessórios", "emoji": "🕶️", "cor": ft.Colors.INDIGO_600},
    ]

    # Elementos de filtro da inetrface
    # Dropdown para filtrar por categoria
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        width=150,
        value="Todas", #valor padrao
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Eletrônicas"),
            ft.dropdown.Option("Roupas"),
            ft.dropdown.Option("Educação"),
            ft.dropdown.Option("Acessórios")
        ]
    )

    #Dropdown para filtrar por faixa de preço
    filtro_preco = ft.Dropdown(
        label="Preço",
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 100"),
            ft.dropdown.Option("R$ 100-500"),
            ft.dropdown.Option("Acima R$ 500")
        ]
    )

    # Campo de texto para buscar produtos por nome
    campo_busca = ft.TextField(
        label="Buscar produto",
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )
    
    def remover_do_carrinho(index):
        """Remove um produto especifico do carrinho usando seu indice"""
        nonlocal total_carrinho #permite modificar a variavel global total_carrinho
        # Verifica se o indice é valido(existe na lista)
        if 0 <= index <len(carrinho):
            # remove o produto da lista e armazena os dados dele
            produto = carrinho.pop(index)
            # subtrai o preço do produto do total
            total_carrinho -= produto["preco"]
            # Mostra notificação de remoçao
            mostrar_notificacao(f"❌ {produto['nome']} removido!")

    def atualizar_carrinho():
        """Atualiza a exibição do carrinho na interface"""
        # atualiza o contador de itens no carrinho
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        #atualiza o valor total formatado em reais
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"

        #limpa lista visual do carrinho
        lista_carrinho.controls.clear
