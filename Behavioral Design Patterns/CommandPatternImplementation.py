### Command Pattern Implementation

### Scenario: Office Automation System with Task Management

# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Concrete Command: PrintDocumentCommand
class PrintDocumentCommand(Command):
    def __init__(self, printer, document):
        self.printer = printer
        self.document = document

    def execute(self):
        self.printer.print_document(self.document)
    
    def undo(self):
        print(f"Undo print of {self.document}")

# Concrete Command: SendEmailCommand
class SendEmailCommand(Command):
    def __init__(self, email_service, recipient, message):
        self.email_service = email_service
        self.recipient = recipient
        self.message = message

    def execute(self):
        self.email_service.send_email(self.recipient, self.message)
    
    def undo(self):
        print(f"Undo send email to {self.recipient}")

# Concrete Command: GenerateReportCommand
class GenerateReportCommand(Command):
    def __init__(self, report_generator):
        self.report_generator = report_generator

    def execute(self):
        self.report_generator.generate_report()
    
    def undo(self):
        print("Undo report generation")

# Receiver Classes
class Printer:
    def print_document(self, document):
        print(f"Printing document: {document}")

class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class ReportGenerator:
    def generate_report(self):
        print("Generating report...")

# Invoker Class
class TaskQueue:
    def __init__(self):
        self.command_queue = []
        self.history = []

    def add_command(self, command):
        self.command_queue.append(command)

    def execute_commands(self):
        while self.command_queue:
            command = self.command_queue.pop(0)
            command.execute()
            self.history.append(command)
    
    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            print("Last command undone.")
        else:
            print("No command to undo.")

# Client Code (usage example)
if __name__ == "__main__":
    # Create receiver objects
    printer = Printer()
    email_service = EmailService()
    report_generator = ReportGenerator()

    # Create command objects
    print_command = PrintDocumentCommand(printer, "Annual Report")
    email_command = SendEmailCommand(email_service, "john.doe@example.com", "Your report is ready.")
    report_command = GenerateReportCommand(report_generator)

    # Create invoker (TaskQueue)
    task_queue = TaskQueue()

    # Add commands to the queue
    task_queue.add_command(print_command)
    task_queue.add_command(email_command)
    task_queue.add_command(report_command)

    # Execute commands
    print("\nExecuting tasks...")
    task_queue.execute_commands()

    # Undo the last executed command
    print("\nUndoing the last command...")
    task_queue.undo_last_command()

    # Undo the last command again
    print("\nUndoing the last command again...")
    task_queue.undo_last_command()

### Expected Output
# Executing tasks...
# Printing document: Annual Report
# Sending email to john.doe@example.com: Your report is ready.
# Generating report...

# Undoing the last command...
# Undo report generation
# Last command undone.

# Undoing the last command again...
# Undo send email to john.doe@example.com
# Last command undone.
