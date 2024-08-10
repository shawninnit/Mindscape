from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for resources and support groups
resources = [
    {"title": "Coping with Stress", "description": "Tips and strategies to manage stress effectively."},
    {"title": "Mindfulness Meditation", "description": "Guided meditation to help you stay centered."},
    {"title": "Building Resilience", "description": "Learn how to bounce back from challenges."},
]

support_groups = [
    {"name": "Anxiety Support Group", "description": "Connect with peers facing similar challenges."},
    {"name": "Study-Life Balance", "description": "Discuss how to balance academic demands with personal life."},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resources')
def show_resources():
    return render_template('resources.html', resources=resources)

@app.route('/mindfulness')
def mindfulness():
    return render_template('mindfulness.html')

@app.route('/support')
def support():
    return render_template('support.html', groups=support_groups)

@app.route('/add_resource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        resources.append({"title": title, "description": description})
        return redirect(url_for('show_resources'))
    return render_template('add_resource.html')

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        support_groups.append({"name": name, "description": description})
        return redirect(url_for('support'))
    return render_template('add_group.html')

if __name__ == '__main__':
    app.run(debug=True)
