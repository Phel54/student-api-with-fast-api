from fastapi.testclient import TestClient

from server.app import app

client = TestClient(app)



def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==  {'message': 'Welcome to this fantastic app!'}
    

def createStudent():
    response = client.post("/student/",json={
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            })
    assert response.status_code == 200
    assert response.json() ==  {'message': 'Welcome to this fantastic app!'}
    
    
    