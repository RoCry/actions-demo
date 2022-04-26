from datetime import datetime

def main():
	print("hello from actions")
	with open("./actions.txt", "a") as f:
		f.write(f"hello from actions {datetime.now()}\n")


if __name__ == '__main__':
	main()
