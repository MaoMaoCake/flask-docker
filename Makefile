all:

build:
	docker build --network=host -t local/app .

db:
	docker exec app python initdb.py

start:
	docker run -it --name app -p 3000:3000 local/app