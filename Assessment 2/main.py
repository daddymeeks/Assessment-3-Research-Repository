from ticket_maker import Ticket

class main():
    @staticmethod
    def main():
        tickets = []
        ticket_counter = 2000
        ticket_amount = 0

        t1 = Ticket(ticket_counter, "MEEKS", "Michael",
                    "20230855@mywhitecliffe.com", "Printer dead!")
        tickets.append(t1)
        ticket_counter += 1
        ticket_amount += 1
        t2 = Ticket(ticket_counter, "CLODS", "Claudia",
                    "20230052@mywhitecliffe.com", "Mouse dead!")
        tickets.append(t2)
        ticket_counter += 1
        ticket_amount += 1

        def new_ticket():
            print("----Creating new ticket----")
            print()
            staff_id = input("ENTER YOUR STAFF ID: ")
            name = input("ENTER YOUR NAME: ")
            email = input("ENTER YOUR EMAIL: ")
            issue_description = input("ENTER YOUR ISSUE: ")
            print()
            print("------Ticket Submitted-----")
            print()
            t = Ticket(ticket_counter, staff_id, name, email, issue_description)
            tickets.append(t)
            t.display()

            if "password" in issue_description.lower():
                new_password = f"{staff_id[:2]}{name[:3]}123"
                print(f"A new password has been generated for you: {new_password}")
                t.response = f"A new password has been generated for you: {new_password}"
                t.status = "CLOSED"


        def display_tickets():
            for t in tickets:
                t.display()

        def responses():
            for t in tickets:
                t.display()
            t_n = int(input("Which ticket number would you like to respond to? "))
            for t in tickets:
                if t.ticket_id == t_n:
                    rs = input("What would you like to respond? ")
                    t.response = rs
                    t.status = "CLOSED"
                    print("\nResponse saved.")
                    t.display()
                    break
            else:
                print("Ticket not found.")

        def reopen():
            closed_tickets = []
            for t in tickets:
                t.display()
                if t.status == "CLOSED":
                    closed_tickets.append(t.ticket_id)

            if not closed_tickets:
                print("There are no closed tickets to reopen.")
                return

            while True:
                re = int(input("Which ticket number would you like to reopen? "))
                if re not in closed_tickets:
                    print("Please choose a ticket that is already closed.")
                else:
                    for t in tickets:
                        if t.ticket_id == re:
                            t.status = "OPEN"
                            print("Ticket reopened.")
                            return

        def display_stats():
            print("---------------------------")
            created_count = len(tickets)
            resolved_count = 0
            to_solve_count = 0
            for t in tickets:
                if t.status == "CLOSED":
                    resolved_count += 1
                else:
                    to_solve_count += 1
            print("Displaying Ticket Statistics")
            print("Tickets Created:", created_count)
            print("Tickets Resolved:", resolved_count)
            print("Tickets To Solve:", to_solve_count) 

        main_menu = -1
        while main_menu != 6:
            print("-------- MAIN MENU --------")
            print()
            print("[1] to display all tickets.")
            print("[2] to submit a new ticket")
            print("[3] to provide a response")
            print("[4] to reopen a ticket")
            print("[5] to display statistics")
            print("[6] to EXIT")
            print()
            print("---------------------------")
            
            main_menu = int(input("Enter your decision: "))
            
            if main_menu == 1:
                print("---------------------------")
                print("** DISPLAYING ALL TICKETS **")
                print()
                display_tickets()
                print("***************************")
            
            elif main_menu == 2:
                new_ticket()
                ticket_counter += 1
                ticket_amount += 1
            
            elif main_menu == 3:
                print("---------------------------")
                responses()
                print("---------------------------")
            
            elif main_menu == 4:
                print("---------------------------")
                reopen()
                print("---------------------------")
            
            elif main_menu == 5:
                print("---------------------------")
                display_stats()
                print("---------------------------")
            
            elif main_menu == 6:
                print("---------------------------")
                print("System shutting down. Have a nice day!")
                quit()
            
            else:
                print("NOT A VALID OPTION")
if __name__ == '__main__':
    main.main()