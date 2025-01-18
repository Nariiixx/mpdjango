from django.shortcuts import render, redirect,get_object_or_404
from .models import cadastrar_produtos
from django.http import HttpResponse
from django.db import transaction

def phome(request):
    #renderiza o arquivo html se houver uma requisição
        return render(request, 'pagina_inicial.html')

def pcadastro(request):
    if request.method == "POST":
        #coleta os dados do form de acordo com os nome do input
        nome_do_produto = request.POST.get('nome_do_produto')
        codigo_de_barra = request.POST.get('codigo_de_barra')
        quantidade_total = request.POST.get('quantidade_total')
        localizacao = request.POST.get('localizacao')
        
        #coloca cada item em seu devido lugar/categoria
        cadastrar_produtos.objects.create(
            nome_do_produto=nome_do_produto,
            codigo_de_barra=codigo_de_barra,
            quantidade_total=quantidade_total,
            localizacao=localizacao
        )
        #mensagem para o user
        return HttpResponse('produtos listados')
    
    #renderiza se houver uma requisição
    return render(request, 'cadastro.html')


def atualizar(request): 
    mensagem = "" # Feedback para o usuário

    if request.method == 'POST':
        produto_id = request.POST.get('id_do_produto')  # Captura o ID do produto
        try:
            # Utiliza uma transação para evitar problemas de bloqueio
            with transaction.atomic():
                # Busca o produto no banco de dados
                produto = get_object_or_404(cadastrar_produtos, id=produto_id)
                
                # Atualiza os campos com os dados do formulário
                produto.nome_do_produto = request.POST.get('nome_do_produto')
                produto.codigo_de_barra = request.POST.get('codigo_de_barra')
                produto.quantidade_total = request.POST.get('quantidade_total')
                produto.localizacao = request.POST.get('localizacao')

                # Salva as alterações no banco
                produto.save()
                mensagem = "Produto atualizado com sucesso!"
        except Exception as e:
            mensagem = f"Erro ao atualizar o produto: {e}"

        return HttpResponse(mensagem)

    return render(request, 'atualiza.html')

def localizar(request):
    #iniciando as variaveis 
    localizaca=0
    nome_do_produto = ""
    if request.method == 'POST':
        #capturando o id do form
        produto_id = request.POST.get('id_do_produto')
        with transaction.atomic():
                #capturando as info do produto
                produto = get_object_or_404(cadastrar_produtos, id=produto_id)
                #pegando somente oque é necessario
                localizaca = produto.localizacao
                nome_do_produto = produto.nome_do_produto
                
        return HttpResponse(f'o produto {nome_do_produto} está localizado em {localizaca}')
    return render(request,'localizar.html' )

def lista_de_produto(request):
    produtos = cadastrar_produtos.objects.all()
    return render(request, 'listaprodutos.html', {'produtos':produtos})

def relatorio(request):
    quantidademaior = cadastrar_produtos.objects.order_by('-quantidade_total').first()
    quantidademenor = cadastrar_produtos.objects.order_by('quantidade_total').first()
    
    contexto = {
        'quantidademaior':quantidademaior,
        'quantidademenor':quantidademenor,
    }
    return render(request, 'relatorio.html', contexto)
    