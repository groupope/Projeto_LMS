from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')
	
def login(request):
	if request.method == "GET":
		return render(request, 'login.html')
	else:
		email = request.POST.get("emailUser")
		senha = request.POST.get("senhaUser")
		if senha == 'teste123':
			print("Usuário ", email, " entrou com sucesso!")
			return render(request, 'index.html')
		else:
			print("Usuário ", email, " digitou a senha errada!")
			return render(request, 'login.html')

def contato(request):
	if request.method == "GET":
		return render(request, 'contato.html')
	else:
		nome = request.POST.get("nome")
		curso = request.POST.get("curso")
		semestre = request.POST.get("semestre")
		print("Nome: ", nome, "\nCurso: ", curso, "\nSemestre: ", semestre)
		return render(request, 'contato.html')