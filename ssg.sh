#!/bin/sh

strip_ext() { echo "$1" | cut -d. -f1; }
get_ext() { echo "$1" | cut -d. -f2-; }

newers() {
	for file in *
	do
		ext="$(get_ext "$file")"
		test "$ext" = "$1" || continue
		basename="$(strip_ext "$file")"
		file2="$basename.$2"
		test "$file" -nt "$file2" && echo "$file"
	done
}

FILES="$(newers thtml html)"
printf "%s" "$FILES"
test -n "$FILES" && echo
for file in $FILES
do
	basename="$(strip_ext "$file")"
	file2="$basename.html"
	cpp -P "$file" -o "$file2"
done

