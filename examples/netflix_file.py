driver.get('https://www.netflix.com/login')

# email user login
email_login = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
# env user name send input
email_login.send_keys(Env.NETFLIX_USER)
# password login find path
password_login = driver.find_element_by_xpath('//*[@id="id_password"]')
# env password send input
password_login.send_keys(Env.NETFLIX_PASS)
# locate login button
login_button = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
# click login button
login_button.send_keys(Keys.ENTER)

# locate all profiles available
profile_links = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'profile-name')))
# second profile selected
second_profile = profile_links[1]
# choose second profile to select.
second_profile.click()

icon_search = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,'icon-search')))
icon_search.click()