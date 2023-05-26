from django.http import HttpResponseNotFound, Http404
from django.shortcuts import HttpResponse, redirect


def index(request): #HttpRequest
    return HttpResponse('Страница приложения main (insurance_firm)')


def company_branch(request, branch):
    return HttpResponse(f'<h1>Информация о страховых агентсвах</h1><p>{branch}</p>')


def insurance_type(request, ins_type):
    return HttpResponse(f'<h1>Виды страхования</h1><p>{ins_type}</p>')


def info_client(request, client):
    return HttpResponse(f'<h1>Информация о клиенте</h1><p>{client}</p>')


def insurance_contract(request, contract):
    return HttpResponse(f'<h1>Информация о контракте</h1><p>{contract}</p>')


def info_object(request, i_object):
    return HttpResponse(f'<h1>Информация об объекте страхования</h1><p>{i_object}</p>')


def insurance_agent(request, agent):
    return HttpResponse(f'<h1>Информаия об агенте страховой фирмы</h1><p>{agent}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
