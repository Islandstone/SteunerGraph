
all: prebuild dots jpgs

prebuild:
	mkdir -p img

dots:
	python2 graph.py Majstrie.csv

jpgs:
	$(MAKE) -f Makefile.jpgs 

clean:
	rm -f *.dot
	rm -rf img

dist: all
	mkdir -p ~/Dropbox/Majstrie/img
	cp img/*.jpg ~/Dropbox/Majstrie/img/

distclean:
	rm -rf ~/Dropbox/Majstrie/img/

