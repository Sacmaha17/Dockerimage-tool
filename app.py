from flask import Flask, request, render_template, flash, redirect
import subprocess, os

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os.environ['GIT_USERNAME'] = request.form['git_user']
        os.environ['GIT_TOKEN'] = request.form['git_token']
        base_image = request.form['base_image']
        request.files['config_file'].save('config/input.yaml')
        with open('config/base_image.txt', 'w') as f:
            f.write(base_image)

        try:
            subprocess.run(['python3', 'scripts/fetch_files.py'], check=True)
            subprocess.run(['python3', 'scripts/generate_dockerfile.py'], check=True)
            subprocess.run(['buildah', 'bud', '-t', 'custom-image', '.'], check=True)
            flash("Image built successfully via Buildah ✅", "success")
        except subprocess.CalledProcessError as e:
            flash(f"Build failed: {e}", "danger")

        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
