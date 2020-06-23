from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os
import csv
from copy import copy
import getpass

class WhatsappBot:
    def __init__(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "venv/bin/chromedriver")

        self.driver = webdriver.Chrome(executable_path=DRIVER_BIN)
        self.driver.get("https://web.whatsapp.com/")

        # firefox_options = webdriver.FirefoxOptions()
        # browser = webdriver.Remote(
        #     command_executor='https://selenium.grow90.tools/wd/hub',
        #     options=firefox_options
        # )
        self.firsttry = True

    def send(self, nums, msgs):
        not_in_cont = []
        in_contacts = []
        for con in nums:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').click()
            # sleep(1)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(con)
            sleep(2)
            person = self.driver.find_elements_by_xpath(
                "//div[@class='_210SC' and contains(@style,'transform: translateY(72px);')]")
            if len(person) == 0:
                print(con, "is not there in your contacts")
                not_in_cont.append([con])
                tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
                while len(tempCheckElement)==0:
                    tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
                tempCheckElement[0].click()
                continue
            in_contacts.append([con])
            person[0].click()
            # sleep(1)

            for lines in msgs:
                for line in lines:
                    tempCheckElement = self.driver.find_elements_by_xpath(
                        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                    while len(tempCheckElement) == 0:
                        tempCheckElement = self.driver.find_elements_by_xpath(
                            "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                    tempCheckElement[0].send_keys(line)
                    self.driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(
                        Keys.SHIFT, Keys.ENTER)

                sleep(1)
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
        return not_in_cont, in_contacts

    def send_image(self, nums, captions, path, n_caps):
        not_in_cont = []
        in_cont = []
        for con in nums:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').click()
            # sleep(1)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(con)
            sleep(2)
            person = self.driver.find_elements_by_xpath(
                "//div[@class='_210SC' and contains(@style,'transform: translateY(72px);')]")
            if len(person) == 0:
                print(con, "is not there in your contacts")
                not_in_cont.append([con])
                tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
                while len(tempCheckElement) == 0:
                    tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
                tempCheckElement[0].click()
                continue
            in_cont.append([con])
            person[0].click()
            # sleep(1)

            self.driver.find_element_by_xpath("//div[@role='button' and @title='Attach']").click()
            # sleep(1)
            tempCheckElement = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input")
            while len(tempCheckElement) == 0:
                tempCheckElement = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input")
            tempCheckElement[0].send_keys(path)

            # sleep(1)
            if len(captions)>1:
                pic_buttons = self.driver.find_elements_by_xpath(
                    "//div[@class='_2gZno']")
                while len(pic_buttons) == 0:
                    pic_buttons = self.driver.find_elements_by_xpath(
                        "//div[@class='_2gZno']")
            # pic_buttons[0].send_keys(path)

            # pic_buttons = self.driver.find_elements_by_xpath("//div[@class='_2gZno']")
            # print("Number of images : ", len(pic_buttons)+1)

            counter = 0
            sleep(1)
            for lines in captions:
                for line in lines:
                    self.driver.find_element_by_xpath(
                        "//div[@class='_3FRCZ copyable-text selectable-text' and @contenteditable='true']").send_keys(
                        line)
                    self.driver.find_element_by_xpath(
                        "//div[@class='_3FRCZ copyable-text selectable-text' and @contenteditable='true']").send_keys(
                        Keys.SHIFT, Keys.ENTER)
                if counter != n_caps-1:
                    pic_buttons[counter].click()
                counter += 1

            # sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
            sleep(2)
        return not_in_cont, in_cont

    def get_numbers_group(self, grp):
        self.default_name = input("Enter Default name : ")
        self.numbers = {}
        self.names = []
        self.counter = 0
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').click()
        # sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]').send_keys(grp)
        sleep(2)
        group = self.driver.find_elements_by_xpath(
            "//div[@class='_210SC' and contains(@style,'transform: translateY(72px);')]")
        if len(group) == 0:
            print(grp, "is not there in your chats")
            tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
            while len(tempCheckElement) == 0:
                tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
            tempCheckElement[0].click()
            return
        group[0].click()
        self.driver.find_element_by_xpath("//div[@class='_33QME' and @role='button']").click()
        sleep(1)

        best_element, best_num, best = self.get_numbers()

        more = self.driver.find_elements_by_css_selector("div._18cLH")
        if len(more) == 0 or len(more) == 2:
            return self.numbers, self.names
        if len(more) == 1:
            more[0].click()
        else:
            more[2].click()
        sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", best_element)
        sleep(1)
        prev_best_num = 0
        while prev_best_num != best_num:
            prev_best_num = best_num
            best_element, best_num, best = self.get_numbers()
            # print("BEST One : ", best_num, best)
            self.driver.execute_script("arguments[0].scrollIntoView();", best_element)
            sleep(1)
        tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
        while len(tempCheckElement) == 0:
            tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='MfAhJ']")
        tempCheckElement[0].click()
        return self.numbers, self.names


    def get_numbers(self):
        item = self.driver.find_elements_by_css_selector("div.-GlrD")[0]
        all_items = item.find_elements_by_css_selector("div._210SC")
        # print("\nNumber of People : ", len(all_items), "\n")
        best = 0
        best_element = None
        best_num = None
        for item in all_items:
            given_name = None
            name = item.find_elements_by_css_selector("span._1_1Jb")
            if len(name) != 0:
                given_name = name[0].text
            num = item.find_element_by_css_selector("span._3ko75").text
            temp_num = copy(num)
            temp_num = temp_num.replace(' ', '')
            temp_num = temp_num.replace('+', '')
            if temp_num.isnumeric():
                if num not in list(self.numbers.values()):
                    if given_name != None:
                        fin_name = self.default_name + '_' + given_name
                        self.numbers[fin_name] = num
                    else:
                        fin_name = self.default_name + '_' + str(self.counter)
                        self.numbers[fin_name] = num
                        self.counter += 1
            else:
                if num not in self.names:
                    self.names.append(num)
            pos = int(item.get_attribute('style').split('(')[1].split('p')[0])
            if pos > best:
                best = pos
                best_element = item
                best_num = num
        return best_element, best_num, best

    def google_contacts(self, filepath, window_num):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[window_num])
        self.driver.get("https://contacts.google.com/")
        sleep(1)
        self.driver.find_element_by_xpath("//a[@role='button' and @jsaction='BlwSWe']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@class='Cqj7xc' and @type='file']").send_keys(filepath)
        sleep(1)
        items = self.driver.find_elements_by_xpath("//span[@class='VfPpkd-vQzf8d' and @jsname='V67aGc']")
        items[1].click()
        sleep(8)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[window_num-1])

    def upload_csv(self, filepath):
        if self.firsttry:
            email = input("Enter gmail id : ")
            password = getpass.getpass()
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
            self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
            sleep(3)
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
            sleep(3)

            self.google_contacts(filepath, 2)

            sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.firsttry = False
        else:
            self.google_contacts(filepath, 1)

    def write_numbers_csv(self, file_name, con_list):
        outf = open(file_name, 'w')
        for row in con_list:
            for column in row:
                outf.write('%s' % column)
            outf.write('\n')
        outf.close()

    def end_task(self):
        self.driver.close()


my_bot = WhatsappBot()
inp = input("Enter 'y' to start : ")

while inp.lower() == 'y':
    # contacts = list(pd.read_csv("numbers.csv")["Number"])
    # contacts=['9496327013']

    with open('numbers.csv') as csvfile:
        rd = csv.reader(csvfile)
        contacts = []
        for row in rd:
            contacts.append(row[0])

    choose = int(input("send message: 0, sent image: 1, get numbers in groups: 2   :  "))
    if choose == 0:
        with open('message.txt', 'r') as file:
            message = file.read()
        message_lines = message.split('++')
        # num_captions = len(caption_lines)
        # print(caption_lines)
        messages = []
        for cap in message_lines:
            lines = cap.split('\n')
            if '' in lines:
                lines.remove('')
            messages.append(lines)

        not_in_contacts, in_contacts = my_bot.send(contacts, messages)
        my_bot.write_numbers_csv("not_in_contacts_message.csv", not_in_contacts)
        my_bot.write_numbers_csv("in_contacts_message.csv", in_contacts)
    elif choose == 1:
        with open('image_caption.txt', 'r') as file:
            caption = file.read()
        caption_lines = caption.split('++')
        num_captions = len(caption_lines)
        # print(caption_lines)
        captions = []
        for cap in caption_lines:
            lines = cap.split('\n')
            if '' in lines:
                lines.remove('')
            captions.append(lines)

        with open('image_path.txt', 'r') as file:
            img_path = file.read()
        img_path = img_path.strip()
        # print(img_path)

        not_in_contacts, in_contacts = my_bot.send_image(contacts, captions, img_path, num_captions)
        my_bot.write_numbers_csv("not_in_contacts_image.csv", not_in_contacts)
        my_bot.write_numbers_csv("in_contacts_image.csv", in_contacts)
    elif choose == 2:
        group = input("Enter group name : ")
        nums, names = my_bot.get_numbers_group(group)
        print("Participants : ", len(nums.values())+len(names))
        exp = int(input("export to excel : 0, add to google contacts : 1, both : 2,  : "))
        filename= "grp_numbers"
        if exp==0 or exp==2:
            df = pd.DataFrame(list(zip(list(nums.values()) + names, list(nums.keys()) + names)),columns=['Numbers', 'New Names'])
            df.to_excel(filename+'.xls')
            print(filename+'.xls' , "created.")
            df = pd.DataFrame(list(zip(list(nums.keys()), list(nums.values()))),
                              columns=['First Name', 'Mobile Phone'])
            df.to_csv(filename + '.csv')
            print(filename + '.csv', "created.")
        if exp==1 or exp==2:
            df = pd.DataFrame(list(zip(list(nums.keys()), list(nums.values()))),
                              columns=['First Name', 'Mobile Phone'])
            df.to_csv(filename+'.csv')
            print(filename+'.csv', "created.")
            filepath = os.path.join(os.getcwd(), filename+'.csv')
            my_bot.upload_csv(filepath)
    else:
        print("Invalid input try again!!!")

    inp = input("Enter 'y' to sent message again 'n' to stop : ")
my_bot.end_task()

