# Book Store

### A simple book Store 
<p align="center">
  <img src="https://raw.githubusercontent.com/JojoNowack/book-store/master_chris/book_store/media/src/main_site.PNG">
</p>

```
Requirements:

Binaries

- Python 3.9 or greaters
- Git**

Python packages:

- pip install -r requirements.txt

```
\*\*Git can be installed via apt for Debian-based distros or by downloading the binaries from [git-scm.com](https://git-scm.com/download/win) for Windows.

### HOW TO USE
```python
# Run Server - 

python manage.py runserver --insecure


```

### SITES
- [`book_store/account/templates/account/login.html`](book_store/account/templates/account/login.html) - [LOGIN](http://127.0.0.1:8000/login)
- [`book_store/account/templates/account/about.html`](book_store/account/templates/account/about.html) - [ABOUT](http://127.0.0.1:8000/about)
- [`book_store/account/templates/account/register.html`](book_store/account/templates/account/register.html) - [REGISTER](http://127.0.0.1:8000/register)
- [`book_store/account/templates/account/profile.html`](book_store/account/templates/account/profile.html) - [LOGIN](http://127.0.0.1:8000/profile)
- [`book_store/account/templates/account/logout.html`](book_store/account/templates/account/logout.html) - [LOGOUT](http://127.0.0.1:8000/logout)
- [`book_store/account/templates/account/meinebuecher.html`](book_store/account/templates/account/meinebuecher.html) - [LOGOUT](http://127.0.0.1:8000/meinebuecher)
- [`book_store/books/templates/`](book_store/books/templates/) - [BOOKS](http://127.0.0.1:8000/)
- [`book_store/books/templates/`](book_store/books/templates/) - [Products](http://127.0.0.1:8000/books/products/)
- [`book_store/order/templates/collection.html`](book_store/books/templates/collection.html) - [QR-Code](http://127.0.0.1:8000/books/products/)
- [`book_store/order/templates/admin_collection.html`](book_store/books/templates/admin_collection.html) - [Admin Seite](http://127.0.0.1:8000/books/products/)




## **Comments / TODO**
- Bücher hinzufügen ( wie viele? )
- Trigger zu Profile max Order
- login verweis
- Tests
- Datenbank anpassen?
- Profile Seite ( verlängern / rückgabe)
- Profile bearbeiten - Passwort und e-mail
- passwort vergessen?
