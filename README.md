# Automated documentation for Python scripts using Sphinx

This repository includes a template for Sphinx documentation that runs in docker through docker-compose.\
Prior launching the service please review the docker-compose.yml, in particular the port number with the HTML documentation (default is set to 8080) and the folder containing the python scripts to be documented.

To bring the system up and running simply point the repository folder within the terminal/command prompt and run:
```
docker-compose up --build
```
Additional pages to the documentation, edits, etc. should automatically update on the HTML page.
