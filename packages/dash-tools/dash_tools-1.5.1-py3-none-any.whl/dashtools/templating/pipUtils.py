'''
 # @ Author: Andrew Hossack
 # @ Create Time: 2022-05-24 17:46:41
'''

from dashtools.templating import buildApp
from dashtools.deploy import deployHeroku
import os
import pkg_resources

# TODO figure out which pip; pip3 or pip command. See configUtils for storing command and
# runtimeUtils for implementation. If using python3 then pip3 is used.


def _install_pip_requirement(requirement: str):
    '''
    Install a pip requirement
    '''
    print(f'dashtools: Installing {requirement}')
    os.system(f'pip install {requirement}')


def _check_pip_requirement_installed(requirement: str) -> bool:
    '''
    Check if a pip requirement is installed
    '''
    try:
        pkg_resources.get_distribution(requirement)
    except pkg_resources.DistributionNotFound:
        return False
    except pkg_resources.VersionConflict:
        return False
    return True


def _check_pip_requirements(requirements: list, template_value: str):
    '''
    Check if pip requirements are installed
    '''
    for req in requirements:
        if not _check_pip_requirement_installed(req):
            print(
                f'dashtools: Template {template_value} requires pip module {req}, which is not installed')
            if deployHeroku.prompt_user_choice(f'dashtools: Install {req}?'):
                _install_pip_requirement(req)
                print()


def _get_template_required_packages(template_value: str) -> list:
    """
    Looks for 'packages' file in template directory. If one is found,
    return a list of pip requirements.
    """
    packages_file = os.path.join(
        buildApp._get_template_path(template_value), 'packages.txt')
    if os.path.exists(packages_file):
        with open(packages_file, 'r') as f:
            return f.read().splitlines()
    return []


def handle_template_requirements(template_value: str):
    """
    Handle pip requirements for template
    """
    _check_pip_requirements(_get_template_required_packages(
        template_value), template_value)
