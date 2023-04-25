# URLShortener

## How to build the app

### Docker Version

1. You must have Docker and Docker Compose installed
2. To run the app use the following commands

```bash
Using the latest version
docker compose up -d --build

Using previous versions
docker-compose up -d --build
```

3. The app will be available on port 5000


### Manual Version

1. You must have python(preferably the latest version) and pip installed
2. Install all the dependencies using the requirements.txt file

```bash
pip install -r requirements.txt
```

3. After the installation is done run the app using the python command

```
python main.py
```

4. The app will be available on port 5000

## Algorithm to shorten the URL

1. I first compute a SHA-256 hash of the URL
2. I convert the hash to a base 64 string and afterwards to a base62 string
3. For the base62 encoding i use various characters
4. Also i convert the base64 string to an integer
5. Finally i convert the integer to a base62 string and i return it

## Endpoints

```bash
/api/v1/url/shorten
Recieves an url in the body, shortens it and stores it in the database, returns the shorten url

/api/v1/url/top
Returns the top visited urls

/api/v1/url/visit/<shortUrl>
Recieves the short url as a parameter and redirects to the longUrl
```