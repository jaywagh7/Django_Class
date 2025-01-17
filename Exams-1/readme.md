# Django Basics - Exam 1

## Project Overview
This project was created as part of the Django Basics examination conducted by **Aakanksha Baishwade**. The examination included theoretical multiple-choice questions and a practical task to build a Django project.

### Teacher: Aakanksha Baishwade  
### Student: Jayesh A. Wagh  
### Total Marks: 100  
### Submission Deadline: End of the Day  

---

## Project Details

### Section A: Multiple Choice Questions (50 Marks)
The theoretical part of the exam tested foundational knowledge of Django. The answers to all multiple-choice questions are included in the `answers.pdf` file in this repository.

### Section B: Practical Task (50 Marks)
The practical task involved creating a Django project and implementing specific requirements. Below are the details of the task.

#### **Practical Task Instructions**
1. **Create a Django Project**:
   - Project Name: `BasicExam`
   - App Name: `teachers`

2. **Model Creation**:
   - A model named `Teacher` was created with the following fields:
     - `id`: Primary Key (Auto Field)
     - `name`: CharField (max_length=50)
     - `subject`: CharField (max_length=100)
     - `email`: EmailField
   - The model was registered in the admin panel, and a superuser was created to manage the data.

---

## Installation and Setup

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BasicExam
