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

## 3. Movendo do APP para pasta APPS.

- Mover a pasta da aplicação para a pasta "apps"

- Alterar o nome da aplicação no arquivo `apps.py` da aplicação

```python
name = 'apps.loops_app'
```

- Alterar o nome da aplicação no arquivo `settings.py` da pasta "config"

```python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.loops_app',  # <-- Alterar o nome da aplicação
]
```

- Alterar o nome da aplicação no arquivo `urls.py` da pasta config

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.loops_app.urls')), # <-- Ajustar o nome da aplicação
]
```