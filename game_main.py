data = {
 "network": {
  "lines": [
    {
     "name.en": "Ginza",
     "name.jp": "銀座線",
     "color": "orange",
     "number": 3,
     "sign": "G"
    },
    {
     "name.en": "Marunouchi",
     "name.jp": "丸ノ内線",
     "color": "red",
     "number": 4,
     "sign": "M"
    }
  ]
 }
}

def find_line_by_number(data, number):
    matches = [line for line in data if line['number'] == number]
    print(matches)
    if len(matches) > 0:
        # print(matches[0])
        return matches[0]
    else:
        raise ValueError(f"Line {number} does not exist.")

find_line_by_number(data["network"]["lines"], 3)
print([line for line in data])