import pkg_resources
from github import Github, GithubException
import requests

requirements = {}
new_package_list = []


def get_dependencies(packages: list):
    new_package_list.clear()
    try:
        for package in packages:
            resource = pkg_resources.working_set.by_key[package]
            if not resource.requires():
                continue
            requirements.update({package: [i.key for i in resource.requires()]})
            new_package_list.extend(requirements[package])
        if new_package_list:
            get_dependencies(new_package_list.copy())
        return requirements
    except KeyError:
        if packages == "pyrebase":
            return "you need to install 'pyrebase' or change the key to 'pyrebase4'"
        return "package not installed on your machine, install and re-run the check again"


def check_non_existing_recipe(packages: list):
    try:
        github = Github()
        repo = github.search_repositories("python-for-android")[0]
        recipe_list = [file.name for file in repo.get_contents("pythonforandroid/recipes")]

        return [package for package in packages if package not in recipe_list]
    except requests.exceptions.RequestException:
        return "Please make sure you have internet access"


if __name__ == "__main__":
    print(get_dependencies(["pyrebase4"]))
    print(check_non_existing_recipe(["pyrebase4"]))
