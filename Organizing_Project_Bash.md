# **Command Line Challenge: Organizing a Project with Bash**

## **Scenario**
You’re creating a directory structure for a coding project. You’ll organize files, edit some content, and search within them—all using Git Bash commands.

---

## **Step-by-Step Tasks**

### **1. Set Up the Project**
- **Navigate to your Desktop**
   
   ```bash
   cd ~/Desktop
   
- **Create a project directory named MyProject**
   
   ```bash
   mkdir MyProject

- **Move into the MyProject directory:**
  
   ```bash
   cd MyProject

- **Create subdirectories named docs, src, and tests:**
   
   ```bash
   mkdir docs src tests

### **2. Create and Organize Files** 
- **Inside the docs folder, create a file called README.md:**
   
   ```bash
   cd docs
   touch README.md
  
- **Go back to the MyProject directory:**
   
   ```bash
   cd ..

- **Create a Python file named app.py inside the src folder:**
   
   ```bash
   touch src/app.py

### **3. Add Content to Files**
- **Edit the README.md file using Notepad and add a project description:**
   
   ```bash
   notepad docs/README.md

- **Add sample Python code to app.py using cat:**
   
   ```bash
   echo "print('Hello, World!')" > src/app.py

- **View the contents of app.py to confirm the code was added:**
   
   ```bash
   cat src/app.py

### **4. Search and Explore**
- **Search for the word print in the src folder to confirm it exists in app.py:**
   
   ```bash
   grep print src/*

- **List all files in the MyProject directory, showing hidden files if any:**
   
   ```bash
   ls -la

### **5. Copy, Move, and Rename**
- **Copy the README.md file from docs to the tests folder:**
   
   ```bash
   cp docs/README.md tests/

- **Rename the copied file in the tests folder to README_copy.md:**
   
   ```bash
   mv tests/README.md tests/README_copy.md

- **Move the app.py file to the root of the project:**
   
   ```bash
   mv src/app.py .

### **6. Cleanup**
- **Delete the empty src folder:**
   
   ```bash
   rm -r src

- **Remove the README_copy.md file in the tests folder:**
   
   ```bash
   rm tests/README_copy.md

### **7. Bonus**
- **Create 3 text files in the docs folder with one command:**
   
   ```bash
   touch docs/file1.txt docs/file2.txt docs/file3.txt

- **View the first 10 lines of one of these files (you’ll see nothing since they’re empty):**
   
   ```bash
   head docs/file1.txt

- **Clear your terminal to remove clutter:**
   
   ```bash
   clear
