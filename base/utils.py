from django.contrib.auth.models import User

def validar_usuario(email,senha1,senha2):
    usuario = User.objects.filter(username=email)
    print("usuario",usuario)
    if usuario.exists():
        mensagem = {
            "tipo_status":"Erro",
            "Mensagem":" E-mail já cadastrado, por favor tente outro e-mail!",
            "color":"red"
        }
        return mensagem
    if not senha1 == senha2:
        print("entrou aqui")
        mensagem = {
            "tipo_status":"Erro",
            "Mensagem":" As senhas não são iguais!",
            "color":"red"
        }
        return mensagem    
