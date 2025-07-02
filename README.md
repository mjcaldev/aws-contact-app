# AWS Contact Form App

A fully serverless contact form application built with **React**, **AWS Lambda**, **API Gateway**, **DynamoDB**, and deployed using the **AWS SAM CLI**. A version of this project actually worked for an unpaid client and simultaneously demonstrates functional understanding of core AWS services working together to form a common solution.

## 🧩 Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend   | React + Vite                   |
| Backend    | Python (Flask style handler)   |
| API        | Amazon API Gateway             |
| Compute    | AWS Lambda                     |
| Database   | Amazon DynamoDB                |
| IaC/Deploy | AWS SAM (Serverless Framework) |

---

## 🧠 Features

- 🌐 **Frontend**: Simple contact form built in React.
- 🔗 **API Gateway**: Accepts POST requests from frontend.
- 🧠 **Lambda Function**: Python handler parses and validates input.
- 🗃 **DynamoDB**: Contact form submissions are saved serverlessly.
- 🚀 **SAM CLI**: Builds, packages, and deploys the app to AWS in one command.

---

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/aws-contact-app.git
cd aws-contact-app
2. Install frontend dependencies
bash
Copy
Edit
cd frontend
npm install
npm run dev
3. Setup Python environment
bash
Copy
Edit
cd ../backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
4. Deploy backend using SAM
bash
Copy
Edit
sam build
sam deploy --guided
Note: The guided deploy will prompt for AWS region, stack name, etc. These values will be saved in samconfig.toml.

🚧 Deployment Notes
Your deployed API URL will be shown at the end of sam deploy. Use this in your frontend .env:

env
Copy
Edit
VITE_API_URL=https://your-api-id.execute-api.us-east-1.amazonaws.com/Prod/contact
Be sure to add the following to your .gitignore:

gitignore
Copy
Edit
node_modules/
.venv/
frontend/dist/
backend/.aws-sam/
📂 Project Structure
arduino
Copy
Edit
aws-contact-app/
├── backend/
│   ├── contact_form/
│   │   └── app.py
│   ├── template.yaml
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── index.html
│   └── vite.config.ts
└── README.md
🧠 Lessons Learned
Topic	Learning
SAM CLI	Cors: must be under the Api resource, not Function
.aws-sam/ Cleanup	Ignoring .aws-sam avoids 1000s of unnecessary git diffs
CORS	Use Globals > Api > Cors for broad CORS config
Git Hygiene	Use .gitignore proactively + git rm -r --cached for retroactive fix

📬 Contact
Built by Micheal J. Callaghan (mjcaldev)