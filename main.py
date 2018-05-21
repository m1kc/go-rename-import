#!/usr/bin/env python3
import sys
import os
import tempfile
import subprocess


def rename_all(srcdir, old_name, new_name, include_subpackages=True, dry_run=True):
	for root, dirs, files in os.walk(srcdir):
		for filename in files:
			rename(os.path.join(root, filename), old_name, new_name, include_subpackages, dry_run)


def rename(filename, old_name, new_name, include_subpackages=True, dry_run=True):
	# print(f"rename: {[filename, old_name, new_name, dry_run]}")
	old_text = open(filename, 'r').read()
	new_text = old_text

	new_text = new_text.replace(f'"{old_name}"', f'"{new_name}"')
	if include_subpackages:
		new_text = new_text.replace(f'"{old_name}/', f'"{new_name}/')

	if old_text != new_text:
		print(f"{filename} ({len(old_text)} -> {len(new_text)})")
		if dry_run:
			d = diff(old_text, new_text)
			print(d)
		else:
			f = open(filename, 'w')
			f.write(new_text)
			f.close()


def diff(str1, str2, colorful=True):
	with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f1:
		with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f2:
			f1.write(str1)
			f1.flush()
			f2.write(str2)
			f2.flush()

			color = '--color=never'
			if colorful:
				color = '--color=always'

			p = subprocess.run(
				['diff', '-u', color, f1.name, f2.name],
				stdout=subprocess.PIPE,
				encoding='utf-8',
			)
			return p.stdout


def main():
	_, srcdir, old_name, new_name = sys.argv
	rename_all(srcdir, old_name, new_name, dry_run=True)
	a = input("Proceed? [y/N] ")
	if a == 'y':
		rename_all(srcdir, old_name, new_name, dry_run=False)
	print("Done.")


if __name__ == '__main__':
	main()
