# Day Calculator

This program is to help calculate the days between two dates.

## Usage

```python
python3 day_calculator.py
```

To reach the calucation section press 1 in the main menu.

The date has to be provided in the following format: 
e.g. 01/01/1900, 1/1/2001

If you want to leave this program press 0 anytime during usage of this program.

Press enter to get back to the main menu.

### Interactive menu

https://user-images.githubusercontent.com/25820758/127765927-cfdaadeb-ae3b-4059-b6b9-f7b8d5be72e3.mov


## Use with docker

```docker 
# build the image
docker build -t day-calculator .

# run the image interactively
docker run -it day-calculator

```

## Technical details


```sh
# main file with all logic
./day_calculator.py

# UnitTest file with all Unittests
test_day_calculator.py


```