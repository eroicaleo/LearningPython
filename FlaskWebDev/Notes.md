# Preface

Deviating from the path set by the framework’s developers will give you lots of headaches.

With Flask you can choose the components of your application, or even write
your own if that’s what you want.

Flask comes with a robust core. And expect all rest are provided by 3rd party.

[github source code](https://github.com/miguelgrinberg/flasky)

* Useful git command for this book

```shell
git clone https://github.com/miguelgrinberg/flasky.git
git checkout 1a
git reset --hard
git fetch --all
git fetch --tags
git reset --hard origin/master
git diff 2a 2b
```

## chapter 01 installation

Flask has three main dependencies.

1. The routing, debugging, and Web Server Gateway
Interface (WSGI) subsystems come from `Werkzeug`;
2. the template support is provided by `Jinja2`;
3. and the command-line integration comes from `Click`.

These dependencies are all authored by Armin Ronacher, the author of Flask.

```shell
conda create --name flasky python=3.8.5
conda activate flasky
conda deactivate
python --version
conda list
conda install flask
```
