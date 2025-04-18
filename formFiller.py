from selenium import webdriver
from selenium.webdriver.common.by import By

def read_jobs(file_name):
    my_list = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = [part.strip() for part in line.split(",")]
            if len(parts) == 5:
                date, company, website, position, position_id = parts
                month, day, year = date.split("/")
                entry = {
                    "month": month,
                    "day": day,
                    "year": year,
                    "company": company,
                    "website": website,
                    "position": position,
                    "position_id": position_id
                }
                my_list.append(entry)
            else:
                print(f"Invalid line format, expected five comma separated items: {line.strip()}")
        return my_list

def load_jobs(driver, my_list):
    for entry in my_list:

        # PAGE - Job list page
        driver.find_element(By.ID, "cphMain_cphMain_btnAdd").click()
    
        # PAGE - Job entry page
        driver.waitFor_element(By.ID, "cphMain_cphMain_txtDate_txtDate_dateMonth", timeout=5)
        driver.find_element(By.ID, "cphMain_cphMain_txtDate_txtDate_dateMonth").send_keys(entry['month'])
        driver.find_element(By.ID, "cphMain_cphMain_txtDate_txtDate_dateDay").send_keys(entry['day'])
        driver.find_element(By.ID, "cphMain_cphMain_txtDate_txtDate_dateYear").send_keys(entry['year'])
        driver.find_element(By.ID, "cphMain_cphMain_txtCompanyName").send_keys(entry['company'])
        driver.find_element(By.ID, "cphMain_cphMain_ddlTypeOfContact").drop_down("Internet Job Site")
        driver.find_element(By.ID, "cphMain_cphMain_ddlMethodOfContact").drop_down("Internet Application")
        
        driver.waitFor_element(By.ID, "cphMain_cphMain_txtWebsiteAddress", timeout=5)
        driver.find_element(By.ID, "cphMain_cphMain_txtWebsiteAddress").send_keys(entry['website'])
        driver.find_element(By.ID, "cphMain_cphMain_txtPositionAppliedFor").send_keys(entry['position'])
        if entry['position'] != "none":
            driver.find_element(By.ID, "cphMain_cphMain_txtReferenceNumber").send_keys(entry['position_id'])
    
        driver.find_element(By.ID, "cphMain_cphMain_ddlResultOfApplication").drop_down("Application/Resume Submitted")
        driver.find_element(By.ID, "cphMain_cphMain_btnNext").click()       

def __main__():
    driver = webdriver.Chrome()
    driver.get("connect.myflorida.com")
    
    #insert breakpoint 1 of 2 here. Login and answer the questions. Navigating to the jobs page.
    print("Insert breakpoint here. Manually complete login.")

    load_jobs(driver, read_jobs("jobs.txt"))

    #insert breakpoint 2 of 2 here. Complete forms and logout. 
    print("Insert breakpoint here. Manually complete submitting and logout.")

    driver.quit()

if __name__ == "__main__":
    __main__()
        