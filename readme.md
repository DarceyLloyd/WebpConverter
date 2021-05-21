# <b>Webp Converter</b>

Converts 1 or many files to webp.

<br>

## <b>Usage</b>

- Install nodejs
- Delete all files in the input and output folders
- Copy your jpg images for conversion into the input folder
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