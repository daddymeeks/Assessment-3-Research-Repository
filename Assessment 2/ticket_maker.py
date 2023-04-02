class Ticket():
    ticket_id: str
    staff_id: str
    name: str
    email: str
    issue_description: str
    response: str
    status: str

    def __init__(self, ticket_id, staff_id, name, email, issue_description, response="Not yet provided", status="OPEN"):
        self.ticket_id = ticket_id
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.issue_description = issue_description
        self.response = response
        self.status = status
        
    def display(self):
        print("Ticket ID:", self.ticket_id)
        print("Staff ID:", self.staff_id)
        print("Name: ", self.name)
        print("Issue Description: ", self.issue_description)
        print("Response:", self.response)
        print("Status: ", self.status)
        print()
