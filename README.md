# FastAPI Starter

A production-ready FastAPI authentication starter template providing email verification, JWT tokens, secure cookie-based sessions, and comprehensive user management. The project includes Prisma ORM integration with PostgreSQL, customizable email templates, role-based access control, and a modern Python async architecture.

Repository URL:

[https://github.com/sarvagyakrcs/fastapi-starter](https://github.com/sarvagyakrcs/fastapi-starter)

## Features

* Complete authentication system: registration, login, logout, OTP-based email verification
* JWT token and secure HTTP-only cookie authentication
* Email verification system with Resend API integration
* Prisma ORM with PostgreSQL support
* Pydantic validation and type hints
* Async/await support throughout the codebase
* Role-based access control with support for multiple roles

## Quick Start

### Prerequisites

* Python 3.8+
* PostgreSQL
* Node.js (for Prisma)
* Bun, npm, or yarn

### Installation

```bash
git clone https://github.com/sarvagyakrcs/fastapi-starter.git
cd fastapi-starter
```

Install Node.js packages:

```bash
bun install
# or
npm install
# or
yarn install
```

Install Python dependencies:

```bash
uv install
```

Set up environment variables in a `.env` file:

```env
DATABASE_URL="postgresql://username:password@localhost:5432/your_db"
AUTH_SECRET="your-super-secret-jwt-key"
RESEND_API_KEY="your-resend-api-key"
```

Make the start script executable:

```bash
chmod +x start.sh
```

Set up the database:

```bash
prisma generate
prisma db push
```

Start the server:

```bash
./start.sh
```

Access the API:

* Base URL: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints Overview

### POST `/auth/register`

Register a new user account.

### POST `/auth/login`

Log in an existing user.

### GET `/auth/logout`

Logs out the current user (requires authentication).

### POST `/auth/verify-otp`

Verifies a user account via email OTP.

## Environment Variables

| Variable         | Description                         | Required |
| ---------------- | ----------------------------------- | -------- |
| DATABASE\_URL    | PostgreSQL connection string        | Yes      |
| AUTH\_SECRET     | JWT signing secret                  | Yes      |
| RESEND\_API\_KEY | Resend email API key for email OTPs | Yes      |

## Project Structure

```
fastapi-starter/
├── app/
│   ├── controller/
│   ├── core/
│   ├── models/
│   ├── routes/
│   ├── service/
│   ├── templates/email/
│   ├── utils/
│   └── main.py
├── prisma/
│   └── schema.prisma
├── pyproject.toml
├── start.sh
```

## Deployment

Using the provided script:

```bash
chmod +x start.sh
./start.sh
```

Manual method:

```bash
uv sync
npx prisma generate
npx prisma db push
uv run fastapi run app/main.py --host 0.0.0.0 --port 8000
```

## Development

Run development server:

```bash
uv run fastapi dev app/main.py
```

Reset the database:

```bash
npx prisma db push --force-reset
```

View the database:

```bash
npx prisma studio
```

## API Endpoints Details

### POST `/auth/register`

Registers a new user.

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "message": "User registered successfully. Please check your email for verification."
}
```

### POST `/auth/login`

Logs in an existing user.

**Request Body:**

```json
{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "message": "Logged in successfully."
}
```

### GET `/auth/logout`

Logs out the current user.

**Response:**

```json
{
  "message": "Logged out successfully."
}
```

### POST `/auth/verify-otp`

Verifies an email OTP code.

**Request Body:**

```json
{
  "email": "john@example.com",
  "otp": "123456"
}
```

**Response:**

```json
{
  "message": "Email verified successfully."
}
```
