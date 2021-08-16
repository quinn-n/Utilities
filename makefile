#install-local:
#	ln -sf replace.py ~/.local/bin/replace
#	ln -sf len.py ~/.local/bin/len
#	ln -sf choose.py ~/.local/bin/choose
#	ln -sf type.py ~/.local/bin/type
#	ln -sf "mass append.py" ~/.local/bin/mass_append
#	ln -sf cpStatus.py ~/.local/bin/cpStatus
localinstall:
	python make.py localinstall
install:
	python make.py install
uninstall:
	rm /bin/replace
	rm /bin/len
	rm /bin/choose
	rm /bin/type
	rm /bin/mass_append
	rm /bin/cpStatus
#local
	rm ~/.local/bin/replace
	rm ~/.local/bin/len
	rm ~/.local/bin/choose
	rm ~/.local/bin/type
	rm ~/.local/bin/mass_append
	rm ~/.local/bin/cpStatus
