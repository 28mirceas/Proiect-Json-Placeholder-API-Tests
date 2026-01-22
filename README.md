# Json-Placeholder-API-Tests Project

## Overview
This project demonstrates **API (REST) testing** skills using both **automated testing in Python** and **Postman collections**. The README is optimized for **GitHub and HR evaluation**, being easy to read and understand.

The tested application is **JSONPlaceholder**, a public API frequently used for QA practice. The project covers **positive**, **negative**, and **edge case** scenarios, as well as the identification and documentation of non-compliant behaviors (BUGs).

---

## QA Skills Demonstrated
- API (REST) testing
- Test automation with **pytest + requests**
- Manual and automated testing with **Postman**
- Test design: positive, negative, edge cases
- Data-driven testing
- Bug identification and documentation
- Project structuring according to QA best practices

---

## Technologies Used
- **Python 3**
- **pytest** – testing framework
- **requests** – HTTP client
- **Postman** – API testing collections
- **JSON** – data format
- **Git / GitHub** – version control

---

## 📁 Project Structure
```
project-root/
│── api/
│ └── json_placeholder.py # API call methods
│── tests/
│ ├── test_json_placeholder.py # Positive & data-driven tests
│ └── negative_test_json_placeholder.py # Negative & edge case tests
│── conftest.py # Shared fixtures
│── postman/
│ └── Json_Placeholder.postman_collection.json
│── README.md
```

---

## Configuration
Common configuration data is defined using **pytest fixtures**:

- `base_url` → API base URL
- `default_request_body` → reusable payload for requests

```text
https://jsonplaceholder.typicode.com
```

---

## Tested Endpoints
| Method | Endpoint | Description |
|------|---------|-----------|
| GET | /posts | Retrieve all posts |
| GET | /posts/{id} | Retrieve a post by ID |
| POST | /posts | Create a post |
| PUT | /posts/{id} | Full post update |
| PATCH | /posts/{id} | Partial update |
| DELETE | /posts/{id} | Delete a post |
| GET | /posts/{id}/comments | Retrieve post comments |

---

## Test Coverage

### Positive Tests
- Status code validation (200 / 201)
- Response data validation
- Data-driven tests using pytest.mark.parametrize

### Negative Tests
- Non-existent IDs
- Invalid body (wrong data types)
- Parameters that return no results

### Edge Cases
- Empty body
- null values

> ⚠️ Note: JSONPlaceholder does not validate data.
> Negative tests intentionally document these behaviors as BUGs, simulating a real-world API.

---

## Examples of Identified BUGs
- API returns 200 OK instead of 404 Not Found for non-existent IDs
- API accepts invalid request bodies and returns 201 Created instead of 400 Bad Request
- API accepts null values and empty strings without validation Request**

---

## Running Automated Tests

1.(Optional) Create a virtual environment
2. Install dependencies:
```bash
pip install pytest requests
```
3. Run the tests:
```bash
pytest -v
```

---

## Testing with Postman

1. Import the collection:
   - `Json_Placeholder.postman_collection.json`
2. Set the environment variable:
```text
base_url3 = https://jsonplaceholder.typicode.com
```
3. Run the folders:
- Positive
- Negative
- Edge Cases

The collection contains assertions for status codes and basic response validations.

---

## Project Purpose
- Demonstrating QA & API Testing skills
- Clear and easy-to-evaluate project for recruiters and technical teams
- Practicing test automation
- Documenting bugs in a realistic context

---

## Author
**QA Tester**

---

## License
Educational project, intended for personal portfolio use.
