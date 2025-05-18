from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value (a=97, A=65)
            base = ord('a') if char.islower() else ord('A')
            # Apply the shift
            if encrypt:
                shifted = (ord(char) - base + shift) % 26
            else:
                shifted = (ord(char) - base - shift) % 26
            # Convert back to character
            result += chr(base + shifted)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def process():
    result = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        shift = int(request.form.get('shift', 3))
        action = request.form.get('action', 'encrypt')
        
        if action == 'encrypt':
            result = caesar_cipher(text, shift, True)
        else:
            result = caesar_cipher(text, shift, False)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
