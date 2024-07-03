from jupyterhub.auth import Authenticator
from traitlets import Unicode

class AutoLoginAuthenticator(Authenticator):
    auto_user = Unicode(
        'username',
        config=True,
        help="Automatically log in as this user",
    )

    async def authenticate(self, handler, data=None):
        return self.auto_user
