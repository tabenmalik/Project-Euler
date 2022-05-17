FROM python:3.10-bullseye

# Common set of development tools
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    # Get latest versions of all packages
    && apt-get -y upgrade --no-install-recommends \
    # Install common development dependencies
    && apt-get -y install --no-install-recommends \
        pipenv \
    # Tactically remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    # Can leave in Dockerfile once upstream base image moves to > 7.0.7-28.
    && apt-get purge -y imagemagick imagemagick-6-common \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*


ENV SHELL=/bin/bash
WORKDIR /project-euler

COPY ./Pipfile /project-euler/Pipfile

RUN cd /project-euler \
    && pipenv update

CMD ["pyenv" "shell"]
