I have the latest version done now, I just need payment

Changes:

* No longer responds to itself
* Waits 1 minute after an API error and trys again (if it fails again it waits another minute)
* New file called writephrases.py. Very useful for adding new phrases, uses a simple command line UI to prevent bugs. Also gives option to create a new file for the phrases, useful in case you break the file somehow.

&nbsp;

Instructions for use:

* The file 'subreddits.txt' is where you should list each subreddit the bot will run on. Each subreddit should be on a new line, and the subreddit name should NOT include the '/r/'.

* The file 'responses.txt' contains each phrase and response pair seperated by a '; '. Each pair is on its own line, more can be added manually however using writephrases.py to do it for you is desirable to avoid bugs.

* To run the bot execute automaticresponse.py by entering  'python3 automaticresponse.py' in terminal.

*  Run the search phrase/response editor by entering 'python3 writephrases.py' in terminal.
