# parse_resume.py

resume_text = """
ABHIJEET PADWAL
Charoli-phata, Pune
abhijeet.padwal21@vit.edu
7249427053

OBJECTIVE
Dedicated and enthusiastic engineering student with a strong academic background seeking opportunities to apply and further develop technical skills in a challenging and innovative environment.

SKILLS
Programming Languages: C, CSS, HTML, Java, JavaScript, Python
Data Structures and Algorithms
Object-Oriented Programming (OOPs)
Computer Vision
Database Management System
Git and GitHub

CERTIFICATION
IBM Full Stack Software Developer Professional Certificate (In Progress)
Issued by IBM, provided by Coursera
Expected Completion: September 2024
Key Courses: HTML, CSS, JavaScript, Git, React, Node.js, Python, Django, Docker, Kubernetes, Microservices
Skills: Full-stack development, cloud services, DevOps tools, AI applications

EDUCATION
Bachelor of Technology (B.Tech) in Electronics and Telecommunication Engineering
Vishwakarma Institute of Technology, Bibwewadi, Pune
Expected Graduation: 2025

Higher Secondary Certificate (HSC)
MIT Junior College, Pune
Percentage: 83.83%
Year of Passing: 2021

Secondary School Certificate (SSC)
Army Public School Dighi, Pune
Percentage: 74%
Year of Passing: 2019

Projects
Hostel Management System
Developed a comprehensive hostel management system that efficiently handles student registrations, room allocations, and inventory management.
Implemented the back-end using PHP and MySQL, and the front-end using JavaScript, HTML, and CSS to store and retrieve student and hostel information securely.

Smart Ticketing System and Overcrowding Control
Created a smart ticketing system using RFID technology for the ticketing process for public transportation.
Implemented GSM technology to send real-time messages to the transportation authorities and passengers for timely interventions.
The research paper has been published in the IEEE Conference

Advancing Landmark Detection: A Vision Transformer Approach
Developed a deep learning-based advanced ViT image classifier for identifying landmarks. Achieved high accuracy in dynamic conditions by leveraging Vision Transformer architecture.
Implemented using PyTorch and Google Colab, enhancing applications in tourism, navigation, and cultural heritage preservation.
The research paper has been accepted at the IEEE Conference
"""

# A function to parse the resume text and convert it to JSON
def parse_resume_to_json(resume_text):
    resume_json = {
        "contact_information": {
            "name": "Abhijeet Padwal",
            "phone": "7249427053",
            "email": "abhijeet.padwal21@vit.edu",
            "address": "Charoli-phata, Pune"
        },
        "objective": "Dedicated and enthusiastic engineering student with a strong academic background seeking opportunities to apply and further develop technical skills in a challenging and innovative environment.",
        "skills": [
            "Programming Languages: C, CSS, HTML, Java, JavaScript, Python",
            "Data Structures and Algorithms",
            "Object-Oriented Programming (OOPs)",
            "Computer Vision",
            "Database Management System",
            "Git and GitHub"
        ],
        "certifications": [
            {
                "name": "IBM Full Stack Software Developer Professional Certificate",
                "issuer": "IBM",
                "platform": "Coursera",
                "status": "In Progress",
                "expected_completion": "September 2024",
                "key_courses": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "Git",
                    "React",
                    "Node.js",
                    "Python",
                    "Django",
                    "Docker",
                    "Kubernetes",
                    "Microservices"
                ],
                "skills_covered": [
                    "Full-stack development",
                    "Cloud services",
                    "DevOps tools",
                    "AI applications"
                ]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Technology (B.Tech) in Electronics and Telecommunication Engineering",
                "institution": "Vishwakarma Institute of Technology, Bibwewadi, Pune",
                "expected_graduation": "2025"
            },
            {
                "qualification": "Higher Secondary Certificate (HSC)",
                "institution": "MIT Junior College, Pune",
                "percentage": "83.83%",
                "year_of_passing": "2021"
            },
            {
                "qualification": "Secondary School Certificate (SSC)",
                "institution": "Army Public School Dighi, Pune",
                "percentage": "74%",
                "year_of_passing": "2019"
            }
        ],
        "projects": [
            {
                "name": "Hostel Management System",
                "description": "Developed a comprehensive hostel management system that efficiently handles student registrations, room allocations, and inventory management.",
                "technologies": [
                    "PHP",
                    "MySQL
