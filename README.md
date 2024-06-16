# DriverApp-BE Reyhan Alvaro

Ini adalah aplikasi backend untuk Driver App, dibuat menggunakan Django dan Django REST Framework. 
Aplikasi ini mendukung pendaftaran pengguna, otentikasi dengan JWT, manajemen perjalanan untuk pengguna, dan penerimaan perjalanan untuk driver.


## Fitur

```
- Pendaftaran dan otentikasi pengguna dengan JWT
- Kontrol akses berbasis peran (User dan Driver)
- Manajemen perjalanan (membuat, melihat status, menerima perjalanan)
- Endpoint yang aman menggunakan JWT
- Dokumentasi API dengan Swagger
```

```
## Penggunaan

Setelah menjalankan server development (`python manage.py runserver`), Anda dapat mengakses aplikasi di `http://127.0.0.1:8000`.

```

```
## Endpoint API

### Endpoint Pengguna

- **Mendaftar sebagai pengguna**
    - **URL**: `/api/register/`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
          "username": "johndoe",
          "email": "johndoe@example.com",
          "password": "password123",
          "phone_number": "1234567890",
          "role": "User"
      }
      ```

- **Login sebagai pengguna dan mendapatkan token JWT**
    - **URL**: `/api/login/`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
          "username": "johndoe",
          "password": "password123"
      }
      ```

- **Membuat pesanan perjalanan (autentikasi diperlukan)**
    - **URL**: `/api/trips/`
    - **Method**: `POST`
    - **Authorization**: Bearer Token
    - **Request Body**:
      ```json
      {
          "pickup_location": "Bandung",
          "dropoff_location": "Jakarta"
      }
      ```

- **Melihat status pesanan perjalanan saat ini (autentikasi diperlukan)**
    - **URL**: `/api/trips/status/`
    - **Method**: `GET`
    - **Authorization**: Bearer Token

### Endpoint Driver

- **Mendaftar sebagai driver** (sama dengan pendaftaran pengguna tetapi spesifikkan `"role": "Driver"`)
    - **URL**: `/api/register/`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
          "username": "driver1",
          "email": "driver1@example.com",
          "password": "password123",
          "phone_number": "0987654321",
          "role": "Driver"
      }
      ```

- **Login sebagai driver dan mendapatkan token JWT**
    - **URL**: `/api/login/`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
          "username": "driver1",
          "password": "password123"
      }
      ```

- **Melihat semua pesanan perjalanan yang tersedia (autentikasi diperlukan)**
    - **URL**: `/api/driver/trips/`
    - **Method**: `GET`
    - **Authorization**: Bearer Token

- **Menerima perjalanan (autentikasi diperlukan)**
    - **URL**: `/api/driver/trips/<int:trip_id>/accept/`
    - **Method**: `POST`
    - **Authorization**: Bearer Token
```

```
## Menjalankan Pengujian

Untuk menjalankan pengujian untuk proyek ini, Anda dapat menggunakan framework pengujian bawaan Django. Pastikan semua dependensi terinstal dan virtual environment diaktifkan.
```
