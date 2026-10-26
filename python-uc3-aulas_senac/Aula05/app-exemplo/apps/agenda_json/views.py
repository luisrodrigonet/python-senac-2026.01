import json

from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


def _ler_contatos():
    caminho_json = settings.BASE_DIR / 'static' / 'json' / 'agenda.json'

    # json.load transforma o conteúdo do arquivo em uma lista de dicionários.
    with caminho_json.open(encoding='utf-8') as arquivo:
        return json.load(arquivo)


def _salvar_contatos(contatos):
    caminho_json = settings.BASE_DIR / 'static' / 'json' / 'agenda.json'

    # indent deixa o arquivo organizado para facilitar a leitura dos dados.
    with caminho_json.open('w', encoding='utf-8') as arquivo:
        json.dump(contatos, arquivo, ensure_ascii=False, indent=4)
        arquivo.write('\n')


def agenda_listar(request):
    contatos = _ler_contatos()
    return render(request, 'agenda_json/index.html', {'contatos': contatos})


@require_http_methods(['GET', 'POST'])
def agenda_adicionar(request):
    contato = {
        'nome': '',
        'telefone': '',
        'email': '',
    }
    erro = None

    # GET exibe o formulário; POST indica que ele foi enviado.
    if request.method == 'POST':
        contato = {
            'nome': request.POST.get('nome', '').strip(),
            'telefone': request.POST.get('telefone', '').strip(),
            'email': request.POST.get('email', '').strip(),
        }

        if not contato['nome'] or not contato['telefone'] or not contato['email']:
            erro = 'Preencha todos os campos.'
        else:
            contatos = _ler_contatos()
            contatos.append(contato)
            _salvar_contatos(contatos)
            return redirect('agenda_json:agenda_listar')

    return render(
        request,
        'agenda_json/adicionar.html',
        {'contato': contato, 'erro': erro},
    )


@require_http_methods(['GET', 'POST'])
def agenda_remover(request, contato_id):
    contatos = _ler_contatos()

    if contato_id >= len(contatos):
        raise Http404('Contato não encontrado.')

    # O GET mostra o aviso; a remoção só acontece após confirmação via POST.
    if request.method == 'POST':
        contatos.pop(contato_id)
        _salvar_contatos(contatos)
        return redirect('agenda_json:agenda_listar')

    return render(
        request,
        'agenda_json/remover.html',
        {'contato': contatos[contato_id], 'contato_id': contato_id},
    )


@require_http_methods(['GET', 'POST'])
def agenda_editar(request, contato_id):
    contatos = _ler_contatos()

    if contato_id >= len(contatos):
        raise Http404('Contato não encontrado.')

    contato = contatos[contato_id]
    erro = None

    # GET exibe os dados atuais; POST recebe as alterações do formulário.
    if request.method == 'POST':
        contato = {
            'nome': request.POST.get('nome', '').strip(),
            'telefone': request.POST.get('telefone', '').strip(),
            'email': request.POST.get('email', '').strip(),
        }

        if not contato['nome'] or not contato['telefone'] or not contato['email']:
            erro = 'Preencha todos os campos.'
        else:
            contatos[contato_id] = contato
            _salvar_contatos(contatos)
            return redirect('agenda_json:agenda_listar')

    return render(
        request,
        'agenda_json/editar.html',
        {'contato': contato, 'erro': erro},
    )