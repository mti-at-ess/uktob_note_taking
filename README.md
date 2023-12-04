# uktob_note_taking

The project has an application with the support for CRUD operations of Notes entity.

## Installation / Setup
- Install **python v3.9.6**
- Run ```pip install -r requirements.txt``` from root directory.
- For migrations, run ```python manage.py migrate``` from root directory.
- Start the server by ```python manage.py runserver```

## Usage
The notes application is exposed at `/notes` subdomain. In order to interact with CRUD endpoints use below subdomains:
- **List**: _GET_ `/notes`
- **Create**: _POST_ `/notes`
- **Fetch**: _GET_ `/notes/$id`
- **Update**: _PUT_ `/notes/$id`
- **Delete**: _DELETE_ `/notes/$id`
