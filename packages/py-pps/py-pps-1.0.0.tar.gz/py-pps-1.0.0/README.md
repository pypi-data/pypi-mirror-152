# py-pps

**py-pps** (short for "pretty-ps") is a command-line tool used as an alternative for the `docker ps` command

## Motives
As an everyday Docker user, the `docker ps` command output always annoyed me. 
It is very wide and not very readable. 
I wanted to have a (better) alternative to it, so I created py-pps.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install py-pps.

```bash
pip install py-pps
```

## Usage

Simply run `pps` in your terminal:
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/10364402/170822616-85a3b392-8b12-4670-9a49-70d384416f89.gif)

## CLI Usage
```
$ pps --help
Usage: pps [OPTIONS]

  Command-line interface for interacting with a WVA device

Options:
  -j / --json           Print all containers' JSON data.
  -v / --version        Print the current version.
  --help                Show this message and exit.
```

## Roadmap
- [ ] Add tests
- [ ] Add additional functionality (such as filtering)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
✉️ [chaim.tomer@gmail.com](mailto:lunde@adobe.com?subject=[GitHub]%20Source%20Han%20Sans)



## License
[MIT](https://choosealicense.com/licenses/mit/)

