# Project Euler Solutions

This is my personal repo for solving [Project Euler](https://projecteuler.net) challenges using Python3. Runtime is measured and spit out at the end of execution along with the solution, according to your code. Perhaps in a later revision, answer submission may be implemented, though likely not even though I have a very good idea how to do it because I'm lazy.

If you want to try the challenges yourself and are cloning this repo for yourself, please delete all the scripts in the `solutions` directory so you can solve the problems on your own.

<br>

## Dependencies

* [`python3.8.*`](https://www.python.org/)
* [`zsh`](https://zsh.sourceforge.io/)
* [`curl`](https://curl.se/)

<br>

## Usage

* Run the `start.zsh` script and provide the problem number you would like to solve
  * example: `./start.zsh 22` - this will create a new script for problem 22
  * this script can be called from any directory and will work just fine (all paths within the `start.zsh` script are relative to the script itself)
* Open your new script in the IDE/text editor of your choice and enjoy solving
* Run the script like you would any other python script
  * example: `cd solutions && python3 ###.py` or `./solutions/###.py`

<br>

## Other Notes

* For any given python script, the `-h` flag will provide the commandline help dialog
* If you know how to use the [`argparse`](https://docs.python.org/3/library/argparse.html) python module, you can add your own commandline arguments in the `getArgs()` method
* If there is something that you'd like all of your new python scripts to have, modify the `template` file in the root directory

<br>

## Troubleshooting

* Unless you have some way of running `zsh` scripts on Windows/MacOS, the `start.zsh` script needs to be run from a Linux environment
* Make sure that the shabangs in all the scripts are valid for your installation and/or call your scripts with the appropriate program (`zsh` or `python3`)
* If you are calling the scripts directly and are getting a permission denied error, try running `chmod 750 <script_in_question>`
