# edas_conference_finder
conference finder for edas.info

# Usage
- `-f`, `--file` : input file path
- `-c`, `--category` : conference's category list. (ex: `-c "wireless, communication"`)
- `-l`, `--location` : confernece's country or city. (ex: `-l "korea, china, usa, seoul, new york, beijing"`)
- `-d`, `--date` : conference's date in `yyyymmdd` format. (ex: `-d 20181231`)
- `-D`, `--deadline` : conference's paper submit deadline in `yyyymmdd` format. (ex: `-D 20181231`)

# Usage Example
`./main.py -f sample.txt -c "wireless, communication, cloud, network" -d 20190131 -D 20180701`

or

`python3 main.py -f sample.txt -c "wireless, communication, cloud, network" -d 20190131 -D 20180701`

# Requirements
- python3.x
- `http://edas.info/listConferencesSubmit.php`'s html code fragment (see the `sample.txt`)

# Author
- Minsu Kim
- k09089@naver.com
