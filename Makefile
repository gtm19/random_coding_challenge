$PHONY: new

# command to create new files using python -m random_coding_challenge {num}
new:
	python -m random_coding_challenge $(word 2,$(MAKECMDGOALS))
