
## generating wordlist

To generate wordlist.txt from the original, you can do the following:

    wget https://github.com/perjg/fourletterword/blob/master/flw/sr_concise?raw=true -O sr_concise
	wget https://github.com/perjg/fourletterword/blob/master/flw/rs_concise?raw=true -O rs_concise
	./makelist.py sr_concise rs_concise > wordlist.txt

After generating wordlist.txt, you can safely remove sr_concise and rs_concise

