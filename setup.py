
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    # This function returns the list of requirements
    requirements_list: List[str] = []

    try:
        with open("requirements.txt") as f:
            lines = f.readlines()

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_list
setup(
    name="Network_S",
    version="0.0.1",
    author="Tejswini Korade",
    author_email="tejaswinikorade4284@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)