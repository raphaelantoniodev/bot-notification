## Bot de Notificação via WhatsApp (Selenium)

- Um bot desenvolvido em Python + Selenium para enviar notificações automáticas via WhatsApp Web.
Ideal para monitorar produtos, serviços ou qualquer evento que exija alerta imediato ao usuário.

- O bot realiza login automático, salva a sessão para evitar novos logins e valida a sessão a cada 5 horas, garantindo funcionamento contínuo e estável.

## Funcionalidades

- Login automático no WhatsApp Web usando Selenium
- Salvamento de sessão/cache, evitando escanear QR Code repetidamente
- Revalidação automática da sessão a cada 5 horas
- Envio de notificações no WhatsApp
- Monitoramento automático de disponibilidade de produtos
- Totalmente automatizado e contínuo

## Tecnologias Utilizadas

- Python
- Selenium WebDriver
- ChromeDriver / FireFox


## Como funciona?

- Ao iniciar, o bot tenta carregar a sessão salva (cookies/cache).
- Caso não exista ou seja inválida, ele faz login manual pelo WhatsApp Web (QR Code).
- Após o login, ele salva os cookies localmente.
- Um loop monitora o produto desejado.
- Assim que o produto estiver disponível, o bot envia uma mensagem automática no WhatsApp.

## A cada 5 horas, ele:

- Revalida a sessão
- Recarrega cookies se necessário
- Garante que o bot não pare

## Instalação
```cmd
git clone https://github.com/SEU_USUARIO/seu-bot-whatsapp.git
cd seu-bot-whatsapp
```


# Instale as dependências:

```pip install -r requirements.txt```


- Certifique-se de instalar o ChromeDriver compatível com sua versão do Chrome (ou outro navegador de sua escolha).

## Como usar

- Execute o script principal:

````python main.py````


## ⚠️ Avisos importantes

- O WhatsApp pode encerrar sessões inativas com frequência; por isso o sistema valida a cada 5 horas.
- Não utilize para spam. Apenas para notificações autorizadas.
- Bots automatizados podem violar os termos do WhatsApp; use por sua conta e risco.