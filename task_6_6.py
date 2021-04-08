from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as bread_a:
	with open("bakery.csv", "r", encoding="utf-8") as bread_r:
		if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit()]:
			if len(argv) == 3:
				print(*bread_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep="\n")
			if "," in argv[1] or "." in argv[1]:
				bread_r.read()
				print(argv[1], file=bread_a)
			else:
				print(*bread_r.readlines()[int(argv[1]) - 1:], sep="")
		else:
			print(bread_r.read())
