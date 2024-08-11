import google.generativeai as genai

# API key should be securely handled, consider using environment variables instead
API_KEY = "AIzaSyD4lULdKzwzUzIwDaY80TWTx5tBneVIuqU"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_response_from_model(user_input):
    response = model.generate_content(user_input)
    return response.text  # Assuming 'content' contains the generated text

user_input = input("Enter Your Prompt = ")
output = get_response_from_model(user_input)
print(output)
