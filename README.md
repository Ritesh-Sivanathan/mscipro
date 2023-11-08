# MSCIPro

## Contents
### 1 ... Introduction & Information
### 2 ... Dependencies
### 3 ... Current Languages, Tools and Frameworks
### 4 ... Future Languages, Tools and Frameworks
### 5 ... Structure

# 1 - **Introduction & Information**

### Purpose:
MSCIPro is a tool for specifically STEM students. Currently, MSCIPro is limited to website-only.
It provides valuable resources and information, like problem generators for STEM topics and related sub-topics.
It also provides links to external resources that could be of use.

### About:

Website construction started on August 28th, 2023. The website was created as a side project, which is being used to learn various languages and frameworks used.

# 2 - Dependencies 

### Currently used dependencies and versions

#### Last updated: **November 5th, 2023**

- Python = 3.11.6 
- Flask = 2.3.3 ``` pip install Flask ```
- Flask-SQLAlchemy = 3.1.1 ``` pip install Flask-SQLAlchemy ```
- SQLAlchemy = 2.0.21 ``` pip install SQLAlchemy ```
- Frozen-Flask = 0.18 ``` pip install frozen-flask ```
- alembic = 1.12.1 ``` pip install alembic ```
- Flask-Migrate = 4.0.5 ``` pip install Flask-Migrate ```
- ipython = 8.15.0 ``` pip install ipython ```
- numpy = 1.25.2 ``` pip install numpy ```
- requests = 2.31.0 ``` pip install requests```


# 3 - Current Languages, Tools and Frameworks

### Languages

- HTML
- CSS
- Python
- Javascript

### Frameworks

- Flask

### Tools

- SQLite

# 4 - Future Languages, Tools and Frameworks

### Languages

- All current languages
- +++

### Frameworks

- React (JS)
- Vue.js
- Angular
- NextJS
- Django (not certain)
- Ruby on Rails

# 5 - Structure

Visual Website Structure:

## Homepage
#### Mathematics
###### Arithmetic Generator
#### Science
#### Programming
#### Login
#### Register
#### Contact Us

Each of these pages, excluding the arithmetic generator are accessible through any of the pages.

Logic Website Structure:

All pages and sub-pages are children of the base.html parent.

## base.html
#### - homepage
#### - mathematics
#### - science
#### - programming
#### - login
#### - register
#### - contact us

Logically, all webpages other than base.html are of equal class. Homepage is the same class as mathematics, for example, because it extends the base.html template. The landing page is homepage.html, however.


