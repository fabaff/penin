# Information gathering and penetration testing framework

PenIn (Information gathering and penetration testing framework) is a 
collection of tools to perform various tasks of an assessment.

## Installation

One requirements is that you have Python 3 installed.

```bash
$ pip3 install -r requirements.txt

$ pip3 install setup.py
```

## Usage

All available commands are grouped.
to execute.

```bash
$ penin --help
```

Some commands require elevated permission. Those are only working if executed
as root.

```bash
$ sudo bin/penin --help
```

## Documentation

At the current state there is no documentation beside the README available.

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `PenIn`,
and can be built with the included `make` helper:

```bash
$ make docker
$ docker run -it penin --help
```

This requires that you have `docker` installed.

## License

`penin` is licensed under the Apache Software License 2.0.