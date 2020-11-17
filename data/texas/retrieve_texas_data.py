"""
Retrieves the Texas enrollment data

The following website https://rptsvr1.tea.texas.gov/adhocrpt/adste.html contains a wealth of information regarding
high school enrollments. This program will help you download the .csv files into your local directory.

Provide it a list of years, list of summaries, and a list of groupings and it will download the csv's in the following
directories:

/.year/summary/groupings/year_summary_groupings.csv
"""
import requests
import os

class RetrieveTexasData:
    def __init__(self):


        self.year_mapping = {"12":"2012", "13":"2013", "14":"2014", "15":"2015", "16":"2016", "17":"2017", "18":"2018", "19":"2019",  "20":"2020"}
        self.valid_summaries = {"ss": "Statewide Totals" , "sr": "Statewide Region Totals", "so": "Statewide County Totals",
"sd": "Statewide District Totals", "sc":"Statewide Campus Totals", "rr": "Selected Regionwide Totals", "ro":"Selected Regionwide County Totals",
"rd": "Selected Regionwide District Totals", "rc": "Selected Regionwide Campus Totals", "oo":"Selected Countywide Totals", "od":"Selected Countywide District Totals",
"oc": "Selected Countywide Campus Totals", "id": "Selected District Totals using district number",
 "dd": "Selected District Totals using district name", "ic":"Selected Campus Totals using district number",
 "ic": "Selected Campus Totals using district number", "dc": "Selected Campus Totals using district name",
 "nc": "Selected Campus Totals using campus number", "cc":"Selected Campus Totals using campus name"}

        self.valid_groupings = {"e":"Ethnicity", "s":"Gender", "g":"Grade", "se":"Gender and Ethnicity",
                                "gi":"Grade and Ethnicity", "gs":"Grade and Gender"}

    def download_data(self, years, select_summaries,select_groupings):
        # todo: the ability to use 18 or 2018
        # todo: shorthand for select_summaires and select groupings will be usefull too
        # todo: verify input years, select_summaries, select_groupings, we want to throw an error.
        urls_to_retrieve = []
        #input: list of years, list of summaries, list of groupings

        for year in years:
            for summary in select_summaries:
                for group in select_groupings:

                    human_year =  self.year_mapping[year]
                    human_summary = self.valid_summaries[summary]
                    human_group = self.valid_groupings[group]

                    folder_location = "{year}/{summary}/{group}/"\
                        .format(year=human_year, summary=human_summary, group=human_group)

                    new_url = self.create_url(year, summary, group)
                    urls_to_retrieve.append((folder_location, new_url))

        self.write_urls(urls_to_retrieve)



    def write_urls(self, urls_to_retrieve):

        errors = [] # list of files that we couldn't write

        # Lets grab the urls and put them in our folder.
        for folder_url in urls_to_retrieve:
            try:
                path, url = folder_url
                print("Writing:", path, url)
                dest_folder= "./" + path
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)  # create folder

                r = requests.get(url, allow_redirects=True)
                filename = r.headers.get('content-disposition').split("\"")
                name = filename[-2]

                with open(dest_folder + name, 'wb') as f:
                    f.write(r.content)
            except:
                errors.append(folder_url)

        print("We had errors with the following files", errors)





    def create_url(self, year, select_summary,select_grouping):
        # returns a url in the following format

        start_url = "https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=marykay&_program=adhoc.addispatch.sas&major=st&minor=e&charsln=120&linespg=60&_debug=0"
        year_download = "&endyear={year}&".format(year=year)
        select_summary_download = "selsumm={select_summary}&key=TYPE HERE&".format(select_summary=select_summary)
        select_grouping_download = "grouping={select_grouping}&format=C".format(select_grouping=select_grouping)

        return start_url + year_download + select_summary_download + select_grouping_download

# Test Cases for create_url
datahelper = RetrieveTexasData()

# assert to prevent regression issues.
assert datahelper.create_url("20", "ss","gs") == "https://rptsvr1.tea.texas.gov/cgi/sas/broker?_service=" \
                                                 "marykay&_program=adhoc.addispatch.sas&major=st&minor=e&charsln=120" \
                                                 "&linespg=60&_debug=0&endyear=20&selsumm=ss" \
                                                 "&key=TYPE HERE&grouping=gs&format=C"

# Downloads the Following Years:

test_years = ["19", "20"]
test_select_summaries = ["ss", "sr", "so", "sd", "sc", "rr", "ro", "rd", "rc", "oo", "od", "oc", "id", "dd", "ic", "dc", "nc", "cc" ]
test_select_grouping = ["e", "s", "g", "se", "gi", "gs"]

datahelper.download_data(test_years,test_select_summaries,test_select_grouping)