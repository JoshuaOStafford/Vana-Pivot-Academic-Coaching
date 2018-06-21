from datetime import datetime, timedelta


def get_week_score_average(start_week, duration, all_scores):
    reports = get_week_range(start_week, duration, all_scores)
    cumulative_score = 0
    for report in reports:
        cumulative_score += report.score
    weighted_score = cumulative_score / reports.count()
    return weighted_score


def get_week_range(week_number, duration, all_scores):
    start_date = None
    if week_number == 1:
        start_date = datetime.strptime('Dec 3 2017', '%b %d %Y')
    elif week_number == 2:
        start_date = datetime.strptime('Dec 10 2017', '%b %d %Y')
    elif week_number == 3:
        start_date = datetime.strptime('Dec 31 2017', '%b %d %Y')
    elif week_number == 4:
        start_date = datetime.strptime('Jan 7 2018', '%b %d %Y')
    elif week_number == 5:
        start_date = datetime.strptime('Jan 14 2018', '%b %d %Y')
    elif week_number == 6:
        start_date = datetime.strptime('Jan 21 2018', '%b %d %Y')
    elif week_number == 7:
        start_date = datetime.strptime('Jan 28 2018', '%b %d %Y')
    elif week_number == 8:
        start_date = datetime.strptime('Mar 4 2018', '%b %d %Y')
    elif week_number == 9:
        start_date = datetime.strptime('Mar 11 2018', '%b %d %Y')
    elif week_number == 10:
        start_date = datetime.strptime('Mar 18 2018', '%b %d %Y')
    elif week_number == 11:
        start_date = datetime.strptime('Apr 1 2018', '%b %d %Y')
    elif week_number == 12:
        start_date = datetime.strptime('Apr 8 2018', '%b %d %Y')
    elif week_number == 13:
        start_date = datetime.strptime('Apr 15 2018', '%b %d %Y')
    elif week_number == 14:
        start_date = datetime.strptime('Apr 22 2018', '%b %d %Y')
    end_date = start_date + timedelta(days=duration*7)
    reports = []
    for report in all_scores:

        if start_date <= report.date <= end_date:
            reports.append(report)
    return reports

