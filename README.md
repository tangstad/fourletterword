# fourletterword
## Four letter word generator for Akafugu VFD shield

Current usage for commandline testing:

    ./generate.py wordlist.txt

Will output a list of four letter words to stdout, one every 500ms.

## Generating wordlist.txt

(You should never really need to do this...)

To generate wordlist.txt from the original, you can do the following:

    wget https://github.com/perjg/fourletterword/blob/master/flw/sr_concise?raw=true -O sr_concise
	wget https://github.com/perjg/fourletterword/blob/master/flw/rs_concise?raw=true -O rs_concise
	./makelist.py sr_concise rs_concise > wordlist.txt

After generating wordlist.txt, you can safely remove sr_concise and rs_concise

