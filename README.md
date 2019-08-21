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
* Please change in file **resources/Annotated-WikiExtractor/annotated_wikiextractor/annotated_wikiextractor.py**:
    * **number_of_workers** in **resources/Annotated-WikiExtractor/annotated_wikiextractor/annotated_wikiextractor.py**.
* Please change in file **resources/Annotated-WikiExtractor/annotated_wikiextractor/wikiextractor.py**:
    * line 340 (title = line[2:2]) to `title = line`)
    * line 348 (title = line[2:-2]) to `title = line`)
* **langage2info** in **merge_indices.py** to the correct crawling dates of which Wikipedia dumps you downloaded.

```bash 
bash convert_all.sh
```

The end result is an index from the Wikipedia url -> 
the path to file in which the output is found with the line number,
See `how_to_use.py` for more information

## Output
In the resulting JSON files, the titles start and end with **++**. All sections titles start and end with **##**

## Debugging
the file **annotated_wikiextractor.py** contains the extraction script, but
without multiprocessing. This helps in debuggin if there is an error.

## TODO
* smaller pages are not excluded, find the option to include those
    
## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
