
import sys, json

def texttree_from(data, pad = ""):
  r = ""
  l = len(data)
  if l > 1:
    r += "─┐ "
    nl_pad = pad + " │ "
  else:
    r += "─• "
    nl_pad = pad + "   "
  r += data[0].replace("\n", "\n" + nl_pad) + "\n"
  for i, e in enumerate(data[1:]):
    if i < l - 2:
      a, b = " ├", " │"
    else:
      a, b = " └", "  "
    r += pad + a + texttree_from(e, pad + b)
  return r

def proceed(s):
  return texttree_from(json.loads(s))

def test():
  data = [
    'A',
    [
      'C',
      [
        'D\nDD',
        ['dd\ndd']
      ],
      [
        'E',
        ['ee']
      ]
    ],
    [
      'F',
      ['ff']
    ]
  ]
  return texttree_from(data)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    r = proceed(sys.argv[1])
  else:
    inp = sys.stdin.read()
    if inp not in ("", "\n", "\r\n"):
      r = proceed(inp)
    else:
      r = test()
  print(r)


