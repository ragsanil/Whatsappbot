from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# import pandas as pd
import os
import csv


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
                "//div[@class='_2wP_Y' and contains(@style,'transform: translateY(72px);')]")
            if len(person) == 0:
                print(con, "is not there in your contacts")
                not_in_cont.append([con])
                tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='_3Burg']")
                while len(tempCheckElement)==0:
                    tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='_3Burg']")
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
                "//div[@class='_2wP_Y' and contains(@style,'transform: translateY(72px);')]")
            if len(person) == 0:
                print(con, "is not there in your contacts")
                not_in_cont.append([con])
                tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='_3Burg']")
                while len(tempCheckElement) == 0:
                    tempCheckElement = self.driver.find_elements_by_xpath("//button[@class='_3Burg']")
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
                        "//div[@class='_2S1VP copyable-text selectable-text' and @contenteditable='true']").send_keys(
                        line)
                    self.driver.find_element_by_xpath(
                        "//div[@class='_2S1VP copyable-text selectable-text' and @contenteditable='true']").send_keys(
                        Keys.SHIFT, Keys.ENTER)
                if counter != n_caps-1:
                    pic_buttons[counter].click()
                counter += 1

            # sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
            sleep(2)
        return not_in_cont, in_cont

    def write_csv(self, file_name, con_list):
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
        my_bot.write_csv("not_in_contacts_message.csv", not_in_contacts)
        my_bot.write_csv("in_contacts_message.csv", in_contacts)
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
        my_bot.write_csv("not_in_contacts_image.csv", not_in_contacts)
        my_bot.write_csv("in_contacts_image.csv", in_contacts)
    elif choose == 2:
        print("Not ready yet")
    else:
        print("Invalid input try again!!!")

    inp = input("Enter 'y' to sent message again 'n' to stop : ")
my_bot.end_task()

