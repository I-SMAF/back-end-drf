<h4>... -Add more files if they’re needed.<br /></h4>
<div>
    <p>

<a href='https://github.com/I-SMAF/back-end-drf/tree/main/project_name'>project_name</a><br />
┃<br />
┣┳ <a href='https://github.com/I-SMAF/back-end-drf/tree/main/project_name/project_name'>project_name</a> (Put all the settings for the app here.)<br />
┃┣ __init__.py<br />
┃┣┳ <a href='https://github.com/I-SMAF/back-end-drf/tree/main/project_name/project_name/settings'>settings</a><br />
┃    ┣ <a href='https://github.com/I-SMAF/back-end-drf/blob/main/project_name/project_name/settings/__init__.py'>__init__.py</a><br />
┃    ┣ base.py<br />
┃    ┣ development.py<br />
┃    ┣ production.py<br />
┃      ...<br />
┃┣ wsgi.py<br />
┃┣ asgi.py (optional)<br />
┃┣ urls.py<br />
┃  ...<br />
┃<br />
┣ api<br />
┃┣ __init__.py<br />
┃  ...<br />
┃┗ urls.py (Use this file to route the apps located under the applications folder.)<br />
┃<br />
┣┳ applications<br />
┃┣ __init__.py<br />
┃┣┳ app1<br />
┃    ┣ models.py (Split the folder and import models in __init__ if necessary.)<br />
┃    ┣ views.py<br />
┃    ┣ serializers.py<br />
┃    ┣ urls.py<br />
┃    ┣┳ test<br />
┃      ...<br />
┃    ┣ api.py <br />
┃      ... <br />
┃  ...<br />
┃<br />
┣┳ utils<br />
┃  ...<br />
...<br />
</p>
</div>
