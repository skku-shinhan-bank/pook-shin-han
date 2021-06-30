from src.app import App
import sys

if __name__=="__main__":
  print('START - POOK SHIN HAN')

  if len(sys.argv) == 4:
    debug = sys.argv[1]
    host = sys.argv[2]
    port = sys.argv[3]
    
    app = App()
    app.run(host, port=port, debug=(debug == 'True'))