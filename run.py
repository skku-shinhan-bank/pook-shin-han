from src.app import app
import sys

if __name__=="__main__":
  print('START - POOK SHIN HAN')

  if len(sys.argv) == 3:
    debug = sys.argv[1]
    port = sys.argv[2]
    
    app.run(debug=debug, port=port)