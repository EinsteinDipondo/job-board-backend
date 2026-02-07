# 🚀 KenyaJobs Backend API

<div align="center">

[![Django REST Framework](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)](https://jwt.io/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*A robust Django REST Framework backend API for the KenyaJobs platform with comprehensive job management, secure authentication, and application tracking.*

[🌐 Live API](https://job-board-backend-z5ul.onrender.com) • [📚 API Documentation](https://job-board-backend-z5ul.onrender.com/api/docs/) • [🐛 Report Bug](https://github.com/EinsteinDipondo/job-board-backend/issues) • [✨ Request Feature](https://github.com/EinsteinDipondo/job-board-backend/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Links](#quick-links)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [API Usage Examples](#api-usage-examples)
- [Database Models](#database-models)
- [Security Features](#security-features)
- [Deployment](#deployment)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)
- [Monitoring & Logging](#monitoring--logging)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 📖 Overview

**KenyaJobs Backend API** is a production-ready Django REST Framework backend featuring comprehensive job management, secure user authentication, application tracking, and advanced filtering capabilities. The API is designed to serve the KenyaJobs platform with scalability, security, and reliability.

### ✨ Key Highlights
- ✅ JWT-based authentication with role-based access control
- ✅ Full CRUD operations for jobs and applications
- ✅ Advanced filtering, searching, and pagination
- ✅ Comprehensive application tracking system
- ✅ Employer tools for managing postings and applications
- ✅ Production-ready deployment with PostgreSQL
- ✅ Comprehensive API documentation
- ✅ Industry-standard security practices

---

## 🔗 Quick Links

| Resource | URL |
|----------|-----|
| **API Base URL** | `https://job-board-backend-z5ul.onrender.com` |
| **API Documentation** | `https://job-board-backend-z5ul.onrender.com/api/docs/` |
| **GitHub Repository** | `https://github.com/EinsteinDipondo/job-board-backend` |

---

## ✨ Features

### 🔐 Authentication & Security

- **JWT Authentication**: Secure token-based authentication system with access and refresh tokens
- **Role-Based Access Control**: Differentiated permissions for job seekers, employers, and administrators
- **CORS Enabled**: Ready for seamless frontend integration with multiple origins
- **Input Validation**: Comprehensive data validation and sanitization
- **Secure Password Hashing**: Industry-standard password security with PBKDF2

### 📋 Job Management

- **Full CRUD Operations**: Create, read, update, and delete jobs with complete control
- **Advanced Filtering**: Filter by location, employment type, salary range, and remote status
- **Full-Text Search**: Search across job titles, descriptions, and company names
- **Pagination**: Efficient data loading and pagination for large datasets
- **Featured Jobs**: Highlight premium job postings with featured status
- **Job Categories**: Organize jobs by categories for better navigation

### 👥 User Management

- **User Registration & Login**: Secure account creation with email verification ready
- **Profile Management**: Comprehensive user profiles with customizable preferences
- **Application Tracking**: Track all submitted job applications with status updates
- **Employer Profiles**: Dedicated features for company accounts and management
- **User Preferences**: Store user preferences and settings

### 📝 Application System

- **Job Applications**: Submit applications with cover letters and resumes
- **Application Status Tracking**: Monitor applications through multiple stages (pending, reviewed, shortlisted, rejected, hired)
- **Resume Management**: Store and manage resume URLs with applications
- **Cover Letters**: Support for personalized application cover letters
- **Employer Tools**: View, manage, and update application statuses

### 🏢 Company Features

- **Company Profiles**: Detailed company information and branding
- **Job Posting Tools**: Create, edit, and manage multiple job listings
- **Application Management**: Centralized interface for reviewing applications
- **Hiring Pipeline**: Track candidates through hiring stages
- **Basic Analytics**: Monitor job posting performance and application metrics

---

## 🏗️ Architecture

### Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Django** | 5.0.2 | Web framework and ORM |
| **Django REST Framework** | 3.14.0 | RESTful API development |
| **PostgreSQL** | Latest | Production-grade database |
| **SQLite** | Built-in | Development database |
| **JWT (djangorestframework-simplejwt)** | Latest | Token-based authentication |
| **Django CORS Headers** | Latest | Cross-origin request handling |
| **Gunicorn** | Latest | Production WSGI server |
| **Python Decouple** | Latest | Environment variable management |
| **Render.com** | Cloud | Hosting platform |

### Database Schema
