# Unitgrade

Unitgrade is an automatic software testing framework that enables instructors to offer automatically evaluated programming assignments with a minimal overhead for students.

Unitgrade is build on pythons `unittest` framework so that the tests can be specified and run in a familiar syntax, 
 and will integrate well with any modern IDE. What it offers beyond `unittest` is the ability to collect tests in reports (for automatic evaluation) 
and an easy and safe mechanism for verifying results. 

 - 100% Python `unittest` compatible
 - Integrates with any modern IDE (VSCode, Pycharm, Eclipse)
 - No external configuration files or setup required
 - Tests are quick to run and will tell you where your mistake is
 - Hint-system collects hints from code and display it with failed unittests

## Installation
Unitgrade is simply installed like any other package using `pip`:
```terminal
pip install unitgrade
```
This will install unitgrade in your site-packages directory and you should be all set. If you want to upgrade an old version of unitgrade run:
```terminal
pip install unitgrade --upgrade --no-cache-dir
```
If you are using anaconda+virtual environment you can install it as any other package:
```terminal
source activate myenv
conda install git pip
pip install unitgrade
```
When you are done, you should be able to import unitgrade. Type `python` in the termial and try:
```pycon
>>> import unitgrade2
```

## Using Unitgrade
In unitgrade, your homework assignments are called **reports** and are distributed as regular `.py`-files. I am going to use `cs101report1.py` as a generic example in the following, but a real-world example can be found here: https://gitlab.compute.dtu.dk/tuhe/unitgrade_private/-/blob/master/examples/example_simplest/students/cs101/report1.py .

The report is simply a collection of questions which are individually scored, and each question may in turn involve checking several sub-cases.

You should think of the tests as a help for you when you are debugging your code and when you are trying to figure out what to do. 
I recommend running the tests through your IDE. In pycharm, this is as simple as right-clicking on the test and selecting `Run as unittest`. The image belows shows the outcome in Pycharm:

![Using unittests in pycharm](https://gitlab.compute.dtu.dk/tuhe/unitgrade/-/raw/master/docs/pycharm.png)

The tests are shown in the lower-left corner, and in this case they are all green meaning they have passed. If a test fails, you can right-click and select `debug as unittest`, or you can click on it and see the output it produced, and you can right-click on individual tests to re-run them.

### Checking your score
To check your score, you have to run the main script (`cs101report1.py`) as a regular python file. This can be done either through pycharm (Hint: Open the file and press `alt-shift-F10`) or in the console by running the command: 
```
python cs101report1.py
```
The file will run and show an output where the score of each question is computed as a (weighted) average of the individual passed tests. An example is given below:
```terminal
 _   _       _ _   _____               _      
| | | |     (_) | |  __ \             | |     
| | | |_ __  _| |_| |  \/_ __ __ _  __| | ___ 
| | | | '_ \| | __| | __| '__/ _` |/ _` |/ _ \
| |_| | | | | | |_| |_\ \ | | (_| | (_| |  __/
 \___/|_| |_|_|\__|\____/_|  \__,_|\__,_|\___| v0.1.22, started: 19/05/2022 15:16:20

Week 4: Looping (use --help for options)
Question 1: Cluster analysis                                                                                            
 * q1.1) clusterAnalysis([0.8, 0.0, 0.6]) = [1, 2, 1] ?.............................................................PASS
 * q1.2) clusterAnalysis([0.5, 0.6, 0.3, 0.3]) = [2, 2, 1, 1] ?.....................................................PASS
 * q1.3) clusterAnalysis([0.2, 0.7, 0.3, 0.5, 0.0]) = [1, 2, 1, 2, 1] ?.............................................PASS
 * q1.4) Cluster analysis for tied lists............................................................................PASS
 * q1)   Total.................................................................................................... 10/10
 
Question 2: Remove incomplete IDs                                                                                       
 * q2.1) removeId([1.3, 2.2, 2.3, 4.2, 5.1, 3.2,...]) = [2.2, 2.3, 5.1, 3.2, 5.3, 3.3,...] ?........................PASS
 * q2.2) removeId([1.1, 1.2, 1.3, 2.1, 2.2, 2.3]) = [1.1, 1.2, 1.3, 2.1, 2.2, 2.3] ?................................PASS
 * q2.3) removeId([5.1, 5.2, 4.1, 4.3, 4.2, 8.1,...]) = [4.1, 4.3, 4.2, 8.1, 8.2, 8.3] ?............................PASS
 * q2.4) removeId([1.1, 1.3, 2.1, 2.2, 3.1, 3.3,...]) = [4.1, 4.2, 4.3] ?...........................................PASS
 * q2.5) removeId([6.1, 3.2, 7.2, 4.2, 6.2, 9.1,...]) = [9.1, 5.2, 1.2, 5.1, 1.2, 9.2,...] ?........................PASS
 * q2)   Total.................................................................................................... 10/10
 
Question 3: Bacteria growth rates                                                                                       
 * q3.1) bacteriaGrowth(100, 0.4, 1000, 500) = 7 ?..................................................................PASS
 * q3.2) bacteriaGrowth(10, 0.4, 1000, 500) = 14 ?..................................................................PASS
 * q3.3) bacteriaGrowth(100, 1.4, 1000, 500) = 3 ?..................................................................PASS
 * q3.4) bacteriaGrowth(100, 0.0004, 1000, 500) = 5494 ?............................................................PASS
 * q3.5) bacteriaGrowth(100, 0.4, 1000, 99) = 0 ?...................................................................PASS
 * q3)   Total.................................................................................................... 10/10
 
Question 4: Fermentation rate                                                                                           
 * q4.1) fermentationRate([20.1, 19.3, 1.1, 18.2, 19.7, ...], 15, 25) = 19.600 ?....................................PASS
 * q4.2) fermentationRate([20.1, 19.3, 1.1, 18.2, 19.7, ...], 1, 200) = 29.975 ?....................................PASS
 * q4.3) fermentationRate([1.75], 1, 2) = 1.750 ?...................................................................PASS
 * q4.4) fermentationRate([20.1, 19.3, 1.1, 18.2, 19.7, ...], 18.2, 20) = 19.500 ?..................................PASS
 * q4)   Total.................................................................................................... 10/10
 
Total points at 15:16:20 (0 minutes, 0 seconds)....................................................................40/40
Provisional evaluation
---------  -----
q1) Total  10/10
q2) Total  10/10
q3) Total  10/10
q4) Total  10/10
Total      40/40
---------  -----
 
Note your results have not yet been registered. 
To register your results, please run the file:
>>> report1intro_grade.py
In the same manner as you ran this file.

```
### Handing in your homework
Once you are happy with your results and want to hand in, you should run the script with the `_grade.py`-postfix, in this case `cs101report1_grade.py` (see console output above):
```
python cs101report1_grade.py
```
This script will run *the same tests as before* and generates a file named `Report0_handin_18_of_18.token` (this is called the `token`-file because of the extension). The token-file contains all your results and it is the token-file you should upload (and no other). Because you cannot (and most definitely should not!) edit it, it shows the number of points in the file-name. 

### Why are there two scripts?
The reason why we use a standard test script (one with the `_grade.py` extension and one without), is because the tests should both be easy to debug, but at the same time we have to avoid accidential changes to the test scripts. The tests themselves are the same, so if one script works, so should the other.

# FAQ
 - **My non-grade script and the `_grade.py` script gives different number of points**
Since the two scripts should contain the same code, the reason is nearly certainly that you have made an (accidental) change to the test scripts. Please ensure both scripts are up-to-date and if the problem persists, try to get support.
   
 - **Why is there a `unitgrade` directory with a bunch of pickle files? Should I also upload them?**
No. The file contains the pre-computed test results your code is compared against. You should only upload the `.token` file, nothing else
   
 - **I am worried you might think I cheated because I opened the '_grade.py' script/token file**
This should not be a concern. Both files are in a binary format (i.e., if you open them in a text editor they look like garbage), which means that if you make an accidential change, they will with all probability simply fail to work. 
   
 - **I think I might have edited the `report1.py` file. Is this a problem since one of the tests have now been altered?**
Feel free to edit/break this file as much as you like if it helps you work out the correct solution. However, since the `report1_grade.py` script contains a seperate version of the tests, please ensure both files are in sync to avoid unexpected behavior. 
   
### Debugging your code/making the tests pass
The course material should contain information about the intended function of the scripts used in the tests, and the file `report1.py` should mainly be used to check which of your code is being run. In other words, first make sure your code solves the exercises, and only later run the test script which is less easy/nice to read. 
However, obivously you might get to a situation where your code seems to work, but a test fails. In that case, it is worth looking into the code in `report1.py` to work out what is going on. 

 - **I am 99% sure my code is correct, but the test still fails. Why is that?**
The testing framework offers a great deal of flexibility in terms of what is compared. This is either: (i) The value a function returns, (ii) what the code print to the console (iii) something derived from these.
When a test fails, you should always try to insert a breakpoint on exactly the line that generate the problem, run the test in the debugger, and figure out what the expected result was supposed to be. This should give you a clear hint as to what may be wrong.

One possibility that might trick some is that if the test compares a value computed by your code, the datatype of that value is important. For instance, a `list` is not the same as a python `ndarray`, and a `tuple` is different from a `list`. This is the correct behavior of a test: These things are not alike and correct code should not confuse them. 

 - **The `report1.py` class is really confusing. I can see the code it runs on my computer, but not the expected output. Why is it like this?**
To make sure the desired output of the tests is always up to date, the tests are computed from a working version of the code and loaded from the disk rather than being hard-coded.

 - **How do I see the output of my programs in the tests? Or the intended output?**
There are a number of console options available to help you figure out what your program should output and what it currently outputs. They can be found using:
 ```python report1.py --help```
Note these are disabled for the `report1_grade.py` script to avoid confusion. It is not recommended you use the grade script to debug your code.  
   
 - **Since I cannot read the `.token` file, can I trust it contains the same number of points internally as the file name indicate?**
Yes. 

### Privacy/security   
 - **I managed to reverse engineer the `report1_grade.py`/`*.token` files in about 30 minutes. If the safety measures are so easily broken, how do you ensure people do not cheat?**
That the script `report1_grade.py` is difficult to read is not the principle safety measure. Instead, it ensures there is no accidential tampering. If you muck around with these files and upload the result, we will very likely know.     

- **I have private data on my computer. Will this be read or uploaded?**
No. The code will look for and upload your solutions, but it will not read/look at other directories in your computer. As long as your keep your private files out of the directory containing your homework you have nothing to worry about. 

- **Does this code install any spyware/etc.? Does it communicate with a website/online service?**
No. Unitgrade makes no changes outside the courseware directory and it does not do anything tricky. It reads/runs code and produce the `.token` file.
  
- **I still have concerns about running code on my computer I cannot easily read**
Please contact me and we can discuss your specific concerns.

# Citing
```bibtex
@online{unitgrade,
	title={Unitgrade (0.1.22): \texttt{pip install unitgrade}},
	url={https://lab.compute.dtu.dk/tuhe/unitgrade},
	urldate = {2022-05-19}, 
	month={9},
	publisher={Technical University of Denmark (DTU)},
	author={Tue Herlau},
	year={2022},
}
```