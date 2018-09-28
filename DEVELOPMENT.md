# Development of PenIn

This project includes a number of helpers in the `Makefile` to streamline
common development tasks.

## Environment Setup

```bash
$ git clone [repo]
$ cd penin
$ python3 -m venv .
$ source bin/activate
$ pip3 install -r requirements.txt

$ pip3 install setup.py
```

## Style

Please sort and group the import with `isort` after you have fixed the style
issues with `black`.

## Tests

```bash
$ make test
```

### Releasing to PyPi

Uee the included helper function via the `Makefile`:

```bash
$ make dist
$ make dist-upload
```
