import csv

from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

def _ler_contatos():
    caminho_csv = settings.BASE_DIR / 'static' / 'csv' / 'agenda.csv'

    # O DictReader usa os nomes do cabeçalho como chaves de cada contato.
    with caminho_csv.open(encoding='utf-8', newline='') as arquivo:
        return list(csv.DictReader(arquivo))


def _salvar_contatos(contatos):
    caminho_csv = settings.BASE_DIR / 'static' / 'csv' / 'agenda.csv'
    # Estes nomes precisam corresponder às colunas do arquivo CSV.
    campos = ('nome', 'telefone', 'email')

    with caminho_csv.open('w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        # Regrava a lista completa, incluindo o cabeçalho e todos os contatos.
        escritor.writerows(contatos)


def agenda_listar(request):
    contatos = _ler_contatos()
    return render(request, 'agenda/index.html', {'contatos': contatos})


@require_http_methods(['GET', 'POST'])
def agenda_adicionar(request):
    contato = {
        'nome': '',
        'telefone': '',
        'email': '',
    }
    erro = None

    # GET mostra o formulário; POST indica que ele foi enviado.
    if request.method == 'POST':
        # strip remove espaços extras digitados no começo ou no fim dos campos.
        contato = {
            'nome': request.POST.get('nome', '').strip(),
            'telefone': request.POST.get('telefone', '').strip(),
            'email': request.POST.get('email', '').strip(),
        }

        # Não salva o contato enquanto algum campo obrigatório estiver vazio.
        if not contato['nome'] or not contato['telefone'] or not contato['email']:
            erro = 'Preencha todos os campos.'
        else:
            contatos = _ler_contatos()
            contatos.append(contato)
            _salvar_contatos(contatos)
            return redirect('agenda:agenda_listar')

    return render(
        request,
        'agenda/adicionar.html',
        {'contato': contato, 'erro': erro},
    )


@require_http_methods(['GET', 'POST'])
def agenda_remover(request, contato_id):
    contatos = _ler_contatos()

    # O contato_id representa a posição do contato na lista lida do CSV.
    if contato_id >= len(contatos):
        raise Http404('Contato não encontrado.')

    # A confirmação é enviada por POST; o GET apenas exibe o aviso.
    if request.method == 'POST':
        contatos.pop(contato_id)
        _salvar_contatos(contatos)
        return redirect('agenda:agenda_listar')

    return render(
        request,
        'agenda/remover.html',
        {'contato': contatos[contato_id], 'contato_id': contato_id},
    )


def agenda_editar(request, contato_id):
    contatos = _ler_contatos()

    # Se a posição não existir na lista, não há contato para editar.
    if contato_id >= len(contatos):
        raise Http404('Contato não encontrado.')

    contato = contatos[contato_id]
    erro = None

    # GET exibe os dados atuais; POST recebe as alterações do formulário.
    if request.method == 'POST':
        # strip remove espaços extras digitados no começo ou no fim dos campos.
        contato = {
            'nome': request.POST.get('nome', '').strip(),
            'telefone': request.POST.get('telefone', '').strip(),
            'email': request.POST.get('email', '').strip(),
        }

        # Evita substituir os dados atuais por um cadastro incompleto.
        if not contato['nome'] or not contato['telefone'] or not contato['email']:
            erro = 'Preencha todos os campos.'
        else:
            contatos[contato_id] = contato
            _salvar_contatos(contatos)

            return redirect('agenda:agenda_listar')

    return render(
        request,
        'agenda/editar.html',
        {'contato': contato, 'erro': erro},
    )