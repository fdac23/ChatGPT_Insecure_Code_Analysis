from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database of subscribed users (email addresses)
subscribed_users = set(["user1@example.com", "user2@example.com", "user3@example.com"])

# Endpoint for unsubscribing users
@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')

    if email in subscribed_users:
        # User is subscribed, remove them from the database
        subscribed_users.remove(email)
        return jsonify({"message": f"Unsubscribed user with email: {email}"})
    else:
        # User is not subscribed
        return jsonify({"message": f"User with email: {email} is not subscribed"})

if __name__ == '__main__':
    app.run(debug=True)