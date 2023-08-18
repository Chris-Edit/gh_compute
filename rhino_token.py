from dotenv import load_dotenv
import os

# .env 파일 만들고
# token = "토큰" 작성 https://www.rhino3d.com/compute/login

# load .env
load_dotenv()
token = os.environ.get('token')

# print(token)
