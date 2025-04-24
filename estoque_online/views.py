from django.shortcuts import render, redirect,get_object_or_404
from .models import cadastrar_produtos
from django.http import HttpResponse
from django.db import transaction
from openpyxl import Workbook
from django.db.models import Count
from django.http import JsonResponse
from django.db.models import Sum

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
        html = """
            <html>
            <head>
                <meta http-equiv="refresh" content="3;url=/cadastro/">
            </head>
            <body>
                <h1>Produto cadastrado... você será redirecionado em 3 segundos</h1>
            </body>
            </html>
            """
        return HttpResponse(html)
        
    #renderiza se houver uma requisição
    return render(request, 'cadastro.html')



def deletar_produto(request):
        duplicados = cadastrar_produtos.objects.values('nome_do_produto', 'codigo_de_barra')\
            .annotate(total=Count('id')).filter(total__gt=1)

        for d in duplicados:
            registros = cadastrar_produtos.objects.filter(
                nome_do_produto=d['nome_do_produto'],
                codigo_de_barra=d['codigo_de_barra']
            )
            registros.exclude(id=registros.first().id).delete()

        return HttpResponse("Duplicatas removidas com sucesso.")





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
    messagem="" # Feedback para o usuário
    return render(request, 'relatorio.html')
    
def exportar_excel(request):
    produtos = cadastrar_produtos.objects.all()
    
    
    # Criação do arquivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = 'Produtos'
    
    # Cabeçalhos
    ws.append(['ID', 'Nome do Produto', 'Código de Barra', 'Quantidade Total', 'Localização'])
    
    # Dados dos produtos
    for obj in produtos:
        ws.append([obj.id, obj.nome_do_produto, obj.codigo_de_barra, obj.quantidade_total, obj.localizacao])
    
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="produtos.xls"'
    wb.save(response)
    return response


def dashboard_dados(request):
    produtos = cadastrar_produtos.objects.all().values('nome_do_produto', 'quantidade_total')
    
    total_estoque = cadastrar_produtos.objects.aggregate(Sum('quantidade_total'))['quantidade_total__sum'] or 0
    
    dados = {
        'produtos': list(produtos),
        'total_estoque': total_estoque,
        'total_itens': cadastrar_produtos.objects.count()
    }
    return JsonResponse(dados)


