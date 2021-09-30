from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

def get_token_for_user(user):
    return (AccessToken.for_user(user), None)
   