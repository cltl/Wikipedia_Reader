# Wikipedia Reader

The goal of this repository is download represent Wikipedia dumps
and convert them into JSON format (with both the text and the offsets of the hyperlinks).

This is a wrapper around [Annotated-WikiExtractor](https://github.com/jodaiber/Annotated-WikiExtractor).

### Prerequisites
Python 2.7 was used to create this project. It might work with older versions of Python.
It should be possible to call
```python
python2.7 some_file.py
```
#### Python modules

A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

#### Resources
The Wikipedia dumps need to be downloaded. In this repository, the paths to the dumps in Italian, English, and Dutch are hardcoded \
in the install script. Please change the paths in the script to change for other languages. The download can be performed by calling:
```bash
bash install.sh data_folder
```

The script will also store GitHub repositories in the folder 'resources'.

## How to use
```bash 
bash convert_all.sh
python create_index.py
```

The end result is an index from the Wikipedia url -> 
the path to file in which the output is found with the line number,
See `how_to_use.py` for more information

## TODO
* index from Wikipedia page to -> file and line number
* in JSON output, the **url** key is always prefixed with "http://en.wikipedia.org/". 
We should make this more general
* it is possible to edit the number of workers (number of parallel processes)
    
## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
