
import sys, json
from dataclasses import dataclass

@dataclass
class IndentedString:
	level: int
	string: str

def proceed(s):
	isl = [dropcount(e, "\t") for e in s.strip().split("\n")]
	l, isl = json_from_indented_text(isl)
	return json.dumps(l, ensure_ascii = False)

def json_from_indented_text(isl, level = 0):
	l = []
	head_found = False
	while len(isl) > 0:
		lv = isl[0].level
		if lv == level and not head_found:
			l.append(isl[0].string)
			isl = isl[1:]
			head_found = True
		elif lv > level:
			r, isl = json_from_indented_text(isl, level = lv)
			l.append(r)
		else:
			break
	return (l, isl)

def dropcount(s, ch):
	n = 0
	while len(s) > 0 and s[0] == ch:
		n += 1
		s = s[1:]
	return IndentedString(level = n, string = s)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		i = sys.argv[1]
	else:
		i = sys.stdin.read()
	print(proceed(i))

