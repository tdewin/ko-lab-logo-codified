multiline_str = """
10010001110
10100010001
11000010001
10100010001
10010001110
00000000000
10000100110
10001010101
10001110110
10001010101
11101010110
"""

# Split into lines and strip whitespace from each line
lines = [line.strip() for line in multiline_str.strip().splitlines()]


offset=10
wid=10
ht=10
gap=2

xwid = len(lines[0])
yht = len(lines)

totwidth = offset*2 + (xwid)*(wid+gap)-gap
totheight = offset*2 + (yht)*(ht+gap)-gap

print(xwid,yht,totwidth,totheight)

with open("output.svg", "w", encoding="utf-8") as file:
  file.write(f'<svg viewBox="0 0 {totwidth} {totheight}" width="{totwidth}" height="{totheight}">')
  file.write(f'<rect id="bg" inkscape:label="bg" style="fill:black;" x="0" y="0" width="{totwidth}" height="{totheight}"/>')
  file.write(f'<g id="grid" inkscape:label="grid">')

  for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
      char = line[x]
      if char == "1":
        file.write(f'<rect id="{x}-{y}" inkscape:label="{x}-{y}" style="fill:white;" x="{offset+x*(wid+gap)}" y="{offset+y*(ht+gap)}" width="{wid}" height="{ht}"/>')
        print(char,end="")
      else:
        print(' ',end="")
    print()
  file.write('</g></svg>')
