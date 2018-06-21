from datetime import datetime, timedelta, date


def get_week_score_average(start_week, duration, all_scores):
    reports = get_week_range(start_week, duration, all_scores)
    cumulative_score = 0
    date_string = ""
    for report in reports:
        cumulative_score += report.score * 100
        date_string += report.date + ' '
    weighted_score = cumulative_score / len(reports)
    return str(weighted_score) + ' out of ' + str(len(reports)) + ' reports on ' + date_string


def get_week_range(week_number, duration, all_scores):
    start_date_dictionary = [date(2017, 12, 3), date(2017, 12, 10), date(2017, 12, 31), date(2018, 1, 7), date(2018, 1, 14),
                             date(2018, 1, 21), date(2018, 1, 28), date(2018, 2, 4), date(2018, 2, 11), date(2018, 2, 18),
                             date(2018, 2, 25), date(2018, 3, 4), date(2018, 3, 11), date(2018, 3, 18), date(2018, 4, 1),
                             date(2018, 4, 8), date(2018, 4, 15), date(2018, 4, 22)]
    start_date = start_date_dictionary[week_number-1]
    end_date = start_date + timedelta(days=duration*7)
    reports = []
    for report in all_scores:
        if start_date <= report.date <= end_date:
            reports.append(report)
    return reports

