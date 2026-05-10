# Microservices System (Coffee Shop API)

[![Python CI Application](https://github.com/IrynaHrechyn/finalwork/actions/workflows/python-app.yml/badge.svg)](https://github.com/IrynaHrechyn/finalwork/actions/workflows/python-app.yml)

Система з двох мікросервісів на FastAPI, що демонструє роботу контейнеризації через Docker та автоматизацію CI/CD процесів.

### 📌 Основний функціонал
* **Inventory Service** (Порт 8002): Керування залишками товарів. Дані персоналізовано (N=2).
* **Order Service** (Порт 9002): Обробка замовлень та взаємодія з Inventory через внутрішню мережу Docker.

### 🛠 Стек технологій
* **Backend**: Python 3.10 (FastAPI)
* **DevOps**: Docker, Docker Compose
* **CI/CD**: GitHub Actions, Newman (Postman CLI)
* **Quality**: Flake8 (PEP8)
  
### 📂 Структура проєкту
Репозиторій організовано за мікросервісним принципом, де кожен компонент має власну директорію та оточення:

* **.github/workflows/** — конфігурації автоматизації (CI/CD пайплайни для перевірки коду та запуску тестів).
* **inventory_service/** — мікросервіс складського обліку (код, залежності та логіка N=2).
* **order_service/** — мікросервіс обробки замовлень (включає логіку міжсервісної взаємодії).
* **collection.json** — колекція Postman-запитів для автоматизованого тестування API через Newman.
* **docker-compose.yml** — файл оркестрації, що описує запуск та мережевий зв'язок між контейнерами.
* **README.md** — технічна документація проєкту.
  
### 🚀 Запуск та тестування

**1. Розгортання контейнерів:**
```bash
docker compose up -d --build
```
**2. Запуск автоматизованих API-тестів:**
```bash
npx newman run collection.json
```
### 🔐 CI/CD Пайплайн
В репозиторії налаштовано автоматичний Workflow, який при кожному push або pull request виконує:

  1. **Linting**: Перевірка коду на відповідність стандарту PEP8.
  2. **Security**: Тестування доступу до конфіденційних даних через GitHub Secrets.
  3. **Integration Tests**: Автоматичне розгортання середовища та проходження інтеграційних тестів.

Гілка main захищена правилами Branch Protection: злиття коду можливе лише після успішного проходження всіх етапів перевірки.
