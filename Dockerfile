FROM quay.io/jupyterhub/jupyterhub:latest

RUN python3 -m pip install --no-cache-dir \
    dockerspawner \ jupyterhub-dummyauthenticator

COPY ./jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
COPY customauthenticator.py /srv/jupyterhub/customauthenticator.py

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
