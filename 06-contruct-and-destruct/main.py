class Logger:

    def __init__(self):
        print("object is CREATED ") # CONSTRUCTOR

    def __del__(self):
        print("Object is deleted or programe is ended ")

if __name__ == "__main__":
    loggr = Logger()
    del_end = Logger()        
