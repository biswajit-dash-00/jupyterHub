# Configuration file for JupyterHub
import os
import sys

# Add the directory containing customauthenticator.py to the Python path
sys.path.insert(0, '/srv/jupyterhub')

from customauthenticator import AutoLoginAuthenticator

c = get_config()

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

c.DockerSpawner.image = os.getenv("DOCKER_NOTEBOOK_IMAGE")

network_name = os.getenv("DOCKER_NETWORK_NAME")
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

notebook_dir = os.getenv("DOCKER_NOTEBOOK_DIR")
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

c.DockerSpawner.remove = True

c.DockerSpawner.debug = True

c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

c.JupyterHub.authenticator_class = AutoLoginAuthenticator

# Automatically log in as a predefined user
c.AutoLoginAuthenticator.auto_user = "username"

# Ensure automatic login is enabled
c.Authenticator.auto_login = True

# Optional settings for user management
c.Authenticator.allow_all = True
c.JupyterHub.allow_named_servers = True

admin = os.getenv("JUPYTERHUB_ADMIN")
if admin:
    c.Authenticator.admin_users = {admin}
