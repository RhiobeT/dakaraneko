# Dakaraneko

A bridge between the Dakara and the Karaneko projects.

## System requirements

* Python 3.

## Install


Clone the project with its submodule:

```sh
git clone --recursive git@github.com:Neraste/dakaraneko.git
```

Or initialise submodules if you have cloned without including them:

```sh
git submodule update --init --recursive
```

Refer to the parsers and config file in the Dakara commands.

## Setting up dakara-server for use with dakaraneko

Get the latest release of dakara-server
### dakara-server installation

Install dakara-server dependencies:

```sh
pip install -r requirements.txt
```
Update/Create database schema: 

```sh
dakara_server/manage.py migrate
```
Create a superuser:

```sh
dakara_server/manage.py createsuperuser
```

### Configuring tags and work types

Create tags and work types:

```sh
dakara_server/manage.py createtags <path-to-dakaraneko>/config.yaml # for tags
dakara_server/manage.py createworktypes <path-to-dakaraneko>/config.yaml # for work types
```
### Feeding database with from media library
Edit the first lines of file `feed.sh` found in dakaraneko, to match your existing directories :

```
DAKARA_SERVER_DIR=/path/to/dakara-server
DAKARANEKO_DIR=/path/to/dakaraneko
KARA_DIR=/path/to/karaoke_folder/
```
The karaoke_folder should have the following subdirectories:
* Wmusic
* CJKmusic
* Jeu
* Anime
* Live action
* Dessin animé
* Nouveau
* Autre

Then execute feed.sh
