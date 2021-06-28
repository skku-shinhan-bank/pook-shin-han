from src.app import app
import os

if __name__=="__main__":
  print('START - POOK SHIN HAN')
  
  port = 3000
  debug = False
  
  app.run(debug=debug, port=port)