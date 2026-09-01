# Python Program for Skill Portfolio

class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Project:
    def __init__(self, name, technology, status):
        self.name = name
        self.technology = technology
        self.status = status

class Certificate:
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform

class Achievement:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.skills = []
        self.projects = []
        self.certificates = []
        self.achievements = []

    def add_skill(self):
        name = input("Enter skill name: ")
        level = input("Enter skill level (Beginner, Intermediate, Advanced): ")
        skill = Skill(name, level)
        self.skills.append(skill)
        print("Skill added successfully!")

    def add_project(self):
        name = input("Enter project name: ")
        technology = input("Enter technology used: ")
        status = input("Enter project status (Completed/Ongoing): ")
        project = Project(name, technology, status)
        self.projects.append(project)
        print("Project added successfully!")

    def add_certificate(self):
        name = input("Enter certificate name: ")
        platform = input("Enter platform: ")
        certificate = Certificate(name, platform)
        self.certificates.append(certificate)
        print("Certificate added successfully!")

    def add_achievement(self):
        title = input("Enter achievement title: ")
        description = input("Enter description: ")
        achievement = Achievement(title, description)
        self.achievements.append(achievement)
        print("Achievement added successfully!")

    def view_portfolio(self):
        print("\n" + "=" * 75)
        print(" " * 25 + "STUDENT PORTFOLIO")
        print("=" * 75)
        print("Name       :", self.name)
        print("Student ID :", self.student_id)
        print("Course     :", self.course)

        print("\n" + "-" * 15 + " SKILLS " + "-" * 15)
        if self.skills:
            for skill in self.skills:
                print(f"{skill.name} - {skill.level}")
        else:
            print("No skills added.")

        print("\n" + "-" * 15 + " PROJECTS " + "-" * 15)
        if self.projects:
            for project in self.projects:
                print(f"{project.name} | {project.technology} | {project.status}")
        else:
            print("No projects added.")

        print("\n" + "-" * 15 + " CERTIFICATIONS " + "-" * 15)
        if self.certificates:
            for certificate in self.certificates:
                print(f"{certificate.name} | {certificate.platform}")
        else:
            print("No certifications added.")

        print("\n" + "-" * 15 + " ACHIEVEMENTS " + "-" * 15)
        if self.achievements:
            for achievement in self.achievements:
                print(f"{achievement.title} | {achievement.description}")
        else:
            print("No achievements added.")

        print("=" * 75)

print("=" * 75)
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course = input("Enter course: ")
student = Student(name, student_id, course)

while True:
    print("\n==================== SKILL PORTFOLIO ====================")
    print("1. Add Skill")
    print("2. Add Project")
    print("3. Add Certificate")
    print("4. Add Achievement")
    print("5. View Portfolio")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student.add_skill()
        elif choice == 2:
            student.add_project()
        elif choice == 3:
            student.add_certificate()
        elif choice == 4:
            student.add_achievement()
        elif choice == 5:
            student.view_portfolio()
        elif choice == 6:
            print("Thanks for using Skill Portfolio System!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
