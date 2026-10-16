## 1. Rodando o projeto Django

```bash
python .\manage.py runserver 
```

## 2. Criando a aplicação de teste de Loops

```bash
python.exe .\manage.py startapp loops_app
```

### 2.1 Criando a pasta de templates

```text
templates\loops_app
```

### 2.2 Adicionar a aplicação a lista de aplicações do Django

```
config\settings.py
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'loops_app', # <-- Nova aplicação
]
```
