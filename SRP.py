class Report:
    def __init__(self,title,description):
        self.title = title
        self.description = description

class ReportPrinter:

    def print_report(self ,report: Report):
        print(report.title)
        print(report.description)

def main():
    title = input("Enter your title: ")
    description = input("Enter your description: ")
    report =Report(title,description)
    printer=ReportPrinter()
    printer.print_report(report)

if __name__ == "__main__":
    main()


