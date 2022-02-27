class HelloWorld:
    
    def __init__(self):
        self.text = "Hello World"
        
    def __call__(self):
        print(self.text)
        
        
def main():
    helloworld = HelloWorld()
    helloworld()

    
if __name__ == '__main__':
    main()
