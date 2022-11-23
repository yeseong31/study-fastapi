import os

from dotenv import load_dotenv

# https://velog.io/@yvvyoon/python-env-dotenv
load_dotenv(verbose=True)

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
