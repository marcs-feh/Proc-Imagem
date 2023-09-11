#!/usr/bin/env sh

for l in $(cat .gitignore); do
	"Remove $l"
	sh -c "rm -fr $l"
done
