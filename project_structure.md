project_name
|
|__ project_name (Put all the settings for the app here.)
|    |__ __init__.py
|    |__ settings
|          |__ __init__.py
|          |__ base.py
|          |__ development.py
|          |__ production.py
|           ...
|    |__ wsgi.py
|    |__ asgi.py (optional)
|    |__ urls.py
|     ...
|
|__ api
|  |__ __init__.py
|   ...
|  |__ urls.py (Use this file to route the apps located under the applications folder.)
|
|__ applications
|   |__ __init__.py
|   |__ app1
|    ... |__ models.py (Split the folder and import models in __init__ if necessary.)
|        |__ views.py
|        |__ serializers.py
|        |__ urls.py
|        |__ test
|        |    ...  
|        |__ templates (Optional and not present if the project is API only.)
|        |
|        |__ api.py (Optional and not present if the project is API only.)
|         ... (Add more files if they’re needed.)
|
|__ templates (These general templates are loaded last in the application.)
|
|__ utils
|    ... 
 ...
