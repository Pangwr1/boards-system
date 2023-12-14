# A Board-Based System

Thanks [Vitor Freitas](https://simpleisbetterthancomplex.com/about/) for providing an amazing tutorials [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/) !!!

BTW, thanks to [Stack Overflow](https://stackoverflow.com/) !!!

## Features

- Three Models:
    - Board
    - Topic
    - Post
- User Sign Up, Login, Logout
- Password Change
- Password Reset by Email
- User Authentication Protection for Operations about create, edit
- Account Personalize Settings
- Humanize Pagination for Topic, Post
- Markdown Render and Editor for Editing Message
- Humanize Time Representation
- Randomize-Generation Gravatar

## TODO

- [ ] Delete Topic or Post
- [ ] Search Bar

## Build

In Ubuntu,

Install python3 and virtual environment:

```bash
$ sudo apt install python3
$ pip install virtualenv
```

Create a virtual development environment:

```bash
$ mkdir Development
$ cd Development
$ virtualenv venv
```

Activate or Deactivate the virtual environment:

```bash
# you can active by
$ source venv/bin/activate
# or you can deactive by
$ deactive
```

> If you active the virtual environemnt, you can see `(venv)` before your terminal prompt.

Install Requirements:

```bash
$ pip install -r requirements.txt
```

Clone this repository:

```bash
$ git clone https://github.com/vanJker/boards-system
$ cd boards-system
```

Make migrations:

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

## Run

In Ubuntu,

Activate the virtual environment

```bash
$ cd Development
$ source venv/bin/activate
```

Run server:

```bash
python manage.py runserver
```

Then, open `http://127.0.0.1:8000/` or `http://localhost:8000/` in your Web browser, you will see the system's webpage.

## References

- [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)

