# FastAPI Starter

A production-ready FastAPI authentication starter template with comprehensive user management, JWT authentication, and email verification.

**[Repository](https://github.com/sarvagyakrcs/fastapi-starter)**

---

## Features

- **Authentication System**: Registration, login, logout with JWT tokens
- **Email Verification**: OTP-based verification using Resend API
- **Security**: HTTP-only cookies, secure session management
- **Database**: Prisma ORM with PostgreSQL integration
- **Modern Python**: Full async/await support, Pydantic validation, type hints
- **Role-based Access Control**: Multi-role user permission system

---

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js (for Prisma)
- Package manager (bun/npm/yarn)

### Installation

```bash
git clone https://github.com/sarvagyakrcs/fastapi-starter.git
cd fastapi-starter
```

Install dependencies:
```bash
# Node.js packages
bun install
# or npm install / yarn install

# Python dependencies
uv install
```

### Configuration

Create `.env` file:
```env
DATABASE_URL="postgresql://username:password@localhost:5432/your_db"
AUTH_SECRET="your-super-secret-jwt-key"
RESEND_API_KEY="your-resend-api-key"
```

### Setup Database

```bash
prisma generate
prisma db push
```

### Run Application

```bash
chmod +x start.sh
./start.sh
```

**Access Points:**
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Project Structure

```
fastapi-starter/
├── app/
│   ├── controller/          # Request handlers
│   ├── core/               # Core configurations
│   ├── models/             # Data models
│   ├── routes/             # API routes
│   ├── service/            # Business logic
│   ├── templates/email/    # Email templates
│   ├── utils/              # Utility functions
│   └── main.py            # Application entry point
├── prisma/
│   └── schema.prisma      # Database schema
├── pyproject.toml         # Python dependencies
└── start.sh              # Startup script
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| `POST` | `/auth/register` | Register new user | No |
| `POST` | `/auth/login` | User login | No |
| `GET` | `/auth/logout` | User logout | Required |
| `POST` | `/auth/verify-otp` | Verify email OTP | No |

### Request/Response Examples

**Register User**
```bash
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Login User**
```bash
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Verify OTP**
```bash
POST /auth/verify-otp
Content-Type: application/json

{
  "email": "john@example.com",
  "otp": "123456"
}
```

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `AUTH_SECRET` | JWT signing secret key | Yes |
| `RESEND_API_KEY` | Resend API key for emails | Yes |

---

## Development

**Development Server**
```bash
uv run fastapi dev app/main.py
```

**Database Operations**
```bash
# Reset database
prisma db push --force-reset

# View database
prisma studio

# Generate Prisma client
prisma generate
```

**Manual Deployment**
```bash
uv sync
prisma generate
prisma db push
uv run fastapi run app/main.py --host 0.0.0.0 --port 8000
```

---

## Technology Stack

- **Backend**: FastAPI, Python 3.8+
- **Database**: PostgreSQL with Prisma ORM
- **Authentication**: JWT tokens, HTTP-only cookies
- **Email**: Resend API integration
- **Validation**: Pydantic models
- **Package Management**: UV for Python, Bun/NPM for Node.js

---

## Support

If this project helped you, consider supporting the development:

**[Buy me a coffee](https://coff.ee/thesarvagya)**

---

## License

This project is open source and available under the [MIT License](LICENSE).