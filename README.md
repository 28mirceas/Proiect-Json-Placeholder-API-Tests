# Proiect-Json-Placeholder-API-Tests

## Prezentare generală
Acest proiect demonstrează competențe de **testare API (REST)** folosind atât **testare automată în Python**, cât și **colecții Postman**. README-ul este optimizat pentru **GitHub și evaluare HR**, fiind ușor de parcurs și de înțeles.

Aplicația testată este **JSONPlaceholder**, un API public utilizat frecvent pentru exerciții QA. Proiectul acoperă scenarii **pozitive**, **negative** și **edge cases**, precum și identificarea și documentarea comportamentelor neconforme (BUG-uri).

---

## Competențe QA demonstrate
- Testare API (REST)
- Automatizare teste cu **pytest + requests**
- Testare manuală și automatizată cu **Postman**
- Design de teste: pozitive, negative, edge cases
- Testare data-driven
- Identificare și documentare bug-uri
- Structurare proiect conform bunelor practici QA

---

## Tehnologii folosite
- **Python 3**
- **pytest** – framework de testare
- **requests** – client HTTP
- **Postman** – colecții de testare API
- **JSON** – format date
- **Git / GitHub** – versionare

---

## 📁 Structura proiectului
```
project-root/
│── api/
│   └── json_placeholder.py        # Metode pentru apeluri API
│── tests/
│   ├── test_json_placeholder.py   # Teste pozitive & data-driven
│   └── negative_test_json_placeholder.py  # Teste negative & edge cases
│── conftest.py                    # Fixture-uri comune
│── postman/
│   └── Json_Placeholder.postman_collection.json
│── README.md
```

---

## Configurare
Datele comune de configurare sunt definite folosind **pytest fixtures**:

- `base_url` → URL de bază al API-ului
- `default_request_body` → payload reutilizabil pentru request-uri

```text
https://jsonplaceholder.typicode.com
```

---

## Endpoint-uri testate
| Metodă | Endpoint | Descriere |
|------|---------|-----------|
| GET | /posts | Obținerea tuturor postărilor |
| GET | /posts/{id} | Obținerea unei postări după ID |
| POST | /posts | Crearea unei postări |
| PUT | /posts/{id} | Actualizare completă postare |
| PATCH | /posts/{id} | Actualizare parțială |
| DELETE | /posts/{id} | Ștergerea unei postări |
| GET | /posts/{id}/comments | Comentariile unei postări |

---

## Acoperire teste

### Teste pozitive
- Validare coduri de status (200 / 201)
- Validare date din response
- Teste data-driven folosind `pytest.mark.parametrize`

### Teste negative
- ID-uri inexistente
- Body invalid (tipuri de date greșite)
- Parametri care nu returnează rezultate

### Edge cases
- Body gol
- Valori `null`

> ⚠️ **Notă:** JSONPlaceholder nu validează datele.
> Testele negative documentează intenționat aceste comportamente ca **BUG-uri**, simulând un API real.

---

## Exemple de BUG-uri identificate
- API returnează **200 OK** în loc de **404 Not Found** pentru ID-uri inexistente
- API acceptă body invalid și returnează **201 Created** în loc de **400 Bad Request**
- API acceptă valori `null` și string-uri goale fără validare

---

## Rulare teste automate

1. (Opțional) Creează un virtual environment
2. Instalează dependențele:
```bash
pip install pytest requests
```
3. Rulează testele:
```bash
pytest -v
```

---

## Testare cu Postman

1. Importă colecția:
   - `Json_Placeholder.postman_collection.json`
2. Setează variabila de environment:
```text
base_url3 = https://jsonplaceholder.typicode.com
```
3. Rulează folderele:
- Positive
- Negative
- Edge Cases

Colecția conține assert-uri pentru coduri de status și validări de bază ale răspunsurilor.

---

## Scopul proiectului
- Demonstrarea competențelor de **QA & API Testing**
- Proiect clar și ușor de evaluat pentru **recrutori și echipe tehnice**
- Exersarea automatizării testelor
- Documentarea bug-urilor într-un context realist

---

## Autor
**QA Tester**

---

## Licență
Proiect educațional, destinat portofoliului personal.
