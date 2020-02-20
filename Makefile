deb-package:
	python3 setup.py --command-packages=stdeb.command bdist_deb
snap-package:
	snapcraft
standalone:
	echo "from  circleoffifths.main import main; main()" > main.py
	PYTHONOPTIMIZE=1 pyinstaller main.py -F -n circleoffifths --distpath dist/
	rm main.py
py-install:
	python3 setup.py install --user
py-bundle:
	# Bundles all the project files into a compressed, executable file. No interpreter or libraies included
	rm -rf tmp
	mkdir -p tmp
	# Copy files recrusively and reserve attributes
	for d in circleoffifths circleoffifths/utilities ; do \
	  mkdir -p tmp/$$d ;\
	  cp -pPR $$d/*.py tmp/$$d/ ;\
	done
	# Create entry point and package archive
	echo "from  circleoffifths.main import main; main()" > tmp/__main__.py
	cd tmp ; zip -q _circleoffifths circleoffifths/*.py circleoffifths/*/*.py __main__.py
	# Add shebang line and append zip file content
	echo '#!/usr/bin/python3' > circleoffifths_bundled
	cat tmp/_circleoffifths.zip >> circleoffifths_bundled
	chmod a+x circleoffifths_bundled
	rm -rf tmp
clean:
	rm -rf build dist deb_dist circleoffifths.egg-info
	rm -rf circleoffifths*.snap circleoffifths-*.tar.gz main.spec
