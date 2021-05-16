import pkg_resources
from github import Github, GithubException

requirements = {}


def get_dependencies(packages: list):
    for package in packages:
        resource = pkg_resources.working_set.by_key[package]
        if not resource.requires():
            continue
        requirements.update({package: [i.key for i in resource.requires()]})
        package = requirements[package]
        if "kivy" in requirements:
            package = requirements.pop("kivy")
        get_dependencies(package)
        return requirements


def check_non_existing_recipe(packages: list):
    github = Github()
    recipe_list = []
    non_existing_recipe = []
    repo = github.search_repositories("python-for-android")[0]
    for file in repo.get_contents("pythonforandroid/recipes"):
        recipe_list.append(file.name)
    for package in packages:
        if package not in recipe_list:
            non_existing_recipe.append(package)
    return non_existing_recipe


check_non_existing_recipe(["kivy", "dark", "white"])
