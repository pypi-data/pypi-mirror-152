# **findHelp Python Library**

A simple Python library to search files / folders.

## **Overview**

This package finds out for f    iles / folders based on given criteria, such as regular expressions, folders to exclude, filter extensions, etc.  It returns a console output, a Pandas.DataFrameObject, a Python dictionary or a delimited file (csv, json, txt).

## **Setup**

Right now, the library is not hosted on **PyPi** so you will need to do a local
install on your system if you plan to use it in other scrips you use.

First, clone this repo to your local system. After you clone the repo, make sure
to run the `setup.py` file, so you can install any dependencies you may need. To
run the `setup.py` file, run the following command in your terminal.

~~~bash
pip install findhelp
~~~


## **Usage**

### **Import `go_search()` function**

Here is a simple example of using the `findHelp` library. 

~~~py
from findhelp.finder import go_search

results = go_search(
    {
        "path": "C:", 
        "stringsearch": 
        "dummy", "output": "obj_list"
    }
)
~~~

The above code will return a Python list of dictionaries. Each dictionary is a found match, containing:

- **`fullpath`**:
  - If `type` = `folder`, full path to the found match.
  - If `type` = `file`, full path in which the file was found.
- **`type`**: `file` / `folder`, the kind of found match.
- **`folder_parent`**: Parent folder for the current found match.
- **`folder_name`**: 
  - If `type` = `folder`, the actual folder name.
  - If `type` = `file`, the folder name in which file was found.
- **`file_name`**: If `type` = file, the name of the file, otherwise empty string.
- **`ext`**: If `type` = file extension for the found match.

There is duplicated info between result fields, it was made this way for making filtering easier.


#### **Arguments**

`go_search()` expects a dictionary containing the criteria to perform the search.

- `path (str)`: Root path to look for, default = current directory
- `stringsearch (str)`: The string to look for
- `ignorecase (bool)`: Indicates whether or not searching is case-sensitive
- `ignoreaccents (bool)`: Ignore accents
- `regexp (bool)`: Searches by regular expresion
- `ext (list[`str]): List of extensions to limit the search
- `all (bool)`: Searches on all folders, ignores 'ignore_folders' switch on 'config.yaml'
- `onlyfiles (bool)`: Searches only for files (not directories)
- `onlydirs (bool)`: Searches only for directories (not files)
- `directoryseparator (str)`: Just for results purposes: which separator use for paths
- `output (str)`: Indicates if results appears on console or are written to a file
  - `console`: Prints results to console.
  - `txt` / `csv`: Creates a delimited file.
  - `json`: Creates a JSON that contains:
    - `search_args`: Dictionary with used criteria.
    - `start`: datetime, when search started.
    - `end`: datetime, when search was finished.
    - `total_time_seconds`: Total time used to perform the search.
    - `results`: List of JSON objects, each one represents a single found match.
  - `df`: `pandas.DataFrame` object with all the results.
  - `obj_list`: Python list containing objects, each one represents a single found match.
  - `list`: Python list of lists, each one represents a single found match. Note it doesn't contain headers.
- `delimiter (str)`: Delimiter used for exporting, when output is different than 'console'
- `outputpath (str)`: Path in which the results file will be located. Default current directory.
- `outputfilename (str)`: Name of file in which results will be stored. Default `search_results_yyyymmdd_hh_mm_ss` 

### Use from console

Using from console takes the same arguments than import `go_search()` function, but instead of a dictionary, expects criteria to be passed as command line arguments.

~~~bash
python -m findhelp -h
~~~

~~~
usage: findhelp.py [-h] [-p PATH] [-s STRINGSEARCH] [-i] [-c] [-r] [-e EXT [EXT ...]] [-a] [-f] [-d] [-ds {/,\\,\}]
                   [-o {console,txt,csv,json,df,obj_list,list}] [-dl DELIMITER] [-m OUTPUTPATH] [-n OUTPUTFILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Root path to look for, default = current directory
  -s STRINGSEARCH, --stringsearch STRINGSEARCH
                        The string to look for
  -i, --ignorecase      Indicates whether or not searching is case-sensitive
  -c, --ignoreaccents   Ignore accents
  -r, --regexp          Searches by regular expresion
  -e EXT [EXT ...], --ext EXT [EXT ...]
                        List of extensions to limit the search
  -a, --all             Searchs on all folders, ignores 'ignore_folders' switch on config.yaml
  -f, --onlyfiles       Searches only for files (not directories)
  -d, --onlydirs        Searches only for directories (not files)
  -ds {/,\\,\}, --directoryseparator {/,\\,\}
                        Just for results purposes: which separator use for paths
  -o {console,txt,csv,json,df,obj_list,list}, --output {console,txt,csv,json,df,obj_list,list}
                        Indicates if results appears on console or are written to a file
  -dl DELIMITER, --delimiter DELIMITER
                        Delimiter used for exporting, when output is different than 'console'
  -m OUTPUTPATH, --outputpath OUTPUTPATH
                        Output (results) path
  -n OUTPUTFILENAME, --outputfilename OUTPUTFILENAME
                        Output (results) filename (with no extension)
~~~



