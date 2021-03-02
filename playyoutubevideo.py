from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def VideoGetter():
    opt='n'

    while opt!='n' or opt !='N':
      driver= webdriver.Chrome()
      driver.maximize_window()

      search_qury=input("Enter a youtuber or a video title to play:")
      driver.get("https://www.youtube.com/results?search_query="+str(search_qury))
      wait=WebDriverWait(driver,10)
      presence=EC.presence_of_element_located
      visible= EC.visibility_of_element_located



      wait.until(visible((By.NAME,"search_query")))

      try:

    # Play the video.
          wait.until(visible((By.ID, "video-title")))
          driver.find_element_by_id("video-title").click()
      except:
          print("ERROR Playing Video!!!")
   
        
    
      opt=input("Play Another one?(y/n):")
      driver.quit()
      
      return 0
  