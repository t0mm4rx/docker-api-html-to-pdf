# docker-api-html-to-pdf

This is an API that will allow you to serve an API that converts the given URL into a PDF file.
It's lighter and more up-to-date than other available repos.

Runs with ubuntu 20.04 and Python.

## Usage

```sh
# Build and run the API
docker build -t html-to-pdf-api .
docker run -p 8080:5000 html-to-pdf-api

# Client-side
curl localhost:8080/pdf?url=https://google.com&args=-n --viewport-size 1200
```

## Credits

Based on:
- https://github.com/wkhtmltopdf/wkhtmltopdf
- https://github.com/traum-ferienwohnungen/docker-wkhtmltopdf-aas