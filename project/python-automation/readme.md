[Google IT Automation with Python](https://www.coursera.org/professional-certificates/google-it-automation)

Automate tasks by writing Python scripts, Use Git and GitHub for version control, Manage IT resources at scale, both for physical machines and virtual machines in the cloud, Analyze real-world IT problems and implement the appropriate strategies to solve those problems


# Crash Course on Python [Link](https://www.coursera.org/learn/python-crash-course/home/info)

## Module 1/Week 1: Hello Python! 
- https://www.python.org/shell
- https://trinket.io/python3
- https://replit.com/languages/python3


## Module 2: Basic Python Syntax 
- past notes on python https://github.com/mguery/python
- expressions and vars 
```
base = 6
height = 3
area = (base*height)/2
print("area of triangle is: " + str(area))
```

- functions
```python
def greeting(name, department):
  print("Welcome, " + name)
  print("you're in " + department)

greeting("MG", "IT")
Welcome, MG
you're in IT
```

```python
def print_seconds(hours, minutes, seconds):
    print(3600*hours + 60*minutes + seconds)

print_seconds(1,2,3)
```

```python
def area_triangle(base, height):
  return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b

print("sum of both areas is: " + str(sum)) 

```



- branching with if statements
```python
def hint_username(username):
  if len(username) < 3:
    print("Invalid username.")
  else: 
    print("Valid username.")
```

```python
def is_even(number):
  if number % 2 == 0:
    return True
  return False
```

```python
def hint_username(username):
  if len(username) < 3:
    print("Invalid username.")
  elif len(username) > 15:
      print("Invalid. To many characs")
  else:
    print("Valid username.")
```


## Module 3: Loops  


## Module 4: Strings, Lists and Dictionaries 


## Module 5:  Object Oriented Programming  


## Module 6: Final Project - WordCloud

---

# Using Python to Interact with the Operating System [Link](https://www.coursera.org/learn/python-operating-system)

## Module 1: Getting Your Python On


## Module 2: Managing Files with Python


## Module 3: Regular Expressions


## Module 4: Managing Data and Processes


## Module 5: Testing in Python


## Module 6: Bash Scripting


## Module 7: Final Project - 


---


# Introduction to Git and GitHub [Link](https://www.coursera.org/learn/introduction-git-github?specialization=google-it-automation#syllabus)

## Module 1: Introduction to Version Control


## Module 2: Using Git Locally


## Module 3: Working with Remotes


## Module 4: Collaboration


---


# Troubleshooting and Debugging Techniques [Link](https://www.coursera.org/learn/troubleshooting-debugging-techniques?specialization=google-it-automation)

## Module 1: Troubleshooting Concepts


## Module 2: Slowness


## Module 3: Crashing Programs


## Module 4: Managing Resources


---


# Configuration Management and the Cloud [Link](https://www.coursera.org/learn/configuration-management-cloud?specialization=google-it-automation)

## Module 1: Automating with Configuration Management


## Module 2: Deploying Puppet


## Module 3: Automation in the Cloud


## Module 4: Managing Cloud Instances at Scale


---


# Automating Real-World Tasks with Python [Link](https://www.coursera.org/learn/automating-real-world-tasks-python?specialization=google-it-automation)

## Module 1: Manipulating Images


## Module 2: Interacting with Web Services


## Module 3: Automatic Output Generation


## Module 4: Putting It All Together

