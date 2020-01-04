from firebase import firebase

firebase=firebase.FirebaseApplication("https://pythontest-29138.firebaseio.com/",None)
name=input("Enter your name")
age=input("Enter your age")
data={
    'Name':name,
    'Age':age
}
result=firebase.post('/pythontest-29138/New',data)
result2=firebase.get('/pythontest-29138/New','')
print(result2)
