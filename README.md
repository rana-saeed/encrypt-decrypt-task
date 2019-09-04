# encrypt-decrypt-task
Simple encryption and decryption algorithms for strings in python.

Environment:<br/> 
Windows OS<br/> 
Python 3.7<br/> 

To run the main python file:<br/>
1. Install "Requests" library for Python<br/>
2. Run <b>$py task.py</b> in terminal/command line<br/>
3. In "task.py" comment and uncomment functions to try<br/>

To run using the CLI tool:<br/>
1. Install "Click" library for Python<br/>
2. Run <b>$py interface.py</b> in terminal followed by text to be encrypted or decrypted then wait for prompts<br/>
	<b>e.g $py interface.py My Secret Message</b><br/>
3. Run <b>$py interface.py</b> in terminal followed by text to be encrypted or decrypted followed by <b>--algorithm</b> and <b>--method</b> arguments defined<br/>
	<b>e.g $py interface.py My Secret Message --algorithm shift --method encrypt</b><br/>

To run using Docker:<br/>
1. Run <b>$docker run encrypt-decrypt-task</b> followed by text to be encrypted or decrypted followed by <b>--algorithm</b> and <b>--method</b> arguments defined<br/>
	<b>e.g $docker run encrypt-decrypt-task My Secret Message --algorithm shift --method encrypt</b><br/>
	Note: Public image is hosted on docker hub found as <b>ranasaeed/encrypt-decrypt-task:firstversion</b>

To run the unit tests for the shiftEncrypt & matrixEncrypt funtions:<br/> 
From the terminal/command line, run <b>$py unitTest.py</b><br/>
