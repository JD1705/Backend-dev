# Backend Development Learning Project  

## Description  
This project is designed to practice the core skills and concepts required to become a backend developer. It’s divided into lessons covering topics like:  
- Testing (Pytest),  
- Database operations (MongoDB, PostgreSQL),  
- API development (FastAPI),  
- and more.  

The lessons are structured with the help of an AI assistant, which provides explanations and examples. I document the key concepts in this README for others to follow along.  

**Note**: Python is the primary language used, so basic proficiency is required. FastAPI knowledge is helpful but not mandatory—I’ll cover the basics in [Lesson 2](#lesson-2).  

## Requirements  
### Core Dependencies  
- FastAPI (for building APIs)  
- Pytest (for testing)  

### Databases  
- MongoDB  
- PostgreSQL  

Install all dependencies with:  
```bash  
pip install -r requirements.txt
```

## Lesson 1: Testing with Pytest  

### Objective:  
Learn to write unit tests for functions and APIs using Pytest and FastAPI.  

### Why Testing?  
Imagine building a bridge (an API, a program, etc.). Would you open it to the public without ensuring it won’t collapse? Of course not. Testing is like a **simulation** for your code:  

**Advantages:**  
- Catches errors **before they reach production**.  
- Gives you confidence to make changes.  
- Documents **how your code should work**.  

### What is Pytest?  
Pytest is a Python testing framework designed to simplify writing, running, and maintaining tests. It’s highly flexible, supporting everything from simple tests to complex ones with dependencies.  

**Example:**  
```python  
# test_math.py  
def test_sum():  
    assert 2 + 2 == 4 
```
Run the example by writing ```pytest test_math.py``` in your terminal

- [Pytest Official Documentation](https://docs.pytest.org/)
- [Pytest Quick Guide](https://docs.pytest.org/en/stable/getting-started.html)