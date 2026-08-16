def read_logs():

    try:
        with open ("app.logs","r") as file:
            logs = file.read()

        return logs

    except FileNotFoundError:
        print("No file to load")
        return None


def count_log_levels(logs):
    lines = logs.splitlines()

    info = 0
    warning = 0
    error = 0

    for line in lines:
        if "INFO" in line:
            info += 1

        elif "WARNING" in line:
            warning +=1

        elif "ERROR" in line:
            error += 1

    return {
        "INFO": info,
        "WARNING": warning,
        "ERROR": error
    }


def find_errors(logs):
    errors = []

    lines = logs.splitlines()

    for line in lines:
        if "ERROR" in line:
            errors.append(line)

    return(errors)


def find_warnings(logs):
    warnings = []

    lines = logs.splitlines()

    for line in lines:
        if "WARNING" in line:
            warnings.append(line)

    return(warnings)


def most_common_error(errors):

    error_counts = {}

    for error in errors:
        message = " ".join(error.split()[3:])

        if message in error_counts:
            error_counts[message] +=1

        else:
            error_counts[message] = 1

    highest_count = 0
    most_common = None

    for error, count in error_counts.items():
        if count> highest_count:
            highest_count = count
            most_common = error

    return most_common


def generate_report(logs):
    print("======= LOG REPORT =======")
    counts = count_log_levels(logs)
    errors = find_errors(logs)
    warnings = find_warnings(logs)
    common_error = most_common_error(errors)

    total_logs = sum(counts.values())
    print("Total Logs: ", total_logs)

    print("\nINFO:", counts["INFO"])
    print("WARNING:", counts["WARNING"])
    print("ERROR:", counts["ERROR"])

    print("\nMost Common Error: ", common_error)

    total_errors = len(errors)
    print("Total Errors: ", total_errors)

    total_warnings = len(warnings)
    print("Total Warnings: ", total_warnings)


if __name__ == "__main__":
    logs = read_logs()

    if logs:
        generate_report(logs)