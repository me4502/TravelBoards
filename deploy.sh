#!/usr/bin/env bash
BRANCH=gh-pages
TARGET_REPO=Me4502/TravelBoards.git
PELICAN_OUTPUT_FOLDER=output

echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    cd $PELICAN_OUTPUT_FOLDER
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "travis@travis-ci.org"
        git config --global user.name "Travis"
    fi

    git init
    git remote add origin https://Me4502:${GH_TOKEN}@github.com/$TARGET_REPO >/dev/null
    git checkout --orphan $BRANCH
    git add .
    git commit -q -m "Deploy $(date)" &> /dev/null
    git push -q -f origin $BRANCH &> /dev/null

    echo -e "Deploy completed\n"
fi