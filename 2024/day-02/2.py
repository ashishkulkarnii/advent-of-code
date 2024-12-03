def report_is_safe(report: list[int]) -> bool:
    increasing = report[0] < report[1]
    
    for i in range(1, len(report)):
        if not ((report[i] > report[i-1]) is increasing) or not (1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return True


def damp_report_is_safe(report: list[int]) -> bool:
    return report_is_safe(report) or any([report_is_safe(report[0:i] + report[i+1:]) for i in range(len(report))])


with open("input.txt", "r") as f:
    reports = [[int(level) for level in report.split()] for report in f.readlines()]

safe_reports = 0
for report in reports:
    safe_reports += damp_report_is_safe(report)

print(safe_reports)
