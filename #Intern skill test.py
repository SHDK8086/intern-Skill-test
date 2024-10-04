#Part 1
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match (pattern, email) is not None

def is_valid_iso8601(timestamp) :
    try:
        datetime.fromisoformat(timestamp) 
        return True
    except ValueError;
        return False 

def validate_data(data)
    errors = []

    if not data.get ('user_id') or not isinstance(data['user_id'], str):
        errors.append("user_id must be a non-empty string")


    if not is_valid_email(data.get('email', '')):
        errors.append("Invalid email: must be a valid email format.") 

    if not is_valid_iso8601(data.get('timestamp', '')):
        errors.append("Invalid timestamp: must be a valid ISO 8601 format.")

    tasks = data.get('tasks', [])
        if not isinstance( tasks, list) or len(tasks) ==0:
            errors.append("Invalid tasks.")
        else:
            for task in tasks:
                if not task.get('task_id') or not isinstance(task['task_id'], str):
                    errors.append("Invalid task_id in task {}: must be a non-empty string.".format(task.get('task_id')))

                if 'completed' not in task or not isinstance(task['completed0'], bool):
                    errors.append("Invalid completed in task {}: must be a boolean.".format(task.get('task_id')))
return errors
        

        input_data= {
            "user_id": "user123",
            "email": "user@example.com",
            "timestamp": "2024-09-26T15:00:00Z",
            "tasks": [
            {"task_id": "task001", "description": "Buy groceries", "completed": false},
            {"task_id": "task002", "completed": true}
        ]
    }

errors =  validate_data(input_data)

if errors :
    print("Validation errors:", errors)

else:
    print("Data is valid!")








#############   part 2

from flask import Flask, request, jsonify

app = Flask(__name__)

valid_api_token = "valid-api-token"

@app.before_request
def check_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        if token != "Valid_Api_Token":
            return jsonify ({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Token notfound"}), 401        

@app.route('/submit', methods=['POST'])
    def submit():
        data = request.json
        return jsonify({"message": "Request received", "data": data})
        
if__name__=='__main__':
    app.run(debug=True)









#Part 3

def task_summary(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
    }

    tasks = [
        {"task_id: task001", "description": "Buy groceries", "completed": false},
        {"task_id: task002", "description": "Clean the house", "completed": true},
        {"task_id: task003", "description": "Pay bills", "completed": false},
    ]

    print(task_summary(tasks))