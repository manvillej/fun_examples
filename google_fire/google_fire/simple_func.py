
import fire
def hello(name):
	return f'Hello {name}!'

def main():
	fire.Fire(hello)

if __name__ == '__main__':
	main()