"""
Retrieves the Texas enrollment data

The following website https://oraapp.doe.k12.ga.us/ows-bin/owa/fte_pack_enrollgrade.entry_form contains a wealth of information regarding
high school enrollments by grade level. This program will help you download the .csv files into your local directory.

Provide it a list of years, list of summaries, and a list of groupings and it will download the csv's in the following
directories:

/.year/summary/groupings/year_summary_groupings.csv
"""
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


class RetrieveGeorgiaData:
 
    def __init__(self):

        self.year_mapping = {"12":"2012", "13":"2013", "14":"2014", "15":"2015", "16":"2016", "17":"2017", "18":"2018", "19":"2019",  "20":"2020",  "21":"2020"}
        self.valid_summaries = {"so": "Statewide County Totals"}
        self.valid_levels = {"g": {"grouping":"Grade", "pack":"enrollgrade", "level":"ALLSYS"},
                             "se": {"grouping":"Gender and Ethnicity","pack":"ethnicsex_pub", "level":"LEA" },
                             "d": {"grouping": "Disability", "pack": "swd_enroll_pub", "level": "LEA"}}

        # self.valid_groupings = {"e": "Ethnicity", "s": "Gender", "g": "Grade", "se": "Gender and Ethnicity",
        #                      "gi": "Grade and Ethnicity", "gs": "Grade and Gender"}

    def download_data(self, years, select_summaries, select_quarters, select_levels):
        urls_to_retrieve = []
        #input: list of years, list of summaries, list of quarters

        for year in years:
            for summary in select_summaries:
                for level in select_levels:



                    human_year = self.year_mapping[year]
                    human_summary = self.valid_summaries[summary]
                    human_group = self.valid_levels[level]["grouping"]
                    folder_location = "{year}/{summary}/{group}".format(year=human_year, summary=human_summary, group=human_group)

                    for quarter in select_quarters:

                        new_url = self.create_url(human_year, quarter, level)
                        urls_to_retrieve.append((folder_location, new_url))

        self.write_urls(urls_to_retrieve)


    def write_urls(self, urls_to_retrieve):

        processes = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            for url in urls_to_retrieve:
                processes.append(executor.submit(self.worker_write_request, url))

        for task in as_completed(processes):
            print(task.result())

    def worker_write_request(self, folder_url):

        try:
            path, url = folder_url
            dest_folder = "./" + path
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)  # create folder

            r = requests.get(url, allow_redirects=True)
            filename = r.headers.get('content-disposition').split("\"")
            name = filename[0][9:]

            mycontent = "\n".join(str(r.content, 'utf-8').split("\n")[4:])

            with open(dest_folder + "/" + name, 'w') as f:
                f.write(mycontent)
                f.close()
        except Exception as ex:
            print("Error writing: ", folder_url, " | with exception: ", ex)



    def create_url(self, year, quarter, level):
        # returns a url in the following format

        base_url = "https://oraapp.doe.k12.ga.us/ows-bin/owa/"
        download_url = "fte_pack_{}.download_allsys".format(self.valid_levels[level]["pack"])
        fiscal_year_url = "?p_fiscal_year={}{}&p_system_id=ALL".format(year, quarter)
        report_level_url = "&p_report_level={}".format(self.valid_levels[level]["level"])

        return base_url + download_url + fiscal_year_url + report_level_url

# Test Cases for create_url
datahelper = RetrieveGeorgiaData()


# assert to prevent regression issues.
assert datahelper.create_url("21", 1, "g") == "https://oraapp.doe.k12.ga.us/ows-bin/owa/" \
                                               "fte_pack_enrollgrade.download_allsys" \
                                               "?p_fiscal_year=211&p_system_id=ALL" \
                                               "&p_report_level=ALLSYS"
# Downloads the Following Years:

test_years = ["12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
test_select_summaries = ["so"]
test_select_quarters = [1, 3]

test_levels = ["se", "g", "d"]

datahelper.download_data(test_years, test_select_summaries, test_select_quarters, test_levels)