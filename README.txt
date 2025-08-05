# ServiceNow External Agent (AI Helper)

This Flask app simulates an AI agent that receives software installation requests via POST `/install` and responds with a success message.

## Example JSON POST Payload

```json
{
  "software": "VS Code",
  "user": "jdoe",
  "device": "LAPTOP-123"
}
