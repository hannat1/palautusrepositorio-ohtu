import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)
        unknown = "Unknown"
        try:
            name = parsed_content["tool"]["poetry"]["name"]
        except KeyError:
            name = unknown
        try:
            desciption = parsed_content["tool"]["poetry"]["description"]
        except KeyError:
            desciption = unknown
        try:
            dependencies = [i for i in parsed_content["tool"]["poetry"]["dependencies"]]
        except KeyError:
            dependencies = unknown
        try:
            dev_dependencies = [j for j in parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"]]
        except KeyError:
            dev_dependencies = unknown
        try:
            licence = parsed_content["tool"]["poetry"]["license"]
        except KeyError:
            licence = unknown
        try:
            authors = [x for x in parsed_content["tool"]["poetry"]["authors"]]
        except KeyError:
            authors = unknown
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desciption, licence, authors, dependencies, dev_dependencies)
