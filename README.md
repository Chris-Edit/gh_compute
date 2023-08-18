# Rhino Grasshopper with Python

guides)
1. Rhino7 설치 및 1회 실행
2. compute.Rhino3d 클론
	https://github.com/mcneel/compute.rhino3d
3. VisualStudio 2019 이상에서 src\compute.sln 컴파일 (as debug)
4. http://localhost:8081/version 에서 로컬 서버 도는지 확인
5. https://www.rhino3d.com/compute/login 으로 토큰 복사 .env에 집어넣기
6. pip install dotenv
7. python 3.7~3.10 버전 다운로드 및 가상환경 생성(해당 파이썬 버전에서 진행)
	py -3.7 -m venv rhino_test
8. pip install compute-rhino3d
	https://compute-rhino3d.readthedocs.io/en/latest/

references)
- https://developer.rhino3d.com/guides/compute/
- https://github.com/mcneel/rhino-developer-samples/tree/7/compute/py/SampleGhBasic
