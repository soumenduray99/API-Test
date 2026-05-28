
# Tableau Compatible REST API

This fixed version resolves:
- NaN JSON issue
- Infinity issue
- Timestamp serialization issue
- Tableau REST Connector parsing issue

## Render Deployment

Build Command:
pip install -r requirements_tableau_final.txt

Start Command:
gunicorn tableau_final_fixed_flask_api:app

## API Endpoints

/api/data
/api/tables
/api/table/Orders
/api/table/Returns
/api/table/People

## Tableau Recommended Setup

Endpoint:
/api/table/Orders

Method:
GET

JSON Path:
$[*]
