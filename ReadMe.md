# Book Store

### A simple book Store 
<p align="center">
  <img src="https://cdn.pixabay.com/photo/2016/03/26/22/21/books-1281581_960_720.jpg">
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
# Run Server

python manage.py runserver


```

### SITES
- [`book_store/account/templates/login.html`](book_store/account/templates/login.html) - [LOGIN](http://127.0.0.1:8000/account/login)

###cicd test


## **Changelog:** (Example, falls man das brauch z.B zur besseren Nachverfolgung?)
**v2.2 (24 Oct 2021):**
- Added basic support for downloading an entire podcast series.
- Split code into multiple files for easier maintenance.
- Changed initial launch script to app.py
- Simplified audio formats.
- Added prebuild exe for Windows users.
- Added Docker file.
- Added CONTRIBUTING.md.
- Fixed artist names getting cutoff in metadata.
- Removed data sanitization of metadata tags.
