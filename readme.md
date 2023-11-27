# <b>Webp Converter</b>

Converts 1 or many files to webp.

NOTE: If your converting more than 4000 use python, node will just get slower and slower and slower.
TODO: Maybe make multi threaded node and python versions of this utility... But then again, maybe not...

<br>

## <b>NodeJS version Usage</b>

- Install nodejs
- Delete all files in the input and output folders
- Copy your jpg or png images for conversion into the input folder
- install the necessary libraries via npm install
```
npm install
```
- Open terminal/dos/shell/cli and run comman node convert
```
node convert
```

- Collect the converted files from the output folder

<br><br>

## <b>Options</b>
The compression is set to 80, if you want to change this open file convert.js go to line 12 and change the value.

Range is 0 to 100

- 0 (worst / fastest)
- 100 (best / longest)

Typical values are 70 to 80.

```
let quality = 80; // 0 = bad, 100 = best, best values are between 70 to 80
```

<br><br><hr>

## <b>Pthon version Usage</b>

- Make sure you have python installed
- Set webpQuality variablein convert.py (save)
- Delete all files in the input and output folders
- Copy your jpg or png images for conversion into the input folder
- run the following command from the project folder root folder
```
py convert.py
```