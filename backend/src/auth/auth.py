import json
from flask import request as req, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'udacitycf-fsnd.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'udacity-coffee-shop'

## AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header
def get_token_auth_header():
    # Get authorization header, if not found raise an error
    auth = req.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'code' : 'authorization_header_missing',
            'description' : 'Missing authorization header in request.'
        }, 401)
    # Split the token and make sure it is available and it is a bearer token
    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code' : 'invalid_header',
            'description' : 'Authorization header must be bearer.'
        }, 401)
    elif len(parts) == 1:
        raise AuthError({
            'code' : 'invalid_header',
            'description' : 'Token not found.'
        }, 401)
    elif len(parts) > 2:
        raise AuthError({
            'code' : 'invalid_header',
            'description' : 'Authorization header must be bearer token.'
        }, 401)
    token = parts[1]
    return token


# Check user premissions
def check_permissions(permission, payload):
    # Check for premissions in jwt token
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT.'
        }, 400)
    # Check the array to determine if user has premission
    if permission not in payload['permissions']:
        raise AuthError({
            'code' : 'unauthorized',
            'description' : 'No Premission.'
        }, 403)
    return True


# Verify the JWT token
'''
references:
    https://auth0.com/docs/quickstart/backend/python/01-authorization
    https://github.com/udacity/FSND/blob/master/BasicFlaskAuth
'''
def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code' : 'invalid_header',
            'description' : 'Authorization malformed.'
        }, 401)
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
            break
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code' : 'token_expired',
                'description' : 'Token Expired.'
            }, 401)
        except jwt.JWTClaimsError:
            raise AuthError({
                'code' : 'invalid_claims',
                'description' : 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
            'code': 'invalid_header',
            'description': 'Unable to find the appropriate key.'
        }, 400)


# Authentication decorator
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
