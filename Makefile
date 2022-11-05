.PHONY: website backend scraper es

all: 
	docker compose up -d --build

website:
	docker compose up -d --build website

backend:
	docker compose up -d --build backend

scraper:
	docker compose up -d --build scraper

es:
	docker compose up -d --build elasticsearch

