from social.backends.vk import VKOAuth2
from social.p3 import urlencode, unquote


class MyVKOAuth2(VKOAuth2):
    def auth_url(self):
        """Return redirect url"""
        state = self.get_or_create_state()
        params = self.auth_params(state)
        params.update(self.get_scope_argument())
        params.update(self.auth_extra_arguments())
        params = urlencode(params)
        # if not self.REDIRECT_STATE:
        # redirect_uri matching is strictly enforced, so match the
        # providers value exactly.
        params = unquote(params)
        return '{0}?{1}'.format(self.authorization_url(), params)