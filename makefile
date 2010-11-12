clean:
	find ./ -name '*~' -exec rm -f {} \; 
	find ./ -name '#*' -exec rm -f {} \;
	find ./ -name 'Thumbs.db' -exec rm -f {} \; 
	find ./ -name '*.pyc' -exec rm -f {} \;
