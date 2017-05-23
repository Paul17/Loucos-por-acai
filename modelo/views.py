from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'view/index.html')

def menu(request):
    return render(request, 'view/cardapio.html')

def sobre(request):
    return render(request, 'view/sobreNos.html')

def contato(request):
    return render(request, 'view/contato.html')

def login(request):
    return render(request, 'view/login.html')

def index_cliente(request):
    return render(request, 'view/indexC.html')

def menu_cliente(request):
    return render(request, 'view/cardapioC.html')

def sobre_cliente(request):
    return render(request, 'view/sobreNosC.html')

def contato_cliente(request):
    return render(request, 'view/contatoC.html')

def perfil_cliente(request):
    return render(request, 'view/perfil.html')

def editar_cliente(request):
    return render(request, 'view/editeEdicao.html')

def index_funcionario(request):
    return render(request, 'view/indexF.html')

def menu_funcionario(request):
    return  render(request, 'view/cardapioF.html')

def sobre_funcionario(request):
    return  render(request, 'view/sobreNosF.html')

def contato_funcionario(request):
    return render(request, 'view/contatoF.html')

def vendas_funcionario(request):
    return render(request, 'view/venda.html')

def delete_estoque(request,id):
    estoque = Estoque.objects.filter(id=id)
    estoque.delete()
    return HttpResponseRedirect('/consulta_estoque/')

def new_cliente(request):
    data = {}
    if request.method == "POST":

        cliform = ClienteForm(request.POST)
        usrform = UsuarioForm(request.POST)
        cartaoform = CartaoForm(request.POST)
        endform = EnderecoForm(request.POST)
        telform = TelefoneForm(request.POST)

        if telform.is_valid() and cartaoform.is_valid() and endform.is_valid() and all(
                [usrform.is_valid() for usr in usrform]) and all([cliform.is_valid() for cli in cliform]):
            new_telefone = telform.save()
            new_cartao = cartaoform.save()
            new_end = endform.save()
            for usr in usrform:
                new_user = usrform.save(commit=False)
                new_user.telefone = new_telefone
                new_user.endereco = new_end
                new_user.save()
                for cli in cliform:
                    new_cli = cliform.save(commit=False)
                    new_cli.cartao = new_cartao
                    new_cli.usuario = new_user
                    new_cli.save()

    else:
        cliform = ClienteForm()
        usrform = UsuarioForm()
        cartaoform = CartaoForm()
        endform = EnderecoForm()
        telform = TelefoneForm()

    data['clientes'] = cliform
    data['usuarios'] = usrform
    data['cartoes'] = cartaoform
    data['enderecos'] = endform
    data['telefones'] = telform

    return render(request, 'view/CadF.html', data)

def consultar_cliente(request):
    data = {}
    data['clientes'] = Cliente.objects.all()
    data['usuarios'] = Usuario.objects.all()

    return render(request, 'view/ConsultarCF.html',data)

def editar_cliente_funcionario(request,id):

    data = {}
    cliente = Cliente.objects.get(pk=id)
    usuario = cliente.usuario

    if request.method == "POST":

        cliform = ClienteForm(request.POST, instance=cliente)
        usrform = UsuarioForm(request.POST, instance=usuario)
        cartaoform = CartaoForm(request.POST, instance=cliente.cartao)
        endform = EnderecoForm(request.POST, instance=usuario.endereco)
        telform = TelefoneForm(request.POST, instance=usuario.telefone)

        if telform.is_valid() and cartaoform.is_valid() and endform.is_valid() and all(
                [usrform.is_valid() for usr in usrform]) and all([cliform.is_valid() for cli in cliform]):

            new_telefone = telform.save()
            new_cartao = cartaoform.save()
            new_end = endform.save()

            for usr in usrform:
                new_user = usrform.save(commit=False)
                new_user.telefone = new_telefone
                new_user.endereco = new_end
                new_user.save()

                for cli in cliform:
                    new_cli = cliform.save(commit=False)
                    new_cli.cartao = new_cartao
                    new_cli.usuario = new_user
                    new_cli.save()

    else:
        cliform = ClienteForm(instance=cliente)
        usrform = UsuarioForm(instance=usuario)
        cartaoform = CartaoForm(instance=cliente.cartao)
        endform = EnderecoForm(instance=usuario.endereco)
        telform = TelefoneForm(instance=usuario.telefone)

    data['clientes'] = cliform
    data['usuarios'] = usrform
    data['cartoes'] = cartaoform
    data['enderecos'] = endform
    data['telefones'] = telform

    return render(request, 'view/editeEdicaoF.html', data)

def excluir_cliente(request, id):

    cliente = Cliente.objects.get(pk=id)
    usuario = cliente.usuario
    cartao = cliente.cartao
    telefone = usuario.telefone
    endereco = usuario.endereco

    endereco.delete()
    telefone.delete()
    cartao.delete()
    usuario.delete()
    cliente.delete()

    return HttpResponseRedirect('/funcionario/')


def index_gerente(request):
    return render(request, 'view/indexG.html')

def menu_gerente(request):
    return render(request, 'view/cardapioG.html')

def sobre_gerente(request):
    return render(request, 'view/sobreNosG.html')

def contato_gerente(request):
    return render(request, 'view/contatoG.html')

def new_funcionario(request):
    data = {}

    if request.method == "POST":
        funcform = FuncionarioForm(request.POST)
        usrform = UsuarioForm(request.POST)
        tpfuncform = TipofuncionarioForm(request.POST)
        endform = EnderecoForm(request.POST)
        sform = SituacaoForm(request.POST)
        telform = TelefoneForm(request.POST)

        if telform.is_valid() and sform.is_valid() and endform.is_valid() and tpfuncform.is_valid() and sform.is_valid() and all([usrform.is_valid() for usr in usrform]) and all([funcform.is_valid() for func in funcform]):
            new_telefone = telform.save()
            new_tipo = tpfuncform.save()
            new_end = endform.save()
            new_situacao = sform.save()
            for usr in usrform:
                new_user = usrform.save(commit=False)
                new_user.telefone = new_telefone
                new_user.endereco = new_end
                new_user.save()
                for func in funcform:
                    new_func = funcform.save(commit=False)
                    new_func.situacao = new_situacao
                    new_func.tipo_funcionario = new_tipo
                    new_func.usuario = new_user
                    new_func.save()


    else:
        funcform = FuncionarioForm()
        usrform = UsuarioForm()
        tpfuncform = TipofuncionarioForm()
        endform = EnderecoForm()
        sform = SituacaoForm()
        telform = TelefoneForm()

    data['funcionarios'] = funcform
    data['usuarios'] = usrform
    data['tipos'] = tpfuncform
    data['enderecos'] = endform
    data['situacoes'] = sform
    data['telefones'] = telform

    return render(request, 'view/cadG.html', data)

def consultar_funcionario(request):

    data = {}
    data['funcionarios'] = Funcionario.objects.all()
    data['usuarios'] = Usuario.objects.all()
    return render(request, 'view/ConsultarF.html', data)

def editar_funcionario_gerente(request, id):

    data = {}
    funcionario = Funcionario.objects.get(pk=id)
    usuario = funcionario.usuario

    if request.method == "POST":

        funcform = FuncionarioForm(request.POST, instance=funcionario)
        usrform = UsuarioForm(request.POST, instance=usuario)
        tpfuncform = TipofuncionarioForm(request.POST, instance=funcionario.tipo_funcionario)
        endform = EnderecoForm(request.POST, instance=usuario.endereco)
        sform = SituacaoForm(request.POST, instance=funcionario.situacao)
        telform = TelefoneForm(request.POST, instance=usuario.telefone)

        if telform.is_valid() and sform.is_valid() and endform.is_valid() and tpfuncform.is_valid() and sform.is_valid() and all(
                [usrform.is_valid() for usr in usrform]) and all([funcform.is_valid() for func in funcform]):
            new_telefone = telform.save()
            new_tipo = tpfuncform.save()
            new_end = endform.save()
            new_situacao = sform.save()
            for usr in usrform:
                new_user = usrform.save(commit=False)
                new_user.telefone = new_telefone
                new_user.endereco = new_end
                new_user.save()
                for func in funcform:
                    new_func = funcform.save(commit=False)
                    new_func.situacao = new_situacao
                    new_func.tipo_funcionario = new_tipo
                    new_func.usuario = new_user
                    new_func.save()
        return HttpResponseRedirect("/consultarFunc/")

    else:
        funcform = FuncionarioForm(instance=funcionario)
        usrform = UsuarioForm(instance=usuario)
        tpfuncform = TipofuncionarioForm(instance=funcionario.tipo_funcionario)
        endform = EnderecoForm(instance=usuario.endereco)
        sform = SituacaoForm(instance=funcionario.situacao)
        telform = TelefoneForm(instance=usuario.telefone)

    data['funcionarios'] = funcform
    data['usuarios'] = usrform
    data['tipos'] = tpfuncform
    data['enderecos'] = endform
    data['situacoes'] = sform
    data['telefones'] = telform

    return render(request, 'view/editeEdicaoG.html', data)

def excluir_funcionario_gerente(request, id):

    funcionario = Funcionario.objects.get(pk=id)
    usuario = funcionario.usuario
    tipo = funcionario.tipo_funcionario
    situacao = funcionario.situacao
    telefone = usuario.telefone
    endereco = usuario.endereco

    endereco.delete()
    telefone.delete()
    situacao.delete()
    tipo.delete()
    usuario.delete()
    funcionario.delete()

    return HttpResponseRedirect('/consultarFunc/')

def consultar_historico(request):
    return render(request, 'view/consultarH.html')

def vendas_gerente(request):
    return render(request, 'view/vendaG.html')

def consulta_estoque(request):
    data = {}
    data['estoques'] = Estoque.objects.all()
    return render(request,'view/ConsultarE.html',data)


def edita_estoque(request,pk):

    data = {}
    estoque = get_object_or_404(Estoque, pk=pk)

    if request.method == "POST":
        form = EstoqueForm(request.POST, instance=estoque)

        if form.is_valid():
            form.save()
    else:
        form = EstoqueForm(instance=estoque)

    data['form'] = form

    return render(request, 'view/editeEdicaoE.html', data)


def new_estoque(request):
    data = {}

    if request.method == "POST":
        form = EstoqueForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = EstoqueForm()

    data['form'] = form

    return render(request, 'view/cadE.html', data)

