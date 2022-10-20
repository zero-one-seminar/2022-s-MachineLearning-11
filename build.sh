#!/bin/zsh

# activate venv
source .practice-datavisualization/bin/activate

# copy ipynb files
cp *.ipynb python-datavisualization/

# build jupyterbook
jb build python-datavisualization

# deploy
if [[ $1 == '-d' ]] then
    ghp-import -n -p -f python-datavisualization/_build/html
fi
