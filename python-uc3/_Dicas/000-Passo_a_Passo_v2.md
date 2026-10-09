## Passo a passo do projeto Django

### **Passo 00 — Ambiente Virtual**

#### **0.1. Criar o ambiente virtual:**
```bash
python -m venv .venv

```


#### **0.2. Ativar o ambiente virtual:**
* **Windows (Prompt de Comando):** `.venv\Scripts\activate.bat`
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **Linux / macOS:** `source .venv/bin/activate`



#### **0.3. Atualizar o gerenciador e instalar dependências:**
```bash
python -m pip install --upgrade pip
pip install django pillow

```

*(Dica: Adicionar a biblioteca `pillow` é essencial para o uso de `ImageField` em imagens de mídia).*

---

### **Passo 01 — Criação e Configuração do Projeto**

####  **1.1. Criar a pasta do projeto e entrar nela:**
```bash
mkdir app-exemplo
cd app-exemplo

```


#### **1.2. Criar o projeto Django:**
```bash
django-admin startproject config .

```

(O uso do ponto `.` no final evita a duplicação de pastas raiz, mantendo o arquivo `manage.py` no diretório corrente).


#### **1.3. Ajustar as configurações globais (`config/settings.py`):**

**Templates:**
```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'], # Para templates globais
        'APP_DIRS': True, # Busca templates dentro de cada app
        ...
    },
]

```


**Internacionalização e Fuso Horário:**
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

```


**Arquivos Estáticos (CSS, JS, imagens do layout):**
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles' # Para produção / collectstatic

```


**Arquivos de Mídia (Uploads de usuários):**
```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

```




#### **1.4. Ajustar rotas de mídia para ambiente de desenvolvimento (`config/urls.py`):**

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```



---

### **Passo 02 — Criação e Desenvolvimento da Aplicação**

#### **2.1. Criar o aplicativo (App):**
```bash
python manage.py startapp nome_da_app
```


#### **2.2. Registrar o app no projeto imediatamente (`config/settings.py`):**
Adicione `'nome_da_app',` na lista `INSTALLED_APPS`.


#### **2.3. Modelagem de Dados (`nome_da_app/models.py`):**
* Definir as classes/tabelas do banco de dados.


#### **2.4. Criação e execução das migrações:**
```bash
python manage.py makemigrations # Cria os arquivos de migração[cite: 4, 8]
python manage.py migrate        # Aplica as alterações no banco de dados[cite: 4]

```


####  **2.5. Cadastro no painel administrativo (`nome_da_app/admin.py`):**

* Registrar os models com `admin.site.register(MeuModel)` para gerenciá-los via painel web.


#### **2.6. Criação do Administrador (Superusuário):**
```bash
python manage.py createsuperuser

```


####  **2.7. Lógica de Visualização (`nome_da_app/views.py`):**
* Criar as views (funções ou classes) para processar as requisições e consultar os dados.


####  **2.8. Criação do Template HTML:**
* Criar a estrutura: `nome_da_app/templates/nome_da_app/index.html` (mantendo o namespace de templates para evitar conflitos de nomes entre apps).


####  **2.9. Configuração de Rotas da Aplicação (`nome_da_app/urls.py`):**
* Criar o arquivo `urls.py` dentro da pasta do app e mapear as views.



#### **2.10. Conectar as rotas do app no projeto principal (`config/urls.py`):**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nome_da_app.urls')), # Roteamento modular
]

```


#### **2.11. Executar e testar o servidor local:**
```bash
python manage.py runserver

```