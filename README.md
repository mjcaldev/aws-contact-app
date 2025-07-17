# AWS Contact Form App

A full-stack serverless contact form application built with **React**, **AWS Lambda**, **API Gateway**, **DynamoDB**, and deployed using the **AWS SAM CLI**. A version of this was built for a paying client's form. It demonstrates practical understanding of core AWS services working together to present a practical solution.

## 🧩 Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend   | React + Vite                   |
| Backend    | Python (Flask style handler)   |
| API        | Amazon API Gateway             |
| Compute    | AWS Lambda                     |
| Database   | Amazon DynamoDB                |
| IaC/Deploy | AWS SAM CLI (Serverless Framework) |

---

## 🧠 Features

- 🌐 **Frontend**: Simple contact form built in React + Vite.
- 🔗 **API Gateway**: Accepts POST requests from frontend.
- 🧠 **Lambda Function**: Python handler parses and validates input efficiently only using resources for each action instead of requiring a constant server running.
- 🗃 **DynamoDB**: Contact form submissions are saved serverlessly.
- 🚀 **SAM CLI**: Builds, packages, and deploys the app to AWS in one command.

---

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/aws-contact-app.git
cd aws-contact-app

2. Install frontend dependencies
cd frontend
npm install
npm run dev

3. Setup Python environment
cd ../backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

4. Deploy backend using SAM
sam build
sam deploy --guided
Note: The guided deploy will prompt for AWS region, stack name, etc. These values will be saved in samconfig.toml.

🚧 Deployment Notes
Your deployed API URL will be shown at the end of sam deploy. Use this in your frontend .env:

env
VITE_API_URL=https://your-api-id.execute-api.us-east-1.amazonaws.com/Prod/contact

Be sure to add the following to your .gitignore:
gitignore
node_modules/
.venv/
frontend/dist/
backend/.aws-sam/

📂 Project Structure (ignore dependencies dirs)
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
| Topic       | Key Takeaway                                    |
| ----------- | ----------------------------------------------- |
| CORS        | Configure at API Gateway, not Lambda            |
| .aws-sam/   | Exclude build artifacts from git history        |
| IAM Roles   | Use least-privilege principles between services |
| Git Hygiene | Clean with `.gitignore` and `git rm --cached`   |

🔑 Key Architectural Benefits
✅ Fully serverless, cost-efficient for low-traffic workloads
✅ Event-driven: API Gateway → Lambda → DynamoDB
✅ No infrastructure to manage or scale manually
✅ Follows AWS best practices for MVP-scale applications


📬 Contact
Built by Micheal J. Callaghan (mjcaldev)