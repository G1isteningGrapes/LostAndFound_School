# Logic: takes the data from the GUI dropdowns, sorts it, and stores it.
import config
import json
from datetime import datetime

MAX_REPORTS = 100
DATE_FORMAT = "%m/%d/%Y"  

STATUS_REPORTED = "reported"
STATUS_CLAIMED = "claimed"
STATUS_RETURNED = "returned"

# Item types
VALID_ITEM_TYPES = config.items #fetching from the config file

reports = []


def loadReports():
    try:
        file = open("reports.json", "r")
        saved = json.load(file)
        file.close()
        return saved
    except FileNotFoundError:
        return []


def saveReports():
    file = open("reports.json", "w")
    json.dump(reports, file, indent=2)
    file.close()


def isValidReport(location, item_type, date_text, description, email, student_id):
    if location == "":
        print("Error: location is empty.")
        return False
    if item_type not in VALID_ITEM_TYPES:
        print("Error: pick an item type from the list.")
        return False
    try:
        datetime.strptime(date_text, DATE_FORMAT)
    except ValueError:
        print("Error: date must look like MM/DD/YYYY.")
        return False
    if description == "":
        print("Error: description is empty.")
        return False
    if email == "":
        print("Error: email is empty.")
        return False
    if student_id == "":
        print("Error: student ID is empty.")
        return False
    return True


def getDate(report):
    # Turn MM/DD/YYYY into a real date so sorting puts the newest first.
    return datetime.strptime(report["date"], DATE_FORMAT)


def submitLostReport(location, item_type, lost_date, description, email, student_id):
    if not isValidReport(location, item_type, lost_date, description, email, student_id):
        return None
    if len(reports) >= MAX_REPORTS:
        print("Error: the database is full (100 reports).")
        return None
    new_report = {
        "report_id": len(reports) + 1,
        "report_type": "lost",
        "location": location,
        "item_type": item_type,
        "date": lost_date,
        "description": description,
        "email": email,
        "student_id": student_id,
        "status": STATUS_REPORTED,
    }
    reports.append(new_report)
    reports.sort(key=getDate, reverse=True)
    saveReports()
    return new_report


def submitFoundReport(location, item_type, found_date, description, email, student_id):
    if not isValidReport(location, item_type, found_date, description, email, student_id):
        return None
    if len(reports) >= MAX_REPORTS:
        print("Error: the database is full (100 reports).")
        return None
    new_report = {
        "report_id": len(reports) + 1,
        "report_type": "found",
        "location": location,
        "item_type": item_type,
        "date": found_date,
        "description": description,
        "email": email,
        "student_id": student_id,
        "status": STATUS_REPORTED,
    }
    reports.append(new_report)
    reports.sort(key=getDate, reverse=True)
    saveReports()
    return new_report


def getReportById(report_id):
    for report in reports:
        if report["report_id"] == report_id:
            return report
    return None


def searchReportsByCategory(item_type):
    result = []
    for report in reports:
        if report["item_type"] == item_type:
            result.append(report)
    result.sort(key=getDate, reverse=True)
    return result


def findMatches(report_id):
    report = getReportById(report_id)
    if report is None:
        print("Error: no report with that id.")
        return []
    if report["report_type"] == "lost":
        other_type = "found"
    else:
        other_type = "lost"
    result = []
    for other in reports:
        if other["report_type"] == other_type and other["item_type"] == report["item_type"] and other["location"] == report["location"]:
            result.append(other)
    result.sort(key=getDate, reverse=True)
    return result


def submitClaim(report_id, student_id):
    report = getReportById(report_id)
    if report is None:
        print("Error: no report with that id.")
        return None
    if report["report_type"] != "lost":
        print("Error: only a lost item can be claimed.")
        return None
    if report["status"] != STATUS_REPORTED:
        print("Error: this report is already " + report["status"] + ".")
        return None
    report["status"] = STATUS_CLAIMED
    report["claimed_by"] = student_id
    saveReports()
    return report


def markReturned(report_id):
    report = getReportById(report_id)
    if report is None:
        print("Error: no report with that id.")
        return None
    if report["status"] != STATUS_CLAIMED:
        print("Error: only a claimed item can be marked returned.")
        return None
    report["status"] = STATUS_RETURNED
    saveReports()
    return report


reports = loadReports()


if __name__ == "__main__":
    print(submitLostReport("Acadia Library", "Keys", "11/14/2026",
                           "Keychain with a blue tag",
                           "student@acadiau.ca", "0311732"))
    print(submitFoundReport("Acadia Library", "Keys", "11/15/2026",
                            "Keys found near the front desk",
                            "finder@acadiau.ca", "0314000"))
    print(searchReportsByCategory("Keys"))
    print(findMatches(1))
    print(submitClaim(1, "0311732"))
    print(markReturned(1))
    print(reports)
