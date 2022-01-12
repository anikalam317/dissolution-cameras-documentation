# Automated documentation for Python scripts using Sphinx

This repository includes a template for Sphinx documentation that runs in docker through docker-compose.\
Prior launching the service please review the docker-compose.yml, in particular the port number with the HTML documentation (default is set to 8080) and the folder containing the python scripts to be documented.

To bring the system up and running simply point the repository folder within the terminal/command prompt and run:
```
docker-compose up --build
```
Additional pages to the documentation, edits, etc. will automatically update on the HTML page.

The main folders that are monitor by the automated documentation are:
- docs/source
- pythonScripts

This last one can be renamed and its name should be updated in the docker-compose.yml and sphinxConfig.yml
If the conf.py is updated or some changes in the documentation is not appearing after refreshing the web browser, please consider restart the docker container.

Finally, to bring the system up and running and dethatch it from the terminal run:
```
docker-compose up --build -d
```
