# Já que nosso teste ainda não teve deploy, vamos simular um sistema de login e logout
# com um servidor de teste. Para isso, vamos utilizar a biblioteca requests para simular

import requests

def simulate_logout_test():
    # Simulação de autenticação
    login_url = "https://sistema-exemplo.com/login"
    payload = {"username": "usuario_teste", "password": "senha_teste"}
    session = requests.Session()
    response = session.post(login_url, data=payload)
    
    if response.status_code != 200:
        return "Falha na autenticação"

    # Simulação de navegação para uma página interna
    internal_page_url = "https://sistema-exemplo.com/pagina-interna"
    response = session.get(internal_page_url)
    
    if response.status_code != 200:
        return "Falha ao acessar página interna"

    # Simulação de logout
    logout_url = "https://sistema-exemplo.com/logout"
    response = session.get(logout_url)
    
    if response.status_code != 200:
        return "Falha ao realizar logout"

    # Verificação de redirecionamento
    if response.url != "https://sistema-exemplo.com/login":
        return "Redirecionamento incorreto"

    # Verificação de sessão encerrada
    response = session.get(internal_page_url)
    if response.status_code != 401:
        return "Sessão não foi encerrada corretamente"

simulate_logout_test()
